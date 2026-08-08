import random
from enum import Enum

attrIndex = [
    'Str',
    'Dex',
    'Con',
    'Int',
    'Wis',
    'Cha'
]

class CharRace(Enum):
    DROW = 'Drow'
    DUERGAR = 'Duergar'
    ELF = 'Elf'
    GNOME = 'Gnome'
    HALFLING = 'Halfling'
    HALFELF = 'Half Elf'
    HALFORC = 'Half Orc'
    DWARF = 'Dwarf'
    SVIRFNEBLIN = 'Svirfneblin'
    HUMAN = 'Human'

class CharClass(Enum):
    ACROBAT = 'Acrobat'
    ASSASSIN = 'Assassin'
    BARBARIAN = 'Barbarian'
    BARD = 'Bard'
    KNIGHT = 'Knight'
    CLERIC = 'Cleric'
    DRUID = 'Druid'
    WARRIOR = 'Warrior'
    ILLUSIONIST = 'Illusionist'
    ROGUE = 'Rogue'
    MAGICUSER = 'Magic User'
    PALADIN = 'Paladin'
    RANGER = 'Ranger'

CLASS_XP = {
    CharClass.ACROBAT: {
        0, 1200, 2400, 4800, 9600, 20000, 40000, 80000,
        160000, 280000, 400000, 520000, 640000, 760000
    },
    CharClass.ASSASSIN: {
        0, 1500, 3000, 6000, 12000, 25000, 50000, 100000,
        200000, 300000, 425000, 550000, 675000, 800000
    },
    CharClass.BARBARIAN: {
        0, 2500, 5000, 10000, 18500, 37000, 85000, 140000,
        270000, 400000, 530000, 660000, 790000, 920000
    },
    CharClass.BARD: {
        0, 2000, 4000, 8000, 16000, 32000, 64000, 120000,
        240000, 360000, 480000, 600000, 720000, 840000
    },
    CharClass.KNIGHT: {
        0, 2500, 5000, 10000, 18500, 37000, 85000, 140000,
        270000, 400000, 530000, 660000, 790000, 920000
    },
    CharClass.CLERIC: {
        0, 1500, 3000, 6000, 12000, 25000, 50000, 100000,
        200000, 300000, 400000, 500000, 600000, 700000
    },
    CharClass.DRUID: {
        0, 2000, 4000, 7500, 12500, 20000, 35000, 60000,
        90000, 125000, 200000, 300000, 750000, 1500000
    },
    CharClass.WARRIOR: {
        0, 2000, 4000, 8000, 16000, 32000, 64000, 120000,
        240000, 360000, 480000, 600000, 720000, 840000
    },
    CharClass.ILLUSIONIST: {
        0, 2500, 5000, 10000, 20000, 40000, 80000, 150000,
        300000, 450000, 600000, 750000, 900000, 1050000
    },
    CharClass.ROGUE: {
        0, 1200, 2400, 4800, 9600, 20000, 40000, 80000,
        160000, 280000, 400000, 520000, 640000, 760000
    },
    CharClass.MAGICUSER: {
        0, 2500, 5000, 10000, 20000, 40000, 80000, 150000,
        300000, 450000, 600000, 750000, 900000, 1050000
    },
    CharClass.PALADIN: {
        0, 2750, 5500, 12000, 24000, 45000, 95000, 175000,
        350000, 500000, 650000, 800000, 950000, 1100000
    },
    CharClass.RANGER: {
        0, 2250, 4500, 10000, 20000, 40000, 90000, 150000,
        300000, 425000, 550000, 675000, 800000, 925000
    }
}

