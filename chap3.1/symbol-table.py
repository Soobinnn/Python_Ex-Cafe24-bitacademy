# 심볼 테이블 내용 확인
g_a = 1
g_b = 'symbol'

# print(globals())

def f():
    l_a = 2
    l_b = '둘리'
    print(locals())

for i in range(10):
    g_c = 3
    g_d = 'python'
    print(locals())


# print(globals())
f()
print(globals())

# 객체의 심볼테이블을 접근하기 위해서는 __dict__ 속성의 내용을 확인한다
print(f.__dict__)

class MyClass:
    x = 10
    y = 20

print(MyClass.__dict__)

