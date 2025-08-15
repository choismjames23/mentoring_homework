from typing import List

def get_character_info(name):
    print(f"< {name.name} 캐릭터 정보 > 이름 : {name.name} , 체력 : {name.hp} , 데미지 : {name.attack_damage}")

def get_hp_info(name):
    return name.hp

def get_character_names(character_list: List):
    return [character.name for character in character_list]