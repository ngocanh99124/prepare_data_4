import cv2
import numpy as np
import os



def is_fake(img):
    w, h = img.shape[0], img.shape[1]
    print(w, h)
    if w > h*2:
        print("is_fake")
        return -1
    if h < w/10:
        print("is_fake")
        return -1
    img = cv2.fastNlMeansDenoisingColored(img,None,5,5,3,5)

    img = cv2.detailEnhance(img, sigma_s=3, sigma_r=0.7)

    img_copy = img.copy()
    kernel = np.ones((3, 3), np.float32) / 9
    blur_img = cv2.filter2D(img_copy, -1, kernel)
    img_gray = cv2.cvtColor(blur_img, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(img_gray, 0, 255)
    size = img.shape[0]*img.shape[1]
    index = np.sum(np.count_nonzero(edged))
    print(index)
    if index == 0 or index/size < 0.001:
        print("is_fake")
        return -1
    return 1


mi = 1
link = "C:\\Users\\ThinkPad\\Desktop\\2dong"
for filename in os.listdir(link):
    img = cv2.imread(os.path.join(link, filename))
    mi = is_fake(img)
    if mi != -1:
        print(filename)
