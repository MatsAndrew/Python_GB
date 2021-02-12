# task_1
import time


class TrafficLight:
    __color = ['Красный', 'Жёлтый', 'Зелёный']

    def running(self):
        el = 0
        while el != 3:
            print(TrafficLight.__color[el])
            if el == 0:
                time.sleep(7)
            elif el == 1:
                time.sleep(2)
            elif el == 2:
                time.sleep(1)
            el += 1


tl = TrafficLight()
tl.running()
