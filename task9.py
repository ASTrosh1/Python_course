import threading
import time

class Countdown(threading.Thread):
    def __init__(self, interval):
        super().__init__()
        self.daemon= True
        self.interval = interval

    def run(self):
        for i in range(10, 0, -1):
            print(f"{self.getName()}, {i}")
            time.sleep(self.interval)

t1 = Countdown(1)
t2 = Countdown(1)
t1.start()
t2.start()
t1.join()
