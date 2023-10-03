import cv2 
import time
import logging
import argparse

logging.basicConfig(filename="quirky.log", level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S', filemode='a')
logger = logging.getLogger()

def readQRCodeFromImage(src_file):
    img = cv2.imread(src_file)
    detect = cv2.QRCodeDetector()
    data, bbox, _ = detect.detectAndDecode(img)
    if data:
        write_log(str(detect.detectAndDecode(img)[0]).strip("(',')"))
        print("QR code written to log: " + data)
    else:
        print("ERROR: No QR code found in " + args.file)

def readQRCodeFromCamera():
    cam = cv2.VideoCapture(0)
    detect = cv2.QRCodeDetector()
    
    while True:
        _, img = cam.read()
        data, bbox, _ = detect.detectAndDecode(img)
        if data:
            write_log(str(detect.detectAndDecode(img)[0]).strip("(',')"))
            print("QR code written to log: " + data)
        if cv2.waitKey(1) == ord("Q"):
            break
    
    cam.release()
    cv2.destroyAllWindows()
    return

def write_log(log_entry):
    logging.info(log_entry) 
    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", choices=['image', 'stream', 'parse'])
    parser.add_argument("-f", "--file")
    parser.add_argument("-o", "--output")
    
    args = parser.parse_args()
    