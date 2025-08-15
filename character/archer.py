from character.character_base import CharacterBase

class Archer(CharacterBase):

    def __init__(self, name, hp, attack_damage):
        self.name = name
        self.hp = hp
        self.attack_damage = attack_damage

    def double_attack(self, target):
        for _ in range(2):
            self.base_attack(target)