import threading
from threading import Thread
import time
'''
Python 3.X threading 模块演示 Demo

threading 的 Thread 类基本使用方式（继承重写 run 方法及直接传递方法）
'''
class NormalThread(Thread):

    def __init__(self, name):
        super().__init__(name)
        self.count = 0

    def run(self):
        print(self.getName() + ' thread is start')
        self.do_customer_things()
        print(self.getName() + ' thread is end')

    def do_customer_things(self):
        while self.count < 10:
            time.sleep(1)
            print('do customer things counter is:' + str(self.count))
            self.count += 1




