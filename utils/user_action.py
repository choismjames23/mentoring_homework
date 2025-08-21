from utils.get_info import get_hp_info, get_character_info, get_character_names

#user_action = ["캐릭터 정보 확인","캐릭터 체력 확인","공격","스킬"]

def select_user_action(character_list):
    #character_list : 캐릭터 인스턴스가 담긴 리스트
    #playing_character : 캐릭터 이름이 담긴 리스트
    playing_character = get_character_names(character_list)
    action = int(input("하고 싶은 행동을 입력하세요.(1.캐릭터 정보 확인, 2.캐릭터 체력 확인, 3.공격, 4.스킬 사용) : "))

    # 캐릭터 정보 확인
    if action == 1:
        name = str(input(f"정보를 확인할 캐릭터 이름을 입력하세요.({playing_character}) : "))
        if name in playing_character:
            get_character_info(character_list[playing_character.index(name)])
        else:
            print("존재하지 않는 캐릭터 입니다.")

    # 캐릭터 체력 확인
    elif action == 2:
        name = str(input(f"체력을 확인할 캐릭터 이름을 입력하세요.({playing_character}) : "))
        if name in playing_character:
            print(f"{name} 캐릭터의 현재 체력은 {get_hp_info(character_list[playing_character.index(name)])} 입니다.")
        else:
            print("존재하지 않는 캐릭터 입니다.")

    # 공격하기 
    elif action == 3:
        attack_name = str(input(f"공격할 캐릭터 이름을 입력하세요.({playing_character}) : "))
        target_name = str(input(f"공격 타겟 캐릭터 이름을 입력하세요.({playing_character}) : "))
        if attack_name and target_name in playing_character:
            character_list[playing_character.index(attack_name)].base_attack(character_list[playing_character.index(target_name)])
            print(f"{attack_name} 가 {target_name} 를 공격하였습니다. 데미지 : {character_list[playing_character.index(attack_name)].attack_damage}, {target_name} 체력 : {get_hp_info(character_list[playing_character.index(target_name)])} ")
        else:
            print("대상이 올바르지 않습니다.")

    # 스킬 사용하기        
    elif action == 4:
        print("스킬 목록은 다음과 같습니다.(전사: 공격력 증가, 궁수: 더블 어택, 마법사: 셀프 힐)")
        name = str(input(f"스킬을 사용할 캐릭터 이름을 입력하세요.({playing_character}) : "))

        # 전사
        if character_list[playing_character.index(name)].job == 'warrior':
            character_list[playing_character.index(name)].power_up()
            print(f'{name} 캐릭터의 공격력이 5 증가하였습니다. 현재 공격력 : {character_list[playing_character.index(name)].attack_damage}')

        # 궁수
        elif character_list[playing_character.index(name)].job == 'archer':
            target_name = str(input(f"공격 타겟 캐릭터 이름을 입력하세요.({playing_character}) : "))
            if target_name in playing_character:
                character_list[playing_character.index(name)].double_attack(character_list[playing_character.index(target_name)])
                print(f"{name} 가 {target_name} 를 공격하였습니다. 데미지 : {character_list[playing_character.index(name)].attack_damage * 2}, {target_name} 체력 : {get_hp_info(character_list[playing_character.index(target_name)])} ")
            else:
                print("대상이 올바르지 않습니다.")

        # 마법사
        elif character_list[playing_character.index(name)].job == 'mage':
            character_list[playing_character.index(name)].heal()
            print(f'{name} 캐릭터가 체력을 20 회복했습니다. 현재 체력 : {character_list[playing_character.index(name)].hp}')

        else:
            print('스킬 사용 가능한 직업군이 아닙니다.')

    else:
        print("유효한 행동이 아닙니다.")