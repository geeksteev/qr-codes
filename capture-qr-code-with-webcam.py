import cv2

# initialize the video capture device
webcam = cv2.VideoCapture(0)

# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()


while True:
    _, img = webcam.read()
    data, bbox, _ = detector.detectAndDecode(img)
        
    if data:
        a = data
        break

    cv2.imshow("QR Code Scanner", img)

    if cv2.waitKey(1) == ord('q'):
        break

print(str(a))
