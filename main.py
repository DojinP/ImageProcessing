import cv2

#함수 선언부



#전역 변수부
src = None
dst1, dst2, dst3 = None, None, None # 영상처리 결과


#메인 코드부
src = cv2.imread('C:\GitHubLecture\images\picture11.jpg') #이미지 읽기



cv2.imshow('source', src)

## 마무리
cv2.waitKey(0)
cv2.destroyAllwindows()


