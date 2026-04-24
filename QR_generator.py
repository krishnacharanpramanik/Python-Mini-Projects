import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=20, border=3)
qr.add_data('https://static.toiimg.com/thumb/msid-126097253,imgsize-19732,width-400,resizemode-4/why-are-you-gay-viral-meme-sensation-simon-kaggwa-njala-reacts-to-being-called-the-piers-morgan-of-uganda.jpg')
qr.make(fit=True)
img=qr.make_image(fill_color='Black', back_color='White')
img.save('You_are.png')