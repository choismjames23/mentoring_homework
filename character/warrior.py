from character.character_base import CharacterBase

class Warrior(CharacterBase):

    def __init__(self, name):
        self.name = name
        # 전사의 체력은 기본 캐릭터보다 100 높다
        self.hp += 100
        self.attack_damage = 10