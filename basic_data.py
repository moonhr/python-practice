import numpy as np

# 기초데이터
basic_data = [
  {
  "기차표 왕복" : 80000,
  "카츠멘숀 삿포로라멘 미니안심세트" : 14500,
  "소곱창고기국" : 10000,
  "합천국밥" : 10000,
  "버거킹 롱치킨 버거 세트"  : 5500,
  "숙박비스테이미도" : 55000,
  "굿즈" : 300000,
  "피시방" : 5000,
  "노래방" : 8000,
  "오락실 태고의 달인"  : 3000,
  "오락실 유비트" : 3000,
  "오락실 노스텔지어" : 3000,
  "오락실 팝픈뮤직" : 1000,
  "교통비" : 30000,
  "지스타 입장표값 BTC" : 15000
},
  {
    "여행지": "영국 런던",
    "여행 기간": "12박 14일",
    "총 여행 비용": 4850000,
    "비행기 값 (왕복)": 1000000,
    "식비": 1500000,
    "호텔": 1000000,
    "교통비": 300000,
    "관광비": 1000000,
    "기타 비용 (핸드폰 유심칩 등)": 50000

},
  {
    "숙소": {
        "이름": "코트야드 메리어트",
        "가격": 213000, 
        "박수": 2
    },
    "여행 경비": {
        "교통비": {
            "버스": 1500, 
            "기차": 9600,  
            "이동 횟수": 8
        },
        "기타": 50000 
    },
    "음식": {
        "갈비": 69000, 
        "갈비 횟수": 6, 
        "아이스크림": 10000,  
        "아이스크림 횟수": 3  
    }
},
{
  "로밍" : 50000,
  "자동차 기름 값" : 50000,
  "휴게소 핫도그" : 5000,
  "비행기 값" : 800000,
  "호텔까지 택시" : 20000,
  "호텔비" : 160000,
  "세부 시장" : 70000,
  "저녁" : 60000,
  "간식" : 20000,
  "아점" : 50000,
  "기념품" : 60000,
  "공항까지 택시" : 20000,
},
{
  "to_airport" : 4600,
  "to_osaka" : 411994,
  "JR_pass" : 500000,
  "carrier_bag" : 35000,
  "dinning" : 200000,
  "hotel_per_day" : 83723,
  "exchange_fee" : 9.38,
  "pocket_money" : 200000,
  "roaming" : 30000
},
{
    "여행지": "제주도",
    "기간": 3,
    "식비": 225000,
    "교통비": 120000,
    "숙박비": 360000,
    "기타 비용": 50000
},
{
    "여행 세면 킷": 8000,
    "대전역까지":1500,
    "당일 점심": 8000,
    "대전역에서 청주 공항까지": 10000,
    "청주 공항 -> 오사카": 53000,
    "오사카 -> 나라현": 20500,
    "입장료": 5000,
    "기념품": 10000,
    "사슴 전병": 2000,
    "점심": 8000,
    "저녁": 8000,
    "숙박비": 70000,
    "간식": 4000,
    "해외 데이터 로밍": 2000,
    "환전 수수료": 20000,
    "여행자 보험": 30000,
    "나라현 -> 오사카": 3000,
    "오사카 -> 청주 공항": 53000
},
{
        "lunch":9000, 
        "amusement park ticket": 30000  ,
        "snacks": 8000,
        "drinks": 4000,
        "dinner": 14000,
        "round-train ticket": 64000,
        "room": 60000,
        "bus ticket": 6000
},
{
    "대전역까지 버스 비용 왕복": 3000,
    "대전역에서 광명역까지 기차 왕복": 42400,
    "광명역에서 인천공항까지 리무진 버스 왕복": 24000,
    "인천공항에서 취리히까지 항공편": 3998800,
    "취리히에서 인천공항으로 항공편": 3994100,
    "차량 7일 렌트 비용": 561004,
    "상황에 따라 쓸 돈": 10000000
},
{
    "bus": 54000,
    "flight": 1017800,
    "hotel": 600000,
    "day_1": {
        "title" : "프라하 주요 관광지 탐방",
        "프라하성 입장비": 37000,
        "블타바 강": 0,
        "까를교": 0, 
        "성 니콜라스 교회": 5000, 
        "경비": 70000,
    },
    "day_2": {
        "title" : "프라하 구 시가지 탐방",
        "중세 지하 탐험": 36000,
        "구 시청사": 0,
        "틴 성당": 0, 
        "화약탑": 12000,
        "경비": 70000  
    
    },
    "day_3": {
        "title" : "카를로비 바리 여행",
        "카를로비 바리 교통비": 35000,
        "믈린스카 콜로나다": 29000,
        "푸니 콜라": 18000,
        "길거리 경비": 82000
    },
    "day_4": {
        "title" : "마무리",
        "하벨 시장": 70000
    }
},
{
    "제주도": {
        "거리": 470, 
        "환율": {"10kg귤": 8058}, 
        "숙박비용": {
            "1박_호텔": 120000, 
            "1박_게스트하우스": 50000, 
        },
        "음식비용": {
            "점심_한끼": 12000, 
            "저녁_한끼": 20000, 
        },
        "기타비용": {
            "관광지_입장료": 15000, 
            "교통비": 10000, 
        },
    },
    "도쿄": {
        "거리": 1104.22, 
        "환율": {"1엔": 9.38}, 
        "숙박비용": {
            "1박_호텔": 150000,  
            "1박_게스트하우스": 70000, 
        },
        "음식비용": {
            "점심_한끼": 15000,
            "저녁_한끼": 25000,
        },
        "기타비용": {
            "관광지_입장료": 20000, 
            "교통비": 15000,  
        },
    },
    "그리스": {
        "거리": 8681,
        "환율": {"1유로": 1483.39},
        "숙박비용": {
            "1박_호텔": 200000,  
            "1박_게스트하우스": 100000,
        },
        "음식비용": {
            "점심_한끼": 18000,
            "저녁_한끼": 30000,
        },
        "기타비용": {
            "관광지_입장료": 25000,
            "교통비": 100000,
        },
    },
    "강원도": {
        "거리": 183,  
        "환율": {"10kg감자": 45000},
        "숙박비용": {
            "1박_호텔": 100000,  
            "1박_게스트하우스": 60000,  
        },
        "음식비용": {
            "점심_한끼": 10000,  
            "저녁_한끼": 18000, 
        },
        "기타비용": {
            "관광지_입장료": 10000, 
            "교통비": 8000,  
        },
    },
},
{
    "교통비" : {
        "가는 경비" : 313988.44,
        "오는 경비" : 313988.44,
    },
    "활동비" : {
        "유니버셜 티켓" : 120025,
        "지팡이" : 75400,
        "교복" : 204000,
    },
    "식비" : {
        "버터맥주" : 8000,
        "젤리" : 25060
        }
},
{
  "버스" : 3000,
  "srt" : 35200,
  "라이온즈 파크 파티플로우석 티켓" : 55000,
  "대구 수성 더 아르코 호텔 라이온즈파크점" : 80000,
} 
]

# 모든 키 값을 수집하기
# 중첩된 딕셔너리와 리스트에서 모든 키를 추출하는 함수
def get_all_keys(data, keys=None):
    if keys == None:
        keys = []
    
    # 기저 조건: data가 딕셔너리나 리스트가 아닌 경우
    if not isinstance(data, (dict, list)):
        return keys
    
    # 딕셔너리인 경우
    if type(data) == dict:
        for key, value in data.items():
            keys.append(key)  # 현재 키를 리스트에 추가
            # 값이 딕셔너리나 리스트인 경우 재귀적으로 호출
            if type(value) == dict or type(value) == list:
                get_all_keys(value, keys)
    
    # 리스트인 경우
    elif type(data) == list:
        for item in data:
            # 리스트의 각 요소가 딕셔너리나 리스트인 경우 재귀적으로 호출
            if type(item) == dict or type(item) == list:
                get_all_keys(item, keys)
    
    return keys
  
all_keys = get_all_keys(basic_data)
# print(all_keys)

#교통비 텍스트 가져오기
# text 매개변수는 기본값이 None으로 설정되어 있습니다. 함수 내부에서 text가 None이면 빈 리스트로 초기화합니다. 이 방식 덕분에 text를 명시적으로 제공하지 않아도 됩니다.
def get_traffic_text(data, text=None):
    if text == None:
        text = []

    for traffic in data:
        if "교통" in traffic:
            text.append(traffic)
            
    return text
  
all_traffic = get_traffic_text(all_keys)
print(f"교통을 포함하는 키들: {all_traffic}")

#교통비 금액 가져오기
def get_traffic_price(data, traffic_keys):
    """
    전체 데이터에서 교통비 관련 키와 일치하는 값을 모두 합산하는 함수입니다.

    :param data: 분석할 전체 데이터 (리스트 또는 딕셔너리).
    :param traffic_keys: '교통비'를 포함한 키를 지정한 리스트입니다.
    :return: '교통비' 관련 값의 합계.
    """
    total_sum = 0

    # 재귀적으로 딕셔너리와 리스트를 탐색하며 '교통비' 관련 값을 찾고 합산
    def recursive_sum(data):
        #nonlocal는 부모함수의 변수에 접근
        nonlocal total_sum
        # isinstance 특정 함수의 인스턴스인지 확인
        if isinstance(data, dict):
            for key, value in data.items():
                # 키에 '교통비' 관련 문자열이 포함된 경우 값 합산
                if any(traffic_key in key for traffic_key in traffic_keys):
                    if isinstance(value, (int, float)):
                        total_sum += value
                # 값이 딕셔너리나 리스트인 경우 재귀적으로 호출
                elif isinstance(value, (dict, list)):
                    recursive_sum(value)
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, (dict, list)):
                    recursive_sum(item)

    # 전체 데이터에서 교통비 관련 값을 합산
    recursive_sum(data)
    return total_sum
  
total_traffic_cost = get_traffic_price(basic_data, all_traffic)
print(f"교통비 관련 총합: {total_traffic_cost}")
