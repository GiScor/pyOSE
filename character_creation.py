from character import Character, CharRace, CharClass, RACE_CLASS_LIMITS
from tools import roll, clear_screen
import time

def print_char():
    char = Character('Tizio', 1, CharRace.ELF, CharClass.ROGUE)
    print(char._name)


attr_names = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']

def print_attr(attributes):
    for i in range(0, 6):
        print(f"{attr_names[i]}: {attributes[i]:>5}")
    print("")

def get_level():
    while True:
        raw = input("Select Level: ")
        try:
            level = int(raw)
            if level < 1:
                raise ValueError()
            return level
        except ValueError:
            print("Please enter a whole positive number")

def get_race():
    races = list(CharRace)
    print("Choose a race:")
    i = 0
    for race in races:
        i += 1
        print(f"{i}. {race.value}")

    while True:
        raw = input("\nType the number (1-10)\n")
        try:
            race_num = int(raw)
            return races[race_num - 1]
        except ValueError:
            print("Please enter a number in the range shown above")

def get_class(crace):
    limits = RACE_CLASS_LIMITS[crace]
    classes = [c for c in limits if limits[c] != 0]
    print("Choose a class:")
    for i, c in enumerate(classes, start=1):
        cap = limits[c]
        cap_str = "Unlimited" if cap is None else cap
        print(f"{i:>2}. {c.value:<15}"
              f"Max Level: {cap_str}")
    while True:
        raw = input("\nType the class number: ")
        try:
            class_num = int(raw)
            if not (1 <= class_num <= len(classes)):
                raise ValueError
            return classes[class_num - 1]
        except ValueError:
            print("Please enter a valid number")

def char_create():
    clear_screen()
    attributes = [0, 0, 0, 0, 0, 0]
    level = get_level()
    print(f"You're level {level}")
    input("[Press ENTER to continue...]")
    clear_screen()

    print("\nRolling attributes...\n")
    time.sleep(.5)
    for i in range(0, 6):
        # print(attr_names[i], end=": ")
        val = roll(3, 6)
        attributes[i] = val
    print_attr(attributes)
    input("[Press ENTER to continue...]")
    clear_screen()

    print("\n\n")
    print_attr(attributes)
    crace = get_race()
    print(crace.value)
    input("[Press ENTER to continue...]")
    clear_screen()

    print(crace.value)
    print("\n")
    print_attr(attributes)
    cclass = get_class(crace)
    print(cclass.value)
    input("[Press ENTER to continue...]")
    clear_screen()

    print(crace.value, end=" ")
    print(cclass.value)
    print("\n")
    print_attr(attributes)
    name: str = input("Choose a name: ")
    print("Your name is", name)
    clear_screen()

    print(name)
    print(crace.value, end=" ")
    print(cclass.value, '\n')
    print_attr(attributes)
    character = Character(name, level, crace, cclass, attributes)

    return character


if __name__ == '__main__':
    char = char_create()
    print(char.attributes)
