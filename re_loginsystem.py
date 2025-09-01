from enum import Enum
import json

class Role(str,Enum): #복습
    ADMIN = 'admin'
    VIEWER ='viewer'
    EDITOR = 'editor'

users = {
    "한정욱": {
        "password": "@pass1",
        "role": Role.VIEWER
    },
    "개발자": {
        "password": "@pass2",
        "role": Role.EDITOR
    },
    "관리자": {
        "password": "@pass3",
        "role": Role.ADMIN
    }
}

print("[All users]")
print(json.dumps(users,indent=2))

print("="*30)

run= True 
while run:
    print("Runnig..")
    work = input("Sign up: 1 / log in: 2")
    if work == "1":
        print("Welcome new user!")
        userid = input("Type your id")
        if not userid in users:
            print("ID available.")
            users[userid] = {}
            userpw = input("Type password(over 4 character): ")
            if len(userpw) > 4:
                users[userid]["password"] = userpw
                #birthday

            else:
                print("Retry (over 4 character)")    

        else:
            print("Retry: existing id")
    elif work == "2":
        print("Happ to see you again!")
        userid = input("id")
        userpw = input("pw")
        if userid in users:
            if userpw == users[userid]["password"]:
                print("Login Seccsed")


            else:
                print("wrong pass")
        else:
            print("wromg id")
    else:
        print("Wrong input") 

    run = bool(input("Rerun? yes any key / no nothing" ))