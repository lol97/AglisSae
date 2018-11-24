import qrcode
import cv2
import numpy as np
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img_cv = np.array(img,dtype=np.uint8)
cv2.imshow("eheh",img_cv)
cv2.waitKey()