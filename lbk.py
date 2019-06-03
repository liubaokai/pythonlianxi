import time

def xujiao(a):
    def lbk():
        start = time.time()
        a()
        end = time.time()
        print(end-start)
    return lbk

@xujiao
def xu():
    for i in range(1000000):
        print(i)

xu()