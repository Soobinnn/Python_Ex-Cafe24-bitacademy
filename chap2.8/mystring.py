class MyString:

    def __init__(self,s):
        self.s = s

    def __truediv__(self, other):
        return self.s.split(other)

    # def __sub__(self):

s = MyString('Python Programmer is Good')
t = s / ' '
print(type(t))
print(t)
print(s / ' ')
# print(s + ' Job')
# print(MyString('Python ')*3)
# print(MyString('Hello ')*3)