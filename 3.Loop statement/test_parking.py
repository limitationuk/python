import datetime

# (1)초기 데이터 설정
parking_lot = []            # 주차장 자리
num_floor = 10              # 층수
spots_floor = 10            # 층별 자리

# 리스트 개수로 층수, 값 "[]" 개수로 층별 자리 구현
for i in range(num_floor):
    spots = []
    for j in range(spots_floor):
        spots.append("[]")
    parking_lot.append(spots)

parked_records = {}  # 주차 기록
subscribers = {  # 정기권 가입자(차량번호: 할인율)
    "12가3456": 0.5,
    "65나4321": 0.8,
    "12다3456": 0.3,
    "65라4321": 0.6
}
while True:  # 'exit'입력할 때 까지 무한 반복
    print("[주차장 현황]")
    for i in range(len(parking_lot)):                       # 주차장 주차 현황
        print(f"{i+1}층: {' '.join(parking_lot[i])}")

    command = input("\n1)입차, 2)출차, 3)exit 입력: ")        # 기능 선택

    # (2)입차 기능
    if command == "1":
        # 차량 번호, 주차 위치 입력
        car_number = input("차량 번호를 입력하세요: ")
        if not car_number in parked_records:                               # 이미 주차되어 있는지 확인
            floor = int(input("층수를 입력하세요: "))
            spots = int(input("자리(번호)를 입력하세요: "))
            if 1 <= floor <= 10 and 1 <= spots <= 10:                      # 입력 값 검사
                if parking_lot[floor-1][spots-1] == "[]":                  # 빈자리인지 체크
                    parking_lot[floor-1][spots-1] = "[X]"                  # 주차된 자리로 변경
                    entry_time = datetime.datetime.now()                   # 현재 시간 자동 입력
                    parked_records[car_number] = {
                        "entry_time": entry_time,
                        "floor": floor,
                        "spots": spots
                    }
                    print(f"차량번호: {car_number}, 입차시간: {entry_time} \n주차되었습니다. ")         
                else:
                    # 같은 층에서 가장 가까운 빈자리 탐색       
                    find_spot = None
                    min_distance = spots_floor + 1   # 최소거리 - 전체 자리보다 크게 초기화
                                                    
                    for idx in range(len(parking_lot[floor-1])): # 사용자가 선택한 층에 빈자리가 있는지 탐색  
                        if parking_lot[floor-1][idx] == "[]":    # 빈자리가 있다면
                            distance = abs((idx+1) - spots)      # 사용자가 선택한 자리와의 거리 계산
                            if min_distance > distance:          # 최소거리인 빈자리 찾기
                                min_distance = distance         
                                find_spot = idx + 1              # 사용자에게 안내하기 위해 +1

                    if find_spot:
                        print(f"이미 주차된 자리입니다. 가까운 빈자리는 {floor}층 {find_spot}번 자리입니다.")
                    else:
                         print(f"{floor}층에는 빈자리가 없습니다.")             
            else:
                print("범위를 벗어났습니다.")
        else:
            print("이미 주차된 차량입니다.")

    # (3)출차 기능
    elif command == "2":
        # 차량번호 입력 및 조회
        # 시간에 따른 요금 계산
        # 정기차량의 경우 할인율 적용
        # 주차 자리 빈자리로 변경                                                                                                                                                      
        print("")

    # 프로그램 종료
    elif command == "3":
        print("\n프로그램을 종료합니다.")
        break

    else:
        print("다시 입력해주세요.")
