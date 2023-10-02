import cv2
import datetime

data = "https://en.m.wikipedia.org"
logfile = "quirky.log"

with open(logfile, 'r+') as f:
    lines = f.readlines()
    for line in lines:
        if line.find(data.split(".")[1]) == True:
            continue
        else:
            f.write(f'\n{str(str(datetime.datetime.now()).split(".")[0] + " " + data)}')
