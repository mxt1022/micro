import cv2 as cv
from pyzbar.pyzbar import decode
import webbrowser#跳转到网站链接

data=['link']#二维码链接,至少有一个元素

#img= cv.imread("test.jpg")
cap=cv.VideoCapture(0)
#二维码标点
while True:
    success,img=cap.read()
    code=decode(img)
    #print(code)
    for qr in code:
        qr_data = qr.data.decode('utf-8')
        #print(qr_data)  # b：字节为单位，需要转换
        if (qr_data!=data[-1]):#与最后一个不一样，加载到列表，否则是一个false
            data.append(qr_data)
            webbrowser.open(qr_data)
            print(data)

        point = qr.rect

        #画矩形框，显示网站链接
        cv.rectangle(img, (point[0], point[1]), (point[0] + point[2], point[1] + point[3]), (200, 20, 200), 5)
        cv.putText(img, qr_data, (point[0] - 20, point[1] - 20), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (20, 0, 255))

    cv.imshow("output", img)
    #如果按下ESC，终止
    if cv.waitKey(1) & 0xFF ==27:
        break
