import threading


def foo1():
    for i in range(100):
        print("1")


def foo2():
    for i in range(100):
        print("2")

thr1 = threading.Thread(target=foo1)
thr2 = threading.Thread(target=foo2)

thr1.start()
thr2.start()





