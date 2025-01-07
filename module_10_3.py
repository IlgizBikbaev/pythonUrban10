from random import randint
from time import sleep
import threading
lock = threading.Lock()

class Bank:
    def __init__(self, balance, lock):
        self.balance = int(balance)
        self.lock = lock

    def deposit(self):
        for i in range(100):
            replenishment = randint(50, 500)
            self.balance += replenishment
            print(f'Пополнение: {replenishment}. Баланс: {self.balance}')
            sleep(0.001)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()



    def take(self):
        for i in range(0, 100):
            withdrawal = randint(50, 500)
            print(f'Запрос на {withdrawal}')
            if withdrawal <= self.balance:
                self.balance -= withdrawal
                print(f'Снятие: {withdrawal}. Баланс: {self.balance}')
                sleep(0.001)
            if withdrawal > self.balance:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            

bk = Bank(0, lock)
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')