import cv2

from canny import cannyEdge
from gray import grayScale

#함수 선언부


#전역 변수부
src = None
dst1, dst2, dst3 = None, None, None # 영상처리 결과


#메인 코드부
src = cv2.imread('C:\GitHubLecture\images\picture11.jpg') #이미지 읽기

dst1 = grayScale(src)
dst2 = cannyEdge(src)

cv2.imshow('src', src)      #화면 출력
cv2.imshow('dst1', dst1)    #화면 출력
cv2.imshow('dst2', dst2)    #화면 출력


## 마무리
cv2.waitKey(0)
cv2.destroyAllwindows()


