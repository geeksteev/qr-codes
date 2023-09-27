import cv2

webcam = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

while True: # Turn this into a try/catch and the if data: into, if data, print it to the console
    _, img = webcam.read()
    data, bbox, _ = detector.detectAndDecode(img)

    if data:
        a = data
        break

    if cv2.waitKey(1) == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()

print(data)