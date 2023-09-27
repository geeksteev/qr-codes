import cv2 
import qrcode
import argparse

def readQRCodeFromImage(filename):
    img = cv2.imread(filename)
    detect = cv2.QRCodeDetector()
    return str(detect.detectAndDecode(img)[1]).strip("(',')")

def readQRCodeFromVideo():
    cam = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    
    while True:
        _, img = cam.read()
        data, bbox, _ = detector.detectAndDecode(img)
        if data:
            print("QR Code Detected:  ", data)
        if cv2.waitKey(1) == ord("Q"):
            break
    
    cam.release()
    cv2.destroyAllWindows()
    return
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--generate', help='Generate a QR Code', required=False)
    parser.add_argument('-r', '--read', help='Read a QR Code', required=False)
    parser.add_argument('-f', '--file', help='Read a QR Code', required=False)
    parser.add_argument('-u', '--url', help='Enter the URL for the QR code', required=False)
    parser.add_argument('-o', '--output', help='Enter the output filename for the QR code image', required=False)
    
args = parser.parse_args()

readQRCodeFromVideo()