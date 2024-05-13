from collections import defaultdict

def solution(fees, records):
    # 요금표 정보
    basic_time, basic_fee, unit_time, unit_fee = fees
    
    # 차량별 주차 시작 시간을 기록할 딕셔너리
    parking_start_time = defaultdict(int)
    # 차량별 주차 총 시간을 기록할 딕셔너리
    parking_total_time = defaultdict(int)
    
    # 주차 기록을 처리하여 주차 시작 시간 및 총 주차 시간 기록
    for record in records:
        time, car_number, action = record.split()
        time = int(time.split(':')[0]) * 60 + int(time.split(':')[1])  # 시간을 분 단위로 변환
        if action == 'IN':
            parking_start_time[car_number] = time
        else:
            start_time = parking_start_time.pop(car_number)
            parking_time = time - start_time
            parking_total_time[car_number] += parking_time
    
    # 미출차 차량에 대한 처리
    for car_number, start_time in parking_start_time.items():
        time = 23 * 60 + 59  # 마지막 시간을 23:59로 설정
        parking_time = time - start_time
        parking_total_time[car_number] += parking_time
    
    # 주차 요금 계산
    parking_fees = []
    for car_number, total_time in sorted(parking_total_time.items()):
        total_fee = basic_fee
        # 기본 시간을 초과하는 경우 추가 요금 계산
        if total_time > basic_time:
            extra_time = total_time - basic_time
            total_fee += ((extra_time - 1) // unit_time + 1) * unit_fee
        parking_fees.append(total_fee)
    
    return parking_fees