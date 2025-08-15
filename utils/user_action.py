from utils.get_info import get_hp_info, get_character_info, get_character_names

#user_action = ["캐릭터 정보 확인","캐릭터 체력 확인","공격","스킬"]

def select_user_action(character_list):
    #character_list : 캐릭터 인스턴스가 담긴 리스트
    #playing_character : 캐릭터 이름이 담긴 리스트
    playing_character = get_character_names(character_list)
    action = int(input("하고 싶은 행동을 입력하세요.(1.캐릭터 정보 확인, 2.캐릭터 체력 확인, 3.공격) : "))

    if action == 1:
        name = str(input(f"정보를 확인할 캐릭터 이름을 입력하세요.({playing_character}) : "))
        if name in playing_character:
            get_character_info(character_list[playing_character.index(name)])
        else:
            print("존재하지 않는 캐릭터 입니다.")
    elif action == 2:
        name = str(input(f"체력을 확인할 캐릭터 이름을 입력하세요.({playing_character}) : "))
        if name in playing_character:
            print(f"{name} 캐릭터의 현재 체력은 {get_hp_info(character_list[playing_character.index(name)])} 입니다.")
        else:
            print("존재하지 않는 캐릭터 입니다.")
    elif action == 3:
        pass
    else:
        print("유효한 행동이 아닙니다.")