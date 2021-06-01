import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("TYPE U ARE OWN WORD")
qr.png('mycode.png',scale=8)

d = decode(Image.open("mycode.png")) # this code is use to decode the QRimage image  
print(d[0].data.decode("ascii"))     ## this code is use to decode the QRimage image
