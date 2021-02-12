# task_3
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": float(wage), "bonus": float(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def full_name(self):
        return f'{self.name} {self.surname}'

    def total_income(self):
        return self._income["wage"] + self._income["bonus"]


p = Position('Иван', 'Кожедуб', 'Лётчик', '100000', '30000')
print(f'Работник: {p.full_name()} Зарплата: {p.total_income()}')
