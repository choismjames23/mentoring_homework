from character.character_base import CharacterBase

class Archer(CharacterBase):

    def __init__(self, name):
        self.name = name
        self.attack_damage = 7

    # 2회 연속 공격 스킬
    def double_attack(self, target):
        for _ in range(2):
            self.base_attack(target)