class CharacterBase:

    def __init__(self, name, hp, attack_damage):
        self.name = name
        self.hp = hp
        self.attack_damage = attack_damage


    def base_attack(self, target):
        target.hp -= self.attack_damage