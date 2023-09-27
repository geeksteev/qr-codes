import cv2

img = cv2.imread('shirt3.png')
detect = cv2.QRCodeDetector()
retval, decoded_info, points, straight_qrcode = detect.detectAndDecodeMulti(img)

print(detect.detectAndDecodeMulti(img))