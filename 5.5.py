import numpy as np

# 호그와트 입학 루트
# 대전에서 오사카 유니버셜스튜디오 호그와트까지

# 기름값, 연비, 이동 거리를 입력받아 여행 경비를 계산
def calculate_travel_cost(fuel_price_per_liter: float, fuel_efficiency_km_per_liter: float, distance_km: float) -> float:
    # 필요한 기름의 양을 계산 (이동 거리 / 연비)
    fuel_needed_liters = distance_km / fuel_efficiency_km_per_liter
    
    # 전체 비용 계산 (기름 필요량 * 기름값)
    total_cost = fuel_needed_liters * fuel_price_per_liter
    
    # 소수점 둘째 자리까지 반올림
    return np.round(total_cost, 2)  

fuel_price = 1699  # 1리터당 기름값 (원)
fuel_efficiency = 12  # 자동차 연비 (km/l) 큰 차량이라 연비가 나쁘다.
distance_1 = 53  # 이동 거리 (km)
distance_2 = 45.8  # 두번째 이동 거리 (km)

# 청주공항에서 간사이공항까지 비행기 티켓 비용
plane_ticket_price = 300000

# 대전에서 청주공항까지
travel_cost_1 = calculate_travel_cost(fuel_price, fuel_efficiency, distance_1)

# 간사이공항에서 유니버셜 스튜디오 까지
travel_cost_2 = calculate_travel_cost(fuel_price, fuel_efficiency, distance_2)

# 총 경비 계산 (첫번째 경비 + 두번째 경비 + 비행기 값)
total_travel_cost = travel_cost_1 + travel_cost_2 + plane_ticket_price

print(f"총 여행 경비는 {total_travel_cost}원입니다.")
