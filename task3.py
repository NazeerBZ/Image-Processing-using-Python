#Accessing specific region of an image 

import cv2;

img = cv2.imread('ballondor.jpg');
gcImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);

face = gcImg[195:460, 422:609];

gcImg[0:265, 210:397] = face;

cv2.imshow('image',gcImg);
cv2.waitKey(0);
cv2.destroyAllWindows();
