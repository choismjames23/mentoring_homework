from character.character_base import CharacterBase

class Mage(CharacterBase):

    def __init__(self, name):
        self.name = name
        self.attack_damage = 8

    # 자신의 체력을 20 회복
    def heal(self):
        self.hp += 20