import cv2

def grayEdge(src) :

    dst = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)

    return dst
