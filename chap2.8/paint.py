from point import Point


def main():
    bound_class_method()

def bound_class_method():
    p = Point()
    p.set_x(10)
    p.set_y(10)
    print(p.get_x(), p.get_y(), sep=',')

def test_other_method():
    print(Point.static_method())
    print(Point.class_method())

if __name__ == '__main__':
    main()
    test_other_method()


def test_member():
    p = Point()
    p.set_y(10)
    p.set_x(10)
    print(f'{p.x},{p.y}, {p.count_of_instance}')

