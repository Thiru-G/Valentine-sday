import os
from PIL import Image
import pillow_heif  # enables HEIC support

# register HEIC
pillow_heif.register_heif_opener()

INPUT_DIR = "/Users/thiru/Downloads/Val"     # folder with your images
OUTPUT_DIR = "./converted"      # output folder (game-photos)
QUALITY = 60               # good for websites

os.makedirs(OUTPUT_DIR, exist_ok=True)

valid_ext = (".jpg", ".jpeg", ".png", ".heic", ".JPG", ".PNG", ".HEIC")

index = 19

for file in sorted(os.listdir(INPUT_DIR)):
    if not file.endswith(valid_ext):
        continue

    in_path = os.path.join(INPUT_DIR, file)
    out_path = os.path.join(OUTPUT_DIR, f"{index}.avif")

    try:
        with Image.open(in_path) as img:
            img = img.convert("RGBA")  # safe for transparency
            img.save(
                out_path,
                format="AVIF",
                quality=QUALITY,
                speed=4
            )

        print(f"✔ {file} → {index}.avif")
        index += 1

    except Exception as e:
        print(f"✖ Failed: {file} ({e})")

print("\nDone. Real AVIF files generated.")
