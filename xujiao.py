import time

def sf(f):
    def cf():
        st = time.time()
        f()
        sst = time.time()
        print("%f" % (sst-st))
    return cf
@sf
def test():
    print("sss")

test()