RACE_CLASS_LIMITS = {
    CharRace.DROW : {
        CharClass.ACROBAT: 10,
        CharClass.ASSASSIN: 10,
        CharClass.BARBARIAN: 0,
        CharClass.BARD: 0,
        CharClass.KNIGHT: 9,
        CharClass.CLERIC: 11,
        CharClass.DRUID: 0,
        CharClass.WARRIOR: 7,
        CharClass.ILLUSIONIST: 0,
        CharClass.ROGUE: 11,
        CharClass.MAGICUSER: 9,
        CharClass.PALADIN: 0,
        CharClass.RANGER: 9
    },
    CharRace.DUERGAR : {
        CharClass.ACROBAT : 0,
        CharClass.ASSASSIN : 9,
        CharClass.BARBARIAN : 0,
        CharClass.BARD : 0,
        CharClass.KNIGHT : 0,
        CharClass.CLERIC : 8,
        CharClass.DRUID : 0,
        CharClass.WARRIOR : 9,
        CharClass.ILLUSIONIST : 0,
        CharClass.ROGUE : 9,
        CharClass.MAGICUSER : 0,
        CharClass.PALADIN : 0,
        CharClass.RANGER : 0
    },
    CharRace.ELF : {
        CharClass.ACROBAT : 10,
        CharClass.ASSASSIN : 10,
        CharClass.BARBARIAN : 0,
        CharClass.BARD : 0,
        CharClass.KNIGHT : 11,
        CharClass.CLERIC : 7,
        CharClass.DRUID : 8,
        CharClass.WARRIOR : 7,
        CharClass.ILLUSIONIST : 0,
        CharClass.ROGUE : 10,
        CharClass.MAGICUSER : 11,
        CharClass.PALADIN : 0,
        CharClass.RANGER : 11
    },
    CharRace.GNOME : {
        CharClass.ACROBAT : 6,
        CharClass.ASSASSIN : 0,
        CharClass.BARBARIAN : 0,
        CharClass.BARD : 0,
        CharClass.KNIGHT : 0,
        CharClass.CLERIC : 7,
        CharClass.DRUID : 0,
        CharClass.WARRIOR : 6,
        CharClass.ILLUSIONIST : 7,
        CharClass.ROGUE : 8,
        CharClass.MAGICUSER : 0,
        CharClass.PALADIN : 0,
        CharClass.RANGER : 0
    },
    CharRace.HALFLING : {
        CharClass.ACROBAT : 0,
        CharClass.ASSASSIN : 0,
        CharClass.BARBARIAN : 0,
        CharClass.BARD : 0,
        CharClass.KNIGHT : 0,
        CharClass.CLERIC : 0,
        CharClass.DRUID : 6,
        CharClass.WARRIOR : 6,
        CharClass.ILLUSIONIST : 0,
        CharClass.ROGUE : 8,
        CharClass.MAGICUSER : 0,
        CharClass.PALADIN : 0,
        CharClass.RANGER : 0
    },
    CharRace.HALFELF : {
        CharClass.ACROBAT : 12,
        CharClass.ASSASSIN : 11,
        CharClass.BARBARIAN : 0,
        CharClass.BARD : 12,
        CharClass.KNIGHT : 12,
        CharClass.CLERIC : 5,
        CharClass.DRUID : 12,
        CharClass.WARRIOR : 8,
        CharClass.ILLUSIONIST : 0,
        CharClass.ROGUE : 12,
        CharClass.MAGICUSER : 8,
        CharClass.PALADIN : 12,
        CharClass.RANGER : 8
    },
    CharRace.HALFORC : {
        CharClass.ACROBAT : 8,
        CharClass.ASSASSIN : 8,
        CharClass.BARBARIAN : 0,
        CharClass.BARD : 0,
        CharClass.KNIGHT : 0,
        CharClass.CLERIC : 4,
        CharClass.DRUID : 0,
        CharClass.WARRIOR : 10,
        CharClass.ILLUSIONIST : 0,
        CharClass.ROGUE : 8,
        CharClass.MAGICUSER : 0,
        CharClass.PALADIN : 0,
        CharClass.RANGER : 0
    },
    CharRace.DWARF : {
        CharClass.ACROBAT : 0,
        CharClass.ASSASSIN : 9,
        CharClass.BARBARIAN : 0,
        CharClass.BARD : 0,
        CharClass.KNIGHT : 0,
        CharClass.CLERIC : 8,
        CharClass.DRUID : 0,
        CharClass.WARRIOR : 10,
        CharClass.ILLUSIONIST : 0,
        CharClass.ROGUE : 9,
        CharClass.MAGICUSER : 0,
        CharClass.PALADIN : 0,
        CharClass.RANGER : 0
    },
    CharRace.SVIRFNEBLIN : {
        CharClass.ACROBAT : 0,
        CharClass.ASSASSIN : 8,
        CharClass.BARBARIAN : 0,
        CharClass.BARD : 0,
        CharClass.KNIGHT : 0,
        CharClass.CLERIC : 7,
        CharClass.DRUID : 0,
        CharClass.WARRIOR : 6,
        CharClass.ILLUSIONIST : 7,
        CharClass.ROGUE : 8,
        CharClass.MAGICUSER : 0,
        CharClass.PALADIN : 0,
        CharClass.RANGER : 0
    },
    CharRace.HUMAN : {
        CharClass.ACROBAT : None,
        CharClass.ASSASSIN : None,
        CharClass.BARBARIAN : None,
        CharClass.BARD : None,
        CharClass.KNIGHT : None,
        CharClass.CLERIC : None,
        CharClass.DRUID : None,
        CharClass.WARRIOR : None,
        CharClass.ILLUSIONIST : None,
        CharClass.ROGUE : None,
        CharClass.MAGICUSER : None,
        CharClass.PALADIN : None,
        CharClass.RANGER : None
    }
}

class Character:

    def __init__(self, name: str, level: int,
                 charclass: CharClass, charrace: CharRace, attr):
        self._name = name
        self._level = level
        self._cclass = charclass
        self._race = charrace
        # self.STR = 0
        # self.DEX = 0
        # self.CON = 0
        # self.INT = 0
        # self.WIS = 0
        # self.CHA = 0
        self.attributes = attr

    @classmethod
    def empty(self):
        self._name = ""
        self._level = 0
        self._cclass = ""
        self._race = ""
        self.STR = 0
        self.DEX = 0
        self.CON = 0
        self.INT = 0
        self.WIS = 0
        self.CHA = 0
        self.attributes = [
            self.STR,
            self.DEX,
            self.CON,
            self.INT,
            self.WIS,
            self.CHA
        ]

    class CharAttr(Enum):
        FOR = 0,
        DEX = 0,
        CON = 0,
        INT = 0,
        WIS = 0,
        CHA = 0


def roll(number: int, dice: int):
    result = 0
    print(f"Rolling {number}d{dice}", end=": ")
    for d in range(1,number+1):
        r = random.randint(1, dice)
        if d != number:
            end='+'
        else:
            end='\n'
        print(r, end=end)
        result += r

    return result

if __name__ == '__main__':
    tizio = Character('Tizio', 1, CharRace.ELF, CharClass.ROGUE)
    print(f"{'Name':<15}{tizio._name:}")
    print(f"{'Lvl':<15}{str(tizio._level):}")
    print(f"{'Class':<15}{tizio._cclass.value:}")
    print(f"{'Race':<15}{tizio._race.value:}")
    tizio.create()
