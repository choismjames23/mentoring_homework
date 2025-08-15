from utils.set_character import set_character
from utils.get_info import get_character_info, get_hp_info, get_character_names
from utils.user_action import select_user_action

playing_character = []

if __name__ == "__main__":
    #캐릭터 생성
    count = int(input("생성할 캐릭터 수를 입력하세요 : "))
    for _ in range(count):
        playing_character.append(set_character())

    print("현재 생성된 캐릭터 목록 : ", get_character_names(playing_character))

    #게임 진행
    while True:
        for character in playing_character:
            if get_hp_info(character) <= 0:
                break
        
        select_user_action(playing_character)