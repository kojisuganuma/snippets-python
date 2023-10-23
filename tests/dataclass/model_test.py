from dataclasses import FrozenInstanceError

import pytest
from snippets_python.dataclass.model import (
    Point,
    Rectangle,
    ImmutablePoint,
    C,
    Derived,
)


def test_point():
    p = Point(1, 2)
    assert p.x == 1
    assert p.y == 2


def test_rectangle():
    r = Rectangle(10, 20)
    assert r.width == 10
    assert r.height == 20
    assert r.color == "white"


def test_immutable_point():
    ip = ImmutablePoint(3, 4)
    assert ip.x == 3
    assert ip.y == 4
    with pytest.raises(FrozenInstanceError):
        ip.x = 5


def test_c():
    c = C(5, 6, 7)
    assert c.x == 5
    assert c.y == 6
    assert c.z == 7


def test_derived():
    d = Derived(8, 9, 10)
    assert d.x == 8
    assert d.y == 9
    assert d.z == 10
