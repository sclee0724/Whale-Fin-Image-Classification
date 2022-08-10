def name_title(value):
    return {
        'blue_whale' : '대왕고래 (blue_whale)',
        'brydes_whale' : '멸치고래 (brydes_whale)',
        'cuviers_beaked_whale' : '민부리고래 (cuviers_beaked_whale)',
        'false_killer_whale' : '흑범고래 (false_killer_whale)',
        'fin_whale' : '큰고래 (fin_whale)',
        'gray_whale' : '귀신고래 (gray_whale)',
        'humpback_whale' : '흑동고래 (humpback_whale)',
        'killer_whale' : '범고래 (killer_whale)',
        'long_finned_pilot_whale' : '참거두고래 (long_finned_pilot_whale)',
        'melon_headed_whale' : '고양이고래 (melon_headed_whale)', 
        'minke_whale' : '밍크고래 (minke_whale)',
        'pygmy_killer_whale' : '들고양이고래 (pygmy_killer_whale)',
        'sei_whale' : '보리고래 (sei_whale)', 
        'short_finned_pilot_whale' : '들쇠고래 (short_finned_pilot_whale)',
        'southern_right_whale' : '남방참고래 (southern_right_whale)'
    }.get(value, '우리 데이터에는 이런 사진 없어요 (^0^)')

def switch(value):
    return {
        'blue_whale' : '흰긴수염고래라고 불리기도 하며 수염고래과에 속하는 고래이다. 현존하는 동물은 물론, 역사상 존재했던 동물 가운데 가장 거대하고 무거운 동물이다. 크릴을 주식으로 먹지만 가끔씩은 크릴외에 작은 물고기를 먹기도 한다. 한국에서는 동해와 서해에 나타나기도 했지만 1944년 이후로 보고가 없다.',
        'brydes_whale' : '브라이드고래라고 하기도 하며 수염고래과에 속하는 종 중 알려진 바가 가장 적은 종이다. 전세계의 따뜻한 온대 및 열대 수역에서 분포하며 물고기를 주식으로 한다.',
        'cuviers_beaked_whale' : '부리고래과에 속하는 고래이다. 모든 부리고래 중 가장 널리 분포하는 고래이며 원양에 서식한다. 선박을 피해 1000m 이상의 깊은 바다를 선호하지만 부리고래 중 가장 흔히 발견된다.',
        'false_killer_whale' : '참돌고래과에서 가장 큰 편에 속하는 고래이다. 전 세계의 온대 및 열대해양에 분포하며 범고래와 유사한 특징을 공유하지만 실제로 두 종의 관계는 깊지않다.',
        'fin_whale' : '수염고래과에 속하는 고래이며 흰긴수염고래와는 다른 긴수염고래라고 부르기도 한다. 흰긴수염고래 다음으로 가장 큰 해양 포유류이다. 전 세계의 대양, 극지방, 열대 지방에 걸쳐 분포하지만 예외로 극지방의 빙산지역에서는 보이지 않는다. 온대 지방에서의 개채밀도 가장 높은것으로 드러났다.',
        'gray_whale' : '귀신고래과에 속한 유일한 고래이다. 북아메리카 태평양 해안을 따라 이동하는 개체군과 동북아시아 연안을 따라 이동하는 개체군 두 가지 개체군이 있다. 연오랑과 세오녀 설화에 나오는 움직이는 바위가 귀신고래의 등이라는 주장이 있다',
        'humpback_whale' : '수염고래과에 속하는 고래이며 수염고래과 혹등고래속에 속하는 유일한 고래이다. 전 세계의 대양에 서식하나 지중해에서는 거의 목격되지 않는다. 최근 DNA 분석결과에 따르면 귀신고래가 혹등고래와 가장 가까운 관계이다.',
        'killer_whale' : '참돌고래과에 속하는 고래 중 가장 큰 종이며 극지방에서 열대지방에 이르기까지 널리 발견되는 고래이다. 제주도, 독도, 울산 앞바다, 서해 등지에서 서식하는 것이 확인되었다. 북극 빙산이 녹기 시작함에 따라 범고래의 출현빈도가 점점 잦아지고 있다.',
        'long_finned_pilot_whale' : '거두고래속에 속하는 종이며 참돌고래과에 속하지만 이들의 행동방식은 다른 대형고래의 것에 가깝다. 처음 태어났을 때에는 75kg 이지만 다 크면 1.8에서 3.5톤까지 나간다. 오징어를 주식으로 하며 가끔씩 물고기도 먹는다.',
        'melon_headed_whale' : '참돌고래과에 속하는 종이며 몸길이 약 2.5m, 몸무게 150~170kg이다. 열대, 아열대 기후의 심해에서 서식하고 한반도에서는 남해에 분포한다.', 
        'minke_whale' : '수염고래과에 속하며 쇠정어리고래라고 하기도 한다. 수컷은 8m, 암컷은 9m 정도로 성장하며 어류, 동물성 플랑크톤, 오징어 등을 먹는다. 세계 각지의 근해에 서식하며 태평양 연안와 한국 동해안에 산다.',
        'pygmy_killer_whale' : '참돌고래과에 속하는 포유류의 일종이며 영어권 명칭 Pygmy Killer Whale 은 작은 범고래라는 의미이며 신체적 특징이 범고래와 유사하기 때문에 붙여진 이름이다. 들고양이고래속에 속하는 유일한 종이다.',
        'sei_whale' : '수염고래과에 속하는 종이다. 전 세계의 대양과 인접한 바다에서 발견되지만 주로 수심이 깊은곳을 선호하기 때문에 극지방, 열지방, 내해지방에서는 잘 발견되지 않는다. 영어명 sei 는 노르웨이어로 대구를 뜻하는데 보리고래와 대구가 항상 해마다 같은 때에 나타난다고 해서 붙은 이름이다.', 
        'short_finned_pilot_whale' : '거두고래속에 속하는 종이다. 참돌고래과에 속하지만 이들의 행동은 대형고래의 것과 가깝다. 같은 거두고래속인 참거두고래와 헷갈릴 수 있지만 여러 차이점이 있다. 이빨의 개수 등이 참거두고래에 비해 적은 편이며 색깔또한 다르다.',
        'southern_right_whale' : '수염고래과에 속하는 종이다. 남극대륙과 가까운 먼 남극해에서 여름을 보내며 다른 참고래와 마찬가지로 동물성 플랑크톤과 크릴을 주식으로 삼는다.'    
        }.get(value, '우리 데이터에는 이런 사진 없어요 (^0^)')