# task_4


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина находится в движении')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'{self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Вы превысили допустимую скорость в 60 км/ч! Ваша скорость: {self.speed} км/ч! Пожалуйста, сбавьте скорость!')
        else:
            print(f'Текущая скорость: {self.speed} км/ч')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Вы превысили допустимую скорость в 40 км/ч! Ваша скорость: {self.speed} км/ч! Пожалуйста, сбавьте скорость!')
        else:
            print(f'Текущая скорость: {self.speed}')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(0, 'белый', 'KIA')
print(town_car.color, town_car.name)
town_car.show_speed()
town_car.go()
town_car.speed = 60
town_car.show_speed()
town_car.turn('налево')
town_car.speed = 70
town_car.show_speed()
town_car.stop()

sport_car = SportCar(80, 'черный', 'Mercedes')
print(sport_car.color, sport_car.name, sport_car.is_police)
sport_car.go()
sport_car.show_speed()
sport_car.turn('направо')
sport_car.speed = 40
sport_car.show_speed()
sport_car.stop()

work_car = WorkCar(0, 'жёлтый', 'Renault')
print(work_car.color, work_car.name, work_car.speed)
work_car.go()
work_car.speed = 39
work_car.show_speed()
work_car.speed = 50
work_car.show_speed()
work_car.speed = 10
work_car.stop()

police_car = PoliceCar(100, 'синий', 'Ford', True)
print(police_car.name, police_car.color, police_car.is_police)
police_car.show_speed()
