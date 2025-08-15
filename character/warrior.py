from character.character_base import CharacterBase

class Warrior(CharacterBase):

    def __init__(self, name, hp, attack_damage):
        self.name = name
        # 전사의 체력은 기본 캐릭터보다 100 높다
        self.hp = hp + 100
        self.attack_damage = attack_damage