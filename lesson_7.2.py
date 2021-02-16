# task_2
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, clothes):
        self.clothes = clothes

    @abstractmethod
    def abstract(self):
        pass

    @property
    def cl(self):
        return f'Необходимо ткани для пошива костюма и пальто: {self.clothes / 6.5 + 0.5 + 2 * self.clothes + 0.3}'


class Coat(Clothes):
    def ct(self):
        return f'Нужно ткани для пошива пальто: {self.clothes / 6.5 + 0.5}'

    def abstract(self):
        pass


class Suit(Clothes):
    def st(self):
        return f'Нужно ткани для пошива костюма: {2 * self.clothes + 0.3}'

    def abstract(self):
        pass


coat = Coat(55)
suit = Suit(180)
print(coat.ct())
print(suit.st())
