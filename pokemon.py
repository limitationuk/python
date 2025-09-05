from abc import ABC, abstractmethod

class Pokemon(ABC):

    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.hp = 100

    @abstractmethod
    def attack(self,other): #구현하지 않으면 인스턴스화 불가능
        pass

    # @abstractmethod
    # def special_atack(self, other):
    #     pass
    
    def defend(self, damage):
        self.hp -= damage
        print(f"{self.name}가 데미지{damage}를 입었습니다. HP:{self.hp}")
        if self.hp <=0:
            self.faint()

    def faint(self):
        print(f"{self.name}의 상태가 전투불능입니다.")

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("피카츄",1) #상위클래스 함수
    
    def attack(self,other):
        damage = 20 + self.level
        other.defend(damage)
        print(f"전기공격 {damage}")

class Jamanbo(Pokemon):
    def __init__(self):
        super().__init__("잠만보",10)
    
    def attack(self,other):
        damage = 40 + self.level
        other.defend(damage)
        print(f"잠만보 {damage}")

#덕 타이핑에 대한 예시, Pokemon을 상속받지 않았지만 attack함수를 가지고 있기 때문에 배틀에 참여할 수 있다.
#사용하지 않는게 좋다.
class SomeDigimon():  
    def attack(self, other):
        damage = 50 + self.level
        other.defend(damage)
        print(f"어떤 디지몬 {damage}")


def battle(pokemon1, pokemon2):
    for _ in range(5):
        pokemon1.attack(pokemon2)
        pokemon2.attack(pokemon1)

p = Pikachu()
j = Jamanbo()
d = SomeDigimon()

battle(p,d)

