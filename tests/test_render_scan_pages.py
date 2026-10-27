import csv
import hashlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path

import fitz
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("render_scan_pages", ROOT / "scripts/render_scan_pages.py")
module = importlib.util.module_from_spec(spec)
import sys
sys.modules[spec.name] = module
spec.loader.exec_module(module)

class RendererTests(unittest.TestCase):
    def test_parser(self):
        self.assertEqual(module.parse_command('/render 001 2-3').last_page,3)
        for command in ['/render 001 0', '/render 001 8-4', '/render 001 1-10', '/render 001 1; echo bad', '/render abc 1']:
            with self.subTest(command=command),self.assertRaises(ValueError): module.parse_command(command)

    def test_image_only_pdf_end_to_end(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t)
            (root/'001').mkdir()
            source=root/'001'/'scan.pdf'
            im=Image.new('RGB',(1600,2200),'white')
            ImageDraw.Draw(im).text((200,200),'SCANNED FINANCIAL TABLE -- TOTAL 125000',fill='black')
            j=io.BytesIO();im.save(j,format='JPEG',quality=90)
            doc=fitz.open()
            for _ in range(3):
                page=doc.new_page(width=800,height=1100)
                page.insert_image(page.rect,stream=j.getvalue())
            doc.save(source)
            doc.close()
            sha=hashlib.sha256(source.read_bytes()).hexdigest()
            with (root/'direct_pdf_links.csv').open('w',newline='') as f:
                w=csv.DictWriter(f,fieldnames=['serial','repository_path','sha256']);w.writeheader();w.writerow({'serial':'001','repository_path':'001/scan.pdf','sha256':sha})
            result=module.render('/render 001 1-3',root,root/'direct_pdf_links.csv',root/'out')
            self.assertEqual(result['pages'],[1,2,3])
            self.assertTrue(result['images'])
            self.assertTrue(all(x['size_bytes']<750_000 for x in result['images']))
            self.assertTrue((root/'out'/'manifest.json').is_file())

if __name__=='__main__':unittest.main()
