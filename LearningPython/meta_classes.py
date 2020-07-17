from abc import *


class SchoolMember(metaclass=ABCMeta):
    '''Представляет любого человека в школе.'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0})'.format(self.name))
