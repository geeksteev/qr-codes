import cv2 
import logging
import argparse

    # parent = argparse.ArgumentParser()
    # parent.add_argument('-i', '--input', help='Read QR codes from an image or webcam.', choices=['image', 'camera'], type=str, required=True)
    
    # parser = argparse.ArgumentParser(parents=[parent])
    # parser.add_argument('-f', '--file', help='Image to read.',  type=str, required=False)
    
def readQRCodeFromImage(src_file):
    img = cv2.imread(src_file)
    detect = cv2.QRCodeDetector()
    # write_log(str(detect.detectAndDecode(img)[0]).strip("(',')"))
    return str(detect.detectAndDecode(img)[0]).strip("(',')")


if __name__ == "__main__":
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument('--parent', type=int)
    
    foo_parser = argparse.ArgumentParser(parents=[parent_parser])
    foo_parser.add_argument('foo')
    foo_parser.parse_args(['--parent', '2', 'XXX'])
    
    print(foo_parser.parse_args())