#pip install PILLOW

from PIL import Image

in_img = 'input_image.png'
out_img = 'compressed_image.png' 

# Open the image
with Image.open(in_img) as img:
    # Save the compressed image
    img.save(out_img, 'PNG', quality=80)

print(f"Image compressed successfully!")