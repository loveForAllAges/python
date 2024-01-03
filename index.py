

class MyClass:
    """Custom class"""
    i = 1000

    def __init__(self, a, b, s) -> None:
        """Вызывается с после создания экземпляра с помощью __new__()."""
        self.a = a
        self.b = b
        self.s = s
        self.length = len(s)

    def __iter__(self):
        """Возвращает обьект с помощью __next__()."""
        return self
    
    def __next__(self):
        """Обращается к элементам в контейнере по одному."""
        if not self.length:
            raise StopIteration
        self.length -= 1
        return self.s[self.length]

    def foo(self):
        return 1+2


def foo(i):
    """
    Foo desc

    >>> print(foo(2))
    4
    """
    return i*i


import unittest
class TestFoo(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(foo(2), 4)
unittest.main()