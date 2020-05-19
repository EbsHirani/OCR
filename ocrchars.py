#Read Chars
import cv2
import pytesseract
import numpy as np 
import os

os.environ["TESSDATA_PREFIX"] = "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata\\"

IMAGE = "image.png"

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

img = cv2.imread(IMAGE)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

height, width, _ = img.shape

for b in  pytesseract.image_to_boxes(img).splitlines():
	x, y, w, h = map(int,b.split()[1:5])
	c = b.split()[0]
	cv2.rectangle(img, (x,height - y), (w,height - h), (0,255,0), 1)
	cv2.putText(img, c, (x ,height - y +25), cv2.FONT_HERSHEY_COMPLEX, 1 , (0,255,0), 1)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows() 



