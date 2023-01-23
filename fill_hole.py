import glob, tqdm
import cv2

li = glob.glob('./*_bg_removed.png')
for cur in li:
    gray = cv2.imread(cur, 0)
    # print(gray.max(), gray.min())
    gray[gray < 127] = 0
    gray[gray > 0] = 1
    # des = cv2.bitwise_not(gray)
    des = gray
    contour,hier = cv2.findContours(des,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
    print(contour, hier)

    for cnt in contour:
        cv2.drawContours(des,[cnt],0,255,-1)

    gray = des
    # gray = cv2.bitwise_not(des)
    cv2.imwrite(cur.replace('_bg_removed.png', '_mask.png'), gray)
