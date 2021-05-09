import cv2 as cv
import numpy as np
import os.path
import sys,getopt

def rescale(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
def grayscale(frame):
    gray=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    return gray
def blurring(frame):
    blur=cv.GaussianBlur(frame,(7,7),cv.BORDER_DEFAULT)
    return blur
def cascading_op(frame):
    canny=cv.Canny(frame,125,175)

    return canny
def load_image(path):
    if os.path.isfile(path):
        image=cv.imread(path.replace('\\','/'))
        return image
    else:
        print("File does not exist")
try:
    if(sys.argv[1]=='--help'):
        print("image_operations.py : \n Performs various operations on a jpg file\nusage: python image_operations.py '[path]' [operation]\n[operation]:1:Rescale\t2:Grayscale\t3:Blur\t4:Cascade\n")
    else:
        path=sys.argv[1]
        img=load_image(path)
        n=int(sys.argv[2])
        if (n==1):
            s=float(input("Enter the scale(0 to 1):"))
            if(s>0 and s<1):
                img=rescale(img,s)
            else:
                img=rescale(img)
            cv.imshow('Rescaled',img)
            cv.waitKey(0)
        elif(n==2):
            img=grayscale(img)
            cv.imshow('Grayscaled',img)
            cv.waitKey(0)
        elif(n==3):
            img=blurring(img)
            cv.imshow('Blurred',img)
            cv.waitKey(0)
        elif(n==4):
            img=cascading_op(img)
            cv.imshow('Cascaded',img)
            cv.waitKey(0)
        else:
            print("usage: python image_operations.py '[path]' [operation]\n[operation]:1:Rescale\t2:Grayscale\t3:Blur\t4:Cascade\n")
except IndexError:
    print("usage: python image_operations.py '[path]' [operation]\n[operation]:1:Rescale\t2:Grayscale\t3:Blur\t4:Cascade\n")