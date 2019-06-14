g_a = 1
g_b = 'symbol'

# print(globals())

def f():
    l_a = 2
    l_b = '둘리'
    # print(globals())
    f()

    # 1. 정의된 함수
    f.k = 'hello'

