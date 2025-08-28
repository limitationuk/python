# 사용자 정보
users = {
    "ID1": {
        "name": "abc123",
        "password": "abc123",
        "phone": "010-1234-5678",
        "email": "elice@example.com"
    },
    "ID2": {
        "name": "qwe456",
        "password": "qwe456",
        "phone": "010-9876-5432",
        "email": "fred@example.com"
    }
}

# 투두리스트 정보
todolist = {
    "ID1": {
        "20250828": {
            "list1": "python 과제",
            "list2": "python 수업 복습"
        },
        "20250829": {
            "list1": "python 수업 복습",
            "list2": "토론 준비"
        }
    },

    "ID2": {
        "20250828": {
            "list1": "linux 과제",
            "list2": "linux 수업 복습"
        },
        "20250829": {
            "list1": "linux 수업 복습",
            "list2": "토론 준비"
        }
    }
}

# 로그인 입력
username = input("아이디 입력: ")
password = input("비밀번호 입력: ")

# name, password 검사
logged_in_user = None
for uid, info in users.items(): #반복문으로 users의 정보를 확인  
    if info["name"] == username and info["password"] == password: #입력한 name, password와 일치하는지 확인
        
        logged_in_user = uid #로그인된 유저의 uid를 저장
        break

if logged_in_user:      
    print(f"{username}님 로그인 성공!")

    # 해당 유저의 투두리스트 불러오기
    user_todolist = todolist[logged_in_user]

    # 날짜 입력
    day = input(f"[날짜 목록] \n{'\n'.join(user_todolist.keys())}\n- 날짜 입력: ")

    # 해당 날짜가 있는지 확인
    if day in user_todolist:
        print(f"[{day} TodoList]\n{user_todolist[day]}")
    else:
        print("해당 날짜는 없음. 새로 추가.")
        user_todolist[day] = {}

    # 리스트 아이템 추가/수정/삭제
    status = input("추가:1, 수정:2, 삭제:3 : ")

    if status == "1":
        key = input("추가할 리스트 이름: ")
        if key in user_todolist[day]:
            print("이미 존재하는 리스트 이름")
        else:
            value = input("할 일 입력: ")
            user_todolist[day][key] = value

    elif status == "2":
        key = input("수정할 리스트 이름: ")
        if key in user_todolist[day]:
            value = input("새로운 내용: ")
            user_todolist[day][key] = value
        else:
            print("해당 리스트 없음")

    elif status == "3":
        key = input("삭제할 리스트 이름: ")
        if key in user_todolist[day]:
            del user_todolist[day][key]
        else:
            print("해당 리스트 없음")

    print("[변경된 전체 투두리스트]")
    print(user_todolist)

else:
    print("로그인 실패")
