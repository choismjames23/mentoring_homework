from utils.set_character import set_character

playing_character = []

if __name__ == "__main__":
    count = int(input("생성할 캐릭터 수를 입력하세요 : "))
    for _ in range(count):
        playing_character.append(set_character())

    print("현재 생성된 캐릭터 목록 : ", [character.name for character in playing_character])

