"""
변수는 데이터를 저장할 수 있는 식별자(identifier).
별도의 선언 없이 값을 할당하는 순간 변수가 생성.
변수는 메모리의 특정 공간을 참조하고 있으며, 그 공간에 데이터가 저장.
파이썬은 동적타이핑(dynamic typing) 언어이므로, 변수에 저장되는 값의 자료형은 자동으로 결정.
"""
#변수의 생성과 출력: str
name = "Han"

print(f"Hello, {name}")
print(type(name))       #변수의 자료형 확인

sent = 'She sais, "EWW!"'

print(sent)
print(type(sent))

print("----" * 5)


#변수의 생성과 출력: str
score = 80

print(f"Score: {score}")
print(type(score))

height = 170.1

print(f"Height: {height}")
print(type(height))

print("----" * 5)


#변수의 생성과 출력: list
fruits = ['apple', 'banana', 'cherry']

print(fruits)
print(f"I love {', '.join(fruits)}.")               
    #.join()은 문자열 메소드로 join() 앞에 있는 문자열(이 경우 ', ')을 구분자로 사용하여, 괄호 () 안의 반복 가능한 객체 (리스트, 튜플 등)에 있는 각 요소를 하나로 합친다.
print(f"Among them, I love {fruits[0]} the most.")
print(type(fruits))

print("----" * 5)


#변수의 생성과 출력: tuple
gold = (1, "Yuna Kim")
silver = (2, "mao Asada")
bronze = (3, "Joannie Rochette")

print("[Ranked Results]")
print(f"{gold[0]}st place: {gold[1]}")
print(f"{silver[0]}nd place: {silver[1]}")
print(f"{bronze[0]}rd place: {bronze[1]}")

print("\n[Medal Winners]")          #\n 줄바꿈
print(f"Gold Medal: {gold[1]}")
print(f"Silver Medal: {silver[1]}")
print(f"Bronze Medal: {bronze[1]}")

print("\n[Ranked list]")
medals = [gold, silver, bronze]     #리스트에 튜플 대입
for rank, name in medals:           #medals 갯수만큼 medals 값을 rank, name에 대입 반복
    print(f"Rank {rank}: {name}")

print("----" * 5)


#변수의 생성과 출력: dictionary
menus = {
    "Americano": 3000,
    "Latte": 3500,
    "Cappuccino": 4000,
    "Mocha": 4500
}

print("[single menu and cost]")
print(menus["Americano"])
print(f"Americano costs {menus["Americano"]} won.")

print("\n[menus infomation]")
print(menus.keys())                   #menus.keys(): 딕셔너리의 모든 키만 모아서 보여줍니다. 
print(list(menus))  
print(f"{list(menus)[0]} costs {list(menus.items())[0][1]} won.")

print(menus.items())                  #menus.items(): 딕셔너리의 모든 키와 값 쌍을 한꺼번에 보여줍니다. 이 쌍들은 튜플 형태로 이루어져 있습니다.
print(f"{list(menus.items())[0][0]} costs {list(menus.items())[0][1]} won.")

print("\n[Price information]")
print(menus.values())                #menus.values(): 딕셔너리의 모든 값만 모아서 보여줍니다. 

print("\n[All menus]")
for menu in menus:
    print(menu)

print("\n[All costs]")
for price in menus.values():
    print(price)



