# -*- coding: utf-8 -*-

import cv2

class Detect_HAAR:

    
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        cv2.namedWindow("detect", cv2.WINDOW_NORMAL)

        #HAAR分類器の顔検出用の特徴量
        #cascade_path = "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
        self.cascade_path = "C:\opencv\data\haarcascades\haarcascade_frontalface_alt.xml"
        #cascade_path = "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml"
        #cascade_path = "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_alt_tree.xml"

    def detect(self):
        if self.cap.isOpened():
            color = (255, 255, 255) #白
            #color = (0, 0, 0) #黒

            frame = self.cap.read()

            k = cv2.waitKey(1)
            if k == 27:
                break

            #グレースケール変換
            image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            #カスケード分類器の特徴量を取得する
            cascade = cv2.CascadeClassifier(cascade_path)

            #物体認識（顔認識）の実行
            #image – CV_8U 型の行列．ここに格納されている画像中から物体が検出されます
            #objects – 矩形を要素とするベクトル．それぞれの矩形は，検出した物体を含みます
            #scaleFactor – 各画像スケールにおける縮小量を表します
            #minNeighbors – 物体候補となる矩形は，最低でもこの数だけの近傍矩形を含む必要があります
            #flags – このパラメータは，新しいカスケードでは利用されません．古いカスケードに対しては，cvHaarDetectObjects 関数の場合と同じ意味を持ちます
            #minSize – 物体が取り得る最小サイズ．これよりも小さい物体は無視されます
            facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(40, 40))
            #facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=3, minSize=(10, 10), flags = cv2.cv.CV_HAAR_SCALE_IMAGE)

            if len(facerect) > 0:
                #検出した顔を囲む矩形の作成
                for rect in facerect:
                    print(rect)
                    cv2.rectangle(frame, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)

            cv2.imshow("detect", frame)
            return facerect


    cap.release()
    cv2.destroyAllWindows()
