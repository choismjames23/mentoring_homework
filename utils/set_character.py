from character.archer import Archer
from character.mage import Mage
from character.warrior import Warrior

def set_character():
    character = int(input("생성할 직업군의 숫자를 입력하세요(1.전사 2.궁수 3.마법사) : "))
    character_name = str(input("생성할 캐릭터의 이름을 입력하세요 : "))
    
    if character == 1:
        character_name = Warrior(f"{character_name}")
        print(f"전사 캐릭터 {character_name.name} 가 생성되었습니다.")
    elif character == 2:
        character_name = Archer(f"{character_name}")
        print(f"궁수 캐릭터 {character_name.name} 가 생성되었습니다.")
    elif character == 3:
        character_name = Mage(f"{character_name}")
        print(f"마법사 캐릭터 {character_name.name} 가 생성되었습니다.")
    else:
        print("잘못된 숫자를 입력했습니다.")

    return character_name