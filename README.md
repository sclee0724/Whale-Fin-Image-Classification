# 🐳 고래 지느러미 이미지 분류 모델 #
----------------------------
+ 이 프로젝트는 전북대 창의적 IT 공학설계의 결과물이다. 
### 프로젝트 계획이유 ###
> 여러분들은 고래를 직접 본적이 있나요? 보셨다면 굉장히 좋은 경험을 하셨네요 일반적으로 고래는 국내에서 보기는 매우 힘듭니다. 광활하고 푸른 태평양 한가운데 있더라도 보기 힘들죠 만약에 여러분들이 운 좋게 고래를 가까이서 보더라도 물 위에 솟아오른 지느러미일 확률이 큽니다. 그럼에도 굉장한 경험인만큼 여러분들은 해당 고래의 정체가 궁금하겠죠. 지느러미만 보고서 어느 고래인지 일반인이 구별하는 것은 굉장히 어렵습니다. 하지만 걱정하지 마세요 저희가 구현한 모델을 통해 빠르고 정확하게 어느 종인지 분별해드립니다!
-------------------------------
### 모델 소개 ##
> 저희 웹에 내장된 모델은 Vggnet(vgg11)을 기반으로 구현한 CNN(합성 곱 신경망)이며, 약 21000장의 데이터를 확보하여 140회 학습이 되어있습니다. 이렇게 학습된 모델을 통해 총 15종의 고래의 정체를 밝힐 수 있습니다. 아쉽게도 고래를 제외한 다른 해양포유류(돌고래, 상어)는 분류 대상이 아니며 저희 모델이 지원하는 고래종은 왼쪽 이미지와 같습니다. 직접 이미지를 넣고 확인해보세요!

+ 분류가능 대상 

    대왕고래 | 흑범고래 | 혹등고래 | 고양이고래 | 보리고래
    ---- | ---- | ---- | ---- | ----
    멸치고래 | 큰고래 | 범고래 | 밍크고래 | 돌쇠고래
    민부리고래 | 귀신고래 | 참거두고래 | 돌고양이고래 | 남방참고래
-------------------------------
### 모델 사용법 ###
+ 웹 서버 구동 파일 이름 : server.py
    + 서버를 구동할 경우
        > 파일 경로를 설정한후 다음과 같이 입력
        <pre><code>
        python app.py
        </code></pre>
-------------------------------

![KakaoTalk_20220811_230845463](https://user-images.githubusercontent.com/79682941/184157292-bc23e744-b01c-46ff-98c8-942f39729972.png)

![KakaoTalk_20220811_230929582](https://user-images.githubusercontent.com/79682941/184157295-5773aa36-3174-4fbc-8ee8-a7ab0e87877a.png)

이 프로젝트는 Eoryeong_Goh, Chaeu_Park, Seungheon_Ok, Seungchan_Lee에 의해 만들어짐

