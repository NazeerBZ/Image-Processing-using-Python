#Reading, Writing and Converting Image to Greyscale Image
import cv2;

colorImg = cv2.imread('ballondor.jpg');
gcImg = cv2.cvtColor(colorImg, cv2.COLOR_BGR2GRAY);
cv2.imwrite('ballondorGrey.png', gcImg);

cv2.imshow('image', cv2.imread('ballondorGrey.png'));
cv2.waitKey(0)
cv2.destroyAllWindows();
