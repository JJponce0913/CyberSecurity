from io import BytesIO
from PIL import Image
import base64

# Base64 string of the image
base64_image = "VBORw0KGgoAAAANSUhEUgAABNEAAABkBAMAAABayruYAAAAJFBMVEUAAADa2tr/////9/e6urpTU1O5ubn39/f///9ZWVlfX1/z8"
# Decode Base64 string to bytes
image_bytes = base64.b64decode(base64_image)

# Open the image using Pillow
image = Image.open(BytesIO(image_bytes))

# Save the image to a file
image.save('decoded_image.png')


# Show the image
image.save('decoded_image.png')
