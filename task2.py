#Accessing each pixal in an image(2darray)

import cv2;

img = cv2.imread('ballondor.jpg');
gcImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);

for i in range(len(gcImg)):
    for j in range(len(gcImg[i])):
        gcImg[i][j] = gcImg[i][j] ** 2;


cv2.imshow('image',gcImg);
cv2.waitKey(0);
cv2.destroyAllWindows();
