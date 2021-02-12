# task_5
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')


stationery = Stationery(None)
stationery.draw()
pen = Pen('ручкой')
pen.draw()
pencil = Pencil('карандашем')
pencil.draw()
handle = Handle('маркером')
handle.draw()
