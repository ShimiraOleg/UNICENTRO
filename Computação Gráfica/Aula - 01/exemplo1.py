import cv2

img = cv2.imread('lena.png', cv2.IMREAD_UNCHANGED)
cv2.imshow('BGRA',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('testando.avif', img)