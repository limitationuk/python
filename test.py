users = {
    "uid1": {
        "name": "한정욱",
        "birth": "1998-07-15",
        "id": "user1",
        "password": "@pass1",
        "role": "viewer"
    },
    "uid2": {
        "name": "개발자",
        "birth": "1995-03-12",
        "id": "user2",
        "password": "@pass2",
        "role": "editor"
    },
    "uid3": {
        "name": "관리자",
        "birth": "1990-01-01",
        "id": "user3",
        "password": "@pass3",
        "role": "admin"
    }
}

print("[전체 사용자 목록]")
for uid, info in users.items():
    print(f"uid: {uid}, name: {info["name"]}, birth: {info["birth"]}, role: {info["role"]}")


print("기능 선택")
print("1) 회원가입")
print("2) 로그인")
choice = input("번호 입력: ")

#회원가입
if choice == "1":
    new_id = input("새 아이디: ")

    existing_ids = [info['id'] for info in users.values()]

    if new_id in existing_ids:
        print("닉네임이 존재합니다.") 
    else:
        name = input("이름: ")
        birth = input("생년월일(yyyy-mm-dd): ")

        if len(birth) == 10 and birth[4] == "-" and birth[7] == "-":
            password = input("비밀번호(8자리, 특수문자): ")

            special = any(ch in "!@#$%^&*" for ch in password)
            
            if len(birth) >= 10 and special:
                role = input("viewer, editor, admin: ")

                if role in ["viewer", "editor", "admin"]:
                    users[new_id]={
                        "name": name,
                        "birth": birth,
                        "id": new_id,
                        "password": password,   
                        "role": role
                    }
                    print("회원가입 성공!")

                    #전체 사용자 출력
                    print("[전체 사용자 목록]")
                    for uid,info in users.items():
                        print(f"name: {info['name']}, birth: {info['birth']}, id: {info['id']}, role: {info['role']}")
                else:
                    print

            


        

elif choice == "2" :
    print("잘못 입력하였습니다.")
else:
    print("잘못 입력하였습니다.")