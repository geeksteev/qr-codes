import cv2 
import datetime
import logging
import argparse

# data = "https://en.m.wikipedia.org"
# log = "quirky.log"
# src_file = ".tests/investopedia.png"
# timestamp = str(str(datetime.datetime.now()).split(".")[0] + " " + data)

logging.basicConfig(filename="quirky.log", level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S', filemode='a')
logger = logging.getLogger()

def readQRCodeFromImage(src_file):
    img = cv2.imread(src_file)
    detect = cv2.QRCodeDetector()
    write_log(str(detect.detectAndDecode(img)[0]).strip("(',')"))
    return 

def readQRCodeFromCamera():
    cam = cv2.VideoCapture(0)
    detect = cv2.QRCodeDetector()
    
    while True:
        _, img = cam.read()
        data, bbox, _ = detect.detectAndDecode(img)
        if data:
            write_log(str(detect.detectAndDecode(img)[0]).strip("(',')"))
            if cv2.waitKey(1) == ord("Q"):
                break
    
    cam.release()
    cv2.destroyAllWindows()
    return

def write_log(log_entry):
    logging.info(log_entry) 
    return

if __name__ == "__main__":
    parent_parser = argparse.ArgumentParser(add_help=False)
    child_parser = argparse.ArgumentParser(parents=[parent_parser])
    
  
readQRCodeFromCamera()