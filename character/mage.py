from character.character_base import CharacterBase

class Mage(CharacterBase):

    def __init__(self, name, hp, attack_damage):
        self.name = name
        self.hp = hp
        self.attack_damage = attack_damage