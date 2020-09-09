import cv2
import numpy as np

img=cv2.imread(r"C:\Users\dp\Desktop\py4e\opencv\database\shape2.png")
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,yy=cv2.threshold(imggray,20,255,cv2.THRESH_BINARY)
contours,hierarch=cv2.findContours(yy, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("totall contour found are-",len(contours))#to find how many contours are there
cv2.drawContours(img,contours,-1,(0,0,255),2)
print("area and perimeter of all contours are->")
for cnt in contours:
    area=cv2.contourArea(cnt)
    print(area)
    peri=cv2.arcLength(cnt,True)
    print(peri)
    approx=cv2.approxPolyDP(cnt,0.02*peri,True)#cornor points
    if(len(approx)==3):#instread of printing you can use cv2.putText to disply it on screen
        print("It can be Triangle")
    elif(len(approx)==4):
        print("It can be quadiletral")
    elif(len(approx)==5):
        print("It can be pentagan")
    elif(len(approx)==6):
        print("It can be hexagon")
    else:
        print("It can be circle")
    x,y,w,h=cv2.boundingRect(approx)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
        
cv2.imshow("s",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

