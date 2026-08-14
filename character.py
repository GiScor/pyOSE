# from enum import Enum
# from tools import roll
from classesraces import CharRace, CharClass
from checks import classRestriction
from tools import roll

attrIndex = [
    'Str',
    'Dex',
    'Con',
    'Int',
    'Wis',
    'Cha'
]

class Character:

    def __init__(self, name="", level=1,
                 charclass=None,
                 charrace=None):
        self._name = name
        self._level = level
        self._class = charclass
        self._race = self.set_race(charrace)
        self.attributes = {
            'STR': 0, 'DEX': 0, 'CON': 0,
            'INT': 0, 'WIS': 0, 'CHA': 0
        }

    def set_name(self, name):
        self._name = name

    def set_level(self, level: int):
        self._level = level

    def set_race(self, charrace: CharRace):
        self._race = charrace

    def set_class(self, charclass: CharClass):
        try:
            classRestriction(self._race, charclass)
            self._class = charclass
        except ValueError:
            self._class = None

    def set_attr(self, attributes: list):
        for i, name in enumerate(self.attributes):
            self.attributes[name] = attributes[i]

    def gen_attr(self):
        for i, name in enumerate(self.attributes):
            self.attributes[name] = roll(3, 6)

    @property
    def STR(self):
        return self.attributes['STR']
    @STR.setter
    def STR(self, value):
        if value < 1:
            raise ValueError("Attributes must be at least 1")
        self.attributes['STR'] = value

    @property
    def DEX(self):
        return self.attributes['DEX']
    @DEX.setter
    def DEX(self, value):
        if value < 1:
            raise ValueError("Attributes must be at least 1")
        self.attributes['DEX'] = value

    @property
    def CON(self):
        return self.attributes['CON']
    @CON.setter
    def CON(self, value):
        if value < 1:
            raise ValueError("Attributes must be at least 1")
        self.attributes['CON'] = value

    @property
    def INT(self):
        return self.attributes['INT']
    @INT.setter
    def INT(self, value):
        if value < 1:
            raise ValueError("Attributes must be at least 1")
        self.attributes['INT'] = value

    @property
    def WIS(self):
        return self.attributes['WIS']
    @WIS.setter
    def WIS(self, value):
        if value < 1:
            raise ValueError("Attributes must be at least 1")
        self.attributes['WIS'] = value

    @property
    def CHA(self):
        return self.attributes['CHA']
    @CHA.setter
    def CHA(self, value):
        if value < 1:
            raise ValueError("Attributes must be at least 1")
        self.attributes['CHA'] = value


if __name__ == '__main__':
    tizio = Character()
    tizio.set_name("Tizio")
    print(tizio._name)
    tizio.set_race(CharRace.DWARF)
    print(tizio._race)
    tizio.set_class(CharClass.BARD)
    print(tizio._class)
    tizio.set_class(CharClass.WARRIOR)
    print(tizio._class)
    tizio.set_attr([10, 9, 8, 7, 6, 5])
    print(tizio.attributes)
    tizio.CHA = 1
    print(tizio.attributes)
    tizio.gen_attr()
    print(tizio.attributes)
