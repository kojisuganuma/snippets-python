from dataclasses import dataclass, field


# 基本的なデータクラス
@dataclass
class Point:
    x: int
    y: int


# デフォルト値を持つデータクラス
@dataclass
class Rectangle:
    width: int
    height: int
    color: str = "white"


# 不変のデータクラス
@dataclass(frozen=True)
class ImmutablePoint:
    x: int
    y: int


# field()関数を使用したデータクラス
@dataclass
class C:
    x: int
    y: int = field(repr=False)
    z: int = field(default=10, compare=False)


# 継承を使用したデータクラス
@dataclass
class Base:
    x: int
    y: int = 5


@dataclass
class Derived(Base):
    z: int = 0  # デフォルト値を設定
