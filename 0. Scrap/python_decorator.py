import time

def timing(func):
    def wrapper():
        t1 = time.time()
        func()
        t = time.time() - t1
        print(t)
    return wrapper

@timing
def tick():
    time.sleep(.4)
    return

@timing
def tock():
    time.sleep(1.3)
    return


tick()
tock()