from PIL import Image
import pillow_heif
import os

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    if f == "hp.py":
        continue
    heic_image = f
    heif_file = pillow_heif.read_heif(heic_image)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
    )
    ext = heic_image[-5:]
    jpg_image = heic_image.replace(ext,".jpg")
    print(jpg_image)
    image.save(jpg_image, format="jpeg")
