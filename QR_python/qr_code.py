from dataclasses import dataclass
from numpy import true_divide
from pyparsing import White
import qrcode


qr = qrcode.QRCode(
    version=1 ,
    box_size=20,
    border=15
)
data = 'https://www.facebook.com/mussie.freneh'
qr.add_data(data)
qr.make(fit=true_divide)
img =qr.make_image(fill = 'black', back_color = 'White') 
img.save('qr_reslut.png')