
b= 300   # G
def f():
    b = 200 # E
    def g():
        # b = 100 #L
        print(b)
        print(__name__) # B
    g()

f()

if __name__ == '__main__':
    f()