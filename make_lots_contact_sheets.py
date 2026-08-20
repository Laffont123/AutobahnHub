from pathlib import Path
from PIL import Image, ImageOps, ImageDraw, ImageFont
import json

manifest = json.loads(Path('/tmp/canonical_lots_1_12.json').read_text())
files = manifest['canonicalFiles']
src = Path('/home/ubuntu/upload')
out = Path('/home/ubuntu/autobahnhub/audits/lots1to12_contact_sheets')
out.mkdir(parents=True, exist_ok=True)
font = ImageFont.load_default()
cols = 5
cell_w, cell_h = 320, 250
per_sheet = 20
for sheet_index in range((len(files) + per_sheet - 1) // per_sheet):
    chunk = files[sheet_index * per_sheet:(sheet_index + 1) * per_sheet]
    sheet = Image.new('RGB', (cols * cell_w, ((len(chunk) + cols - 1) // cols) * cell_h), '#111827')
    draw = ImageDraw.Draw(sheet)
    for pos, filename in enumerate(chunk):
        x = (pos % cols) * cell_w
        y = (pos // cols) * cell_h
        try:
            image = Image.open(src / filename).convert('RGB')
            image.thumbnail((cell_w - 12, cell_h - 38))
            tile = Image.new('RGB', (cell_w - 12, cell_h - 38), '#1f2937')
            tile.paste(image, ((tile.width - image.width) // 2, (tile.height - image.height) // 2))
            sheet.paste(tile, (x + 6, y + 6))
        except Exception as exc:
            draw.text((x + 8, y + 8), f'ERROR {filename}: {exc}', fill='white', font=font)
        draw.text((x + 8, y + cell_h - 24), filename, fill='#f9fafb', font=font)
    path = out / f'lot1to12_sheet_{sheet_index + 1:02d}.jpg'
    sheet.save(path, quality=90)
print(f'created {len(list(out.glob("*.jpg")))} sheets in {out}')
