from PIL import Image
from pyzbar.pyzbar import decode
data = decode(Image.open('hasil.png'))
print(data[0][0].decode('UTF-8'))