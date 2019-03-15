import _thread
import time

'''
Python 3.X _thread 模块演示 Demo
当注释掉 self.lock.acquire() 和 self.lock.release() 后运行代码会发现最后的 count 为 467195 等，并发问题。
当保留 self.lock.acquire() 和 self.lock.release() 后运行代码会发现最后的 count 为 1000000，锁机制保证了并发。
time.sleep(5) 就是为了解决 _thread 模块的诟病，注释掉的话子线程没机会执行了
所谓得诟病:就是在主进程里面需要预估子进程结束得时间,让主进程再该时间点之后结束,否则主进程会提前结束,无法执行子进程
'''
class ThreadTest(object):

    def __init__(self):
        self.count = 0
        self.lock = None

    def runnable(self):
        self.lock.acquire()
        print('thread lock acquare id is ' + str(_thread.get_ident()))
        for i in range(0,100000):
            self.count += 1
        print('thread lock release id is ' + str(_thread.get_ident()))
        self.lock.release()

    def test(self):
        self.lock = _thread.allocate_lock()
        for i in range(0,10):
            _thread.start_new_thread(self.runnable, ())


if __name__ == '__main__':
    test = ThreadTest()
    print('ThreadTest is runing...')
    test.test()
    time.sleep(5)
    print('ThreadTest end count is ' + str(test.count))



