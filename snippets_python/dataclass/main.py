from snippets_python.dataclass.model import (
    C,
    Derived,
    ImmutablePoint,
    Point,
    Rectangle,
)

if __name__ == "__main__":
    p = Point(1, 2)
    r = Rectangle(10, 20)
    ip = ImmutablePoint(3, 4)
    c = C(5, 6, 7)
    d = Derived(8, 9, 10)

    print(p)
    print(r)
    print(ip)
    print(c)
    print(d)
