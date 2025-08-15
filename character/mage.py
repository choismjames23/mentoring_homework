from character.character_base import CharacterBase

class Mage(CharacterBase):

    def __init__(self, name, hp, attack_damage):
        self.name = name
        self.hp = hp
        self.attack_damage = attack_damage

    # 자신의 체력을 20 회복
    def heal(self):
        self.hp += 20