import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)

    def run(self):
        print(f'{self.name}, на нас напали!')
        count_days = 0
        enemies = 100
        while enemies > 0:
            time.sleep(1)
            count_days +=1
            enemies = enemies -  self.power
            if enemies < 0:
                enemies = 0
            print(f'{self.name} сражается {count_days}-й день, осталось {enemies} воинов.')
        print(f'{self.name} одержал победу на {count_days}-й день!')







first_knight = Knight('Sir Lancelot', 10)
first_knight.start()

second_knight = Knight("Sir Galahad", 20)
second_knight.start()

first_knight.join()
second_knight.join()
print(f'игра закончена!')
