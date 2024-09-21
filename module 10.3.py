from threading import Thread, Lock
from time import sleep
import random

class Bank(Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()



    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            ran = random.randint(50, 500)
            self.balance += ran
            print(f'Пополнение: {ran}. Баланс: {self.balance}')
            sleep(0.001)


    def take(self):
        ran = random.randint(50, 500)
        for i in range(100):
            print(f'Запрос на {ran}')
            if ran <= self.balance:
                self.balance -= ran
                print(f'Снятие: {ran}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()

bk = Bank()


th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')