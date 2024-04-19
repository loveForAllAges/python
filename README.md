# Python Cheatsheet
Version: 3.12.3

## Contents



## Operators
- **`**`**: Оператор возведения в степень;
- **`%`**: Остаток от деления;
- **`//`**: Оператор целочисленного деления;
- **`/`**: Оператор деления;
- **`*`**: Оператор умножения;
- **`-`**: Оператор вычитания;
- **`+`**: Оператор сложения;
- **`=`**: Оператор присваивания;
- **`:=`**: Оператор присваивания и возвращения значения переменной;
- **`==`**: Оператор сравнения равенства;
- **`!=`**: Оператор сравнения неравенства;
- **`<`**: Оператор меньше, чем;
- **`>`**: Оператор больше, чем;
- **`<=`**: Оператор меньше или равно;
- **`>=`**: Оператор больше или равно;
- **`<<`**: Побитовый сдвиг влево;
- **`>>`**: Побитовый сдвиг вправо;
- **`&`**: Побитовое и;
- **`^`**: Побитовое исключающее или;
- **`|`**: Побитовое или;
- **`~`**: Побитовое не;
- **`not`**: Булевый оператор не;
- **`and`**: Булевый оператор и;
- **`is`**: Проверка ID объектов;
- **`in`**: Наличие объекта в последовательности;
- **`or`**: Булевый оператор или;
- **`if`**: Оператор если;
- **`else`**: Оператор выполняется, если условие `if` и `elif` неверно;
- **`elif`**: Оператор выполняется, если условие `if` неверно;
- **`... if ... else ...`**: Тернарный условный оператор;
- **`switch-case`**: Оператор Switch-Case. [Подробнее](src/operators.md#switch-case);
- **`while`**: Оператор повторного выполнения;
- **`break`**: Оператор выхода из цикла `while`;
- **`continue`**: Оператор возвращения к началу цикла;
- **`lambda`**: Анонимная функция. [Подробнее](src/operators.md#lambda);
- **`for`**: Оператор перебора итерируемых объектов. [Подробнее](src/operators.md#for)


## Built-in functions
- __`abs`__: Возвращает абсолютное значение числа. [_Подробнее_](src/built_in_functions.md/#abs)
- __`aiter`__: Возвращает асинхронный итератор для асинхронной итерации. [_Подробнее_](src/built_in_functions.md/#aiter)
- __`all`__: Имеют ли все элементы итерируемого объекта значение True. [_Подробнее_](src/built_in_functions.md/#all)
- __`anext`__: Возвращает следующий элемент из асинхронного итератора. [_Подробнее_](src/built_in_functions.md/#anext)
- __`any`__: Имеет ли какой-либо элемент итерируемого объекта значение True. [_Подробнее_](src/built_in_functions.md/#any)
- __`ascii`__: Возвращает строку с печатным представлением объекта. [_Подробнее_](src/built_in_functions.md/#ascii)
- __`bin`__: Преобразует целое число в двоичную строку. [_Подробнее_](src/built_in_functions.md/#bin)
- __`bool`__: Возвращает логическое значение. [_Подробнее_](src/built_in_functions.md/#bool)
- __`breakpoint`__: Помещает в отладчик на месте вызова. [_Подробнее_](src/built_in_functions.md/#breakpoint)
- __`bytearray`__: Возвращает изменяемый массив байт. [_Подробнее_](src/built_in_functions.md/#bytearray)
- __`bytes`__: Возвращает неименяемый массив байт. [_Подробнее_](src/built_in_functions.md/#bytes)
- __`callable`__: Является ли объект вызываемым. [_Подробнее_](src/built_in_functions.md/#callable)
- __`chr`__: Возвращает символ по коду Юникода. [_Подробнее_](src/built_in_functions.md/#chr)
- __`classmethod`__: Преоразует метод в метод класса. [_Подробнее_](src/built_in_functions.md/#classmethod)
- __`compile`__: Компилирует строку в код, готовый к выполнению. [_Подробнее_](src/built_in_functions.md/#compile)
- __`complex`__: Возвращает комплексное число. [_Подробнее_](src/built_in_functions.md/#complex)
- __`delattr`__: Удаляет именованный атрибут объекта. [_Подробнее_](src/built_in_functions.md/#delattr)
- __`dict`__: Возвращает словарь. [_Подробнее_](src/built_in_functions.md/#dict)
- __`dir`__: Список имен в пространстве имен или атрибуты объекта. [_Подробнее_](src/built_in_functions.md/#dir)
- __`divmod`__: Возвращает частное и остаток введенных чисел. [_Подробнее_](src/built_in_functions.md/#divmod)
- __`enumerate`__: Возвращает перечисляемый объект. [_Подробнее_](src/built_in_functions.md/#enumerate)
- __`eval`__: Вычисляет и выполняет введенное выражение. [_Подробнее_](src/built_in_functions.md/#eval)
- __`exec`__: Выполняет Python код, полученный из строки. [_Подробнее_](src/built_in_functions.md/#exec)
- **`filter`**: Фильтрует итерируемый объект заданной функцией. [_Подробнее_](src/built_in_functions.md/#filter)
- __`float`__: Возвращает число с плавающей запятой. [_Подробнее_](src/built_in_functions.md/#float)
- __`format`__: Форматирует строку. [_Подробнее_](src/built_in_functions.md/#format)
- __`frozenset`__: Возвращает frozenset. [_Подробнее_](src/built_in_functions.md/#frozenset)
- __`getattr`__: Возвращает значение именованного атрибута объекта. [_Подробнее_](src/built_in_functions.md/#getattr)
- __`globals`__: Возвращает словарь глобальных переменных. [_Подробнее_](src/built_in_functions.md/#globals)
- __`hasattr`__: Существует ли атрибут у объекта. [_Подробнее_](src/built_in_functions.md/#hasattr)
- __`hash`__: Возвращает хеш объекта. [_Подробнее_](src/built_in_functions.md/#hash)
- __`help`__: Вызов встроенной справочной системы. [_Подробнее_](src/built_in_functions.md/#help)
- __`hex`__: Преобразует целое число в шестнадцатеричную строку. [_Подробнее_](src/built_in_functions.md/#hex)
- __`id`__: ID объекта. [_Подробнее_](src/built_in_functions.md/#id)
- __`input`__: Принимает входные данные. [_Подробнее_](src/built_in_functions.md/#input)
- __`int`__: Возвращает целочисленный объект. [_Подробнее_](src/built_in_functions.md/#int)
- __`isinstance`__: Является ли объект экземпляром другого объекта. [_Подробнее_](src/built_in_functions.md/#isinstance)
- __`issubclass`__: Является ли класс является подклассом другого класса. [_Подробнее_](src/built_in_functions.md/#issubclass)
- __`iter`__: Возвращает объект итератора. [_Подробнее_](src/built_in_functions.md/#iter)
- __`len`__: Возвращает длину объекта. [_Подробнее_](src/built_in_functions.md/#len)
- __`list`__: Возвращает объект список. [_Подробнее_](src/built_in_functions.md/#list)
- __`locals`__: Возвращает словарь локальных переменных. [_Подробнее_](src/built_in_functions.md/#locals)
- __`map`__: Возвращает итератор, который применяет функцию к каждому итерируемомуsrc/built_in_functions.md/ объекту. [_Подробнее_](#map)
- __`max`__: Возвращает наибольший элемент. [_Подробнее_](src/built_in_functions.md/#max)
- __`memoryview`__: Возвращает объект memoryview. [_Подробнее_](src/built_in_functions.md/#memoryview)
- __`min`__: Возвращает наименьший элемент. [*Подробнее*](src/built_in_functions.md/#min)
- __`next`__: Получает следующий элемент итератора. [_Подробнее_](src/built_in_functions.md/#next)
- __`object`__: Возвращает новый объект. [_Подробнее_](src/built_in_functions.md/#object)
- __`oct`__: Преобразует целое число в восьмеричную строку. [_Подробнее_](src/built_in_functions.md/#oct)
- __`open`__: Открывает файл и возвращает файловый объект. [_Подробнее_](src/built_in_functions.md/#open)
- __`ord`__: Возвращает код Юникода по символу. [_Подробнее_](src/built_in_functions.md/#ord)
- __`pow`__: Возводит число в степень. [_Подробнее_](src/built_in_functions.md/#pow)
- __`print`__: Выводит объекты. [_Подробнее_](src/built_in_functions.md/#print)
- __`property`__: Возвращает атрибут свойства. [_Подробнее_](src/built_in_functions.md/#property)
- __`range`__: Возвращает неизменяемый тип последовательности range. [_Подробнее_](src/built_in_functions.md/#range)
- __`repr`__: Возвращает строку с представлением объекта. [_Подробнее_](src/built_in_functions.md/#repr)
- __`reversed`__: Возвращает обратный итератор. [_Подробнее_](src/built_in_functions.md/#reversed)
- __`round`__: Округляет число. [_Подробнее_](src/built_in_functions.md/#round)
- __`set`__: Возвращает объект set. [_Подробнее_](src/built_in_functions.md/#set)
- __`setattr`__: Присваивает значение атрибуту. [_Подробнее_](src/built_in_functions.md/#setattr)
- __`slice`__: Возвращает часть объекта. [_Подробнее_](src/built_in_functions.md/#slice)
- __`sorted`__: Возвращает новый отсортированный список. [_Подробнее_](src/built_in_functions.md/#sorted)
- __`staticmethod`__: Преобразует метод в статический. [_Подробнее_](src/built_in_functions.md/#staticmethod)
- __`str`__: Возвращает объект str. [_Подробнее_](src/built_in_functions.md/#str)
- __`sum`__: Возвращает сумму элементов. [_Подробнее_](src/built_in_functions.md/#sum)
- __`super`__: Делегирует вызовы методов родительскому объекту. [_Подробнее_](src/built_in_functions.md/#super)
- __`tuple`__: Возвращает неизменяемый тип последовательности tuple. [_Подробнее_](src/built_in_functions.md/#tuple)
- __`type`__: Возвращает тип объекта. [_Подробнее_](src/built_in_functions.md/#type)
- __`vars`__: Возвращает object.\_\_dict__ иначе `locals`. [_Подробнее_](src/built_in_functions.md/#vars)
- __`zip`__: Возвращает итератор кортежей. [_Подробнее_](src/built_in_functions.md/#zip)
- __`import`__: Вызывается оператором импорта. [_Подробнее_](src/built_in_functions.md/#import)


## Types
- **`list`**: Изменяемая последовательность. [Подробнее](src/types.md#list)
- **`tuple`**: Неизменяемая последовательность. [Подробнее](src/types.md#tuple)
- **`dict`**: Изменяемая последовательность пар ключ-значение. [Подробнее](src/types.md#dict)
- **`set`**: Изменяемая неупорядоченная коллекция уникальных хешируемых объектов. [Подробнее](src/types.md#set)
- **`frozenset`**: Изменяемая неупорядоченная коллекция уникальных хешируемых объектов. [Подробнее](src/types.md#frozenset)
- **`bytes`**: Неизменяемая последовательность байт. [Подробнее](src/types.md#bytes)
- **`bytearray`**: Изменяемая последовательность байт. [Подробнее](src/types.md#bytearray)
- **`memoryview`**: Буфер памяти с данными. [Подробнее](src/types.md#memoryview)
- **`string`**: Неизменяемая последовательность. [Подробнее](src/types.md#string)
- **`int`**: целые числа. [Подробнее](src/types.md#int)
- **`float`**: Числа с плавающей точкой. [Подробнее](src/types.md#float)
- **`complex`**: Комплексные числа. [Подробнее](src/types.md#complex)
- **`bool`**: Логические значения. [Подробнее](src/types.md#bool)


## Operations on sequences
- **`x in s`**: Элемент x находится в s
- **`x not in s`**: Элемент x не находится в s
- **`s + t`**: Объединение s и t
- **`s * n`**: Добавление s к самому себе n раз
- **`s[i]`**: i-й элемент из s
- **`s[i:j]`**: последовательность от i до j из s
- **`s[i:j:k]`**: последовательность от i до j с шагом k из s
- **`len(s)`**: длина s
- **`min(s)`**: наименьший элемент из s
- **`max(s)`**: наибольший элемент из s
- **`s.index(x[, i[, j]])`**: индекс первого вхождения x в s (в или после индекса i и перед индексом j)
- **`s.count(x)`**: количество x в s


#### Operations on mutable sequences
- **`s[i] = x`**: Элемент i из s заменяется на x
- **`s[i:j] = t`**: Фрагмент s от i до j заменяется содержимым итерируемого t
- **`del s[i:j]`**: Аналогично `s[i:j] = []`
- **`s[i:j:k] = t`**: Элементы `s[i:j:k]` заменяются элементами t
- **`del s[i:j:k]`**: Удаляет элементы `s[i:j:k]`
- **`s.append(x)`**: Добавляет x в конец последовательности
- **`s.clear()`**: Удаляет все элементы из s
- **`s.copy()`**: Создает неглубокую копию s (как `s[:]`)
- **`s.extend(t)`**: Расширяет s содержимым t
- **`s *= n`**: Обновляет s, его содержимое повторяется n раз
- **`s.insert(i, x)`**: Вставляет x в s перед индексом i
- **`s.pop()`**: Извлекает элемент в i, а также удаляет его из s
- **`s.remove(x)`**: Удаляет первый элемент из s, где `s[i] = x`
- **`s.reverse()`**: Меняет местами элементы s на месте


## Function definition
```python
def f(*args): pass  # f(1, 2, 3)
def f(x, *args): pass  # f(1, 2, 3)
def f(*args, z): pass  # f(1, 2, z=3)
def f(**kwds): pass  # f(x=1, y=2, z=3)
def f(x, **kwds): pass  # f(x=1, y=2, z=3) | f(1, y=2, z=3)
def f(*args, **kwds): pass  # f(x=1, y=2, z=3) | f(1, y=2, z=3) | f(1, 2, z=3) | f(1, 2, 3)
def f(x, *args, **kwds): pass  # f(x=1, y=2, z=3) | f(1, y=2, z=3) | f(1, 2, z=3) | f(1, 2, 3)
def f(*args, y, **kwds): pass  # f(x=1, y=2, z=3) | f(1, y=2, z=3)
def f(*, x, y, z): pass  # f(x=1, y=2, z=3)
def f(x, *, y, z): pass  # f(x=1, y=2, z=3) | f(1, y=2, z=3)
def f(x, y, *, z): pass  # f(x=1, y=2, z=3) | f(1, y=2, z=3) | f(1, 2, z=3)
```
Формат документирования функций:
```python
def foo():
    """
    Краткое описание функции с точкой на конце.

    Если есть подробности, то они указываются через пустую строку.
    """
    return

print(foo.__doc__)
```


## Class instantiation
```python
class A:
      """Строка документации класса."""
      def __init__(self, a):
            """Строка документации метода."""
            self.a = a
      def __repr__(self):
            """Используется repr(c), а также str(c) если __str__ не обьявлен."""
            return f'{self.__class__.__name__}({self.a!r})'
      def __str__(self):
            """Используется str(c), например print(c)"""
            return str(self.a)
      @classmethod
      def get_class_name(cls): # Принимает класс, а не экземпляр
            return cls.__name__
      @staticmethod
      def static(): # Ничего не принимает
            return 1

a = A(1)  # Создание экземпляра

# Создание экземпляра класса под капотом
obj = cls.__new__(cls, *args, **kwds)
if isinstance(obj, cls):
      obj.__init__(*args, **kwds)
```
```python
class B:
      @property
      def f(self):
            if not hasattr(self, '_f'): return
            return self._f
      @f.setter
      def f(self, value):
            self._f = value
```


## Exceptions
Обработка исключений позволяет избежать принудительного закрытия программы. Чтобы вызвать исключение принудительно, используется `raise`.
```python
try:
      # Код, который будет выполняться, пока не всплывет исключение.
      pass
except ValueError:
      # Код, который выполнится, если всплывет исключение ValueError.
      # В блоке try-except может быть указано неограниченное количество except блоков для перехвата ошибок.
      pass
except Exception:
      # Код, который выполнится, если будет вызвано любое исключение.
      pass
finally:
      # Код, который выполнится в любом случае
      pass
```
Пользовательские исключения создаются посредством создания класса, наследующего класс Exception.
```python
class CustomException(Exception):
      pass

raise CustomException
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# __main__.CustomException
```


## Assert
`assert` - способ проверки утверждением.
```python
pod_bay_door_status = 'open'
assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'

pod_bay_door_status = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'
# Traceback (most recent call last):
#   File "<pyshell#10>", line 1, in <module>
#     assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'
# AssertionError: The pod bay doors need to be "open".
```


## Decorators
Декоратор - это функция, которая принимает другую функцию в качестве аргумента и возвращает оболочку.
```python
def your_decorator(func):
      def wrapper():
            func()
      return wrapper

@your_decorator
def foo():
      print("Hello World!")

foo()
# Before func!
# Hello World!
# After func!
```
Декоратор для функции с параметрами:
```python
def your_decorator(func):
      def wrapper(*args,**kwargs):
            func(*args,**kwargs)
      return wrapper

@your_decorator
def foo(bar):
      print("My name is " + bar)

foo("Jack")
# Before func!
# My name is Jack
# After func!
```
Шаблон для создания декоратора для функций с параметрами и без них, с возвращаемым значением или без:
```python
import functools

def your_decorator(func):
      @functools.wraps(func)
      def wrapper(*args,**kwargs):
            result = func(*args,**kwargs)
            return result
      return wrapper


# Задание параметров декоратора
def your_decorator(arg):
      def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kwargs):
                  result = func(*args,**kwargs)
                  return result
            return wrapper
      return decorator

@your_decorator(arg = 'x')
def foo(bar):
      return bar
```
Реализация декоратора на основе класса. Используется для сохранения состояния:
```python
class CountCallNumber:
      def __init__(self, func):
            self.func = func
            self.call_number = 0

      def __call__(self, *args, **kwargs):
            self.call_number += 1
            print("This is execution number " + str(self.call_number))
      return self.func(*args, **kwargs)

@CountCallNumber
def say_hi(name):
      print("Hi! My name is " + name)

say_hi("Jack")
# This is execution number 1
# Hi! My name is Jack

say_hi("James")
# This is execution number 2
# Hi! My name is James
```


## Generator
Функция-генератор - это функция или выражение, которое позволяет создавать итерируемые последовательности значений по мере их необходимости, вместо того, чтобы заранее создавать их все и хранить в памяти. Существует два основных типа генераторов: функциональные генераторы (с использованием ключевого слова yield) и генераторные выражения.
```python
def my_generator():
    yield 1
    yield 2

gen = my_generator()
print(next(gen)) # Вывод: 1


gen_expr = (x ** 2 for x in range(5))
print(list(gen_expr)) # Вывод: [0, 1, 4, 9, 16]
```
При каждом вызове next() генератор возобновляет работу с того места, где остановился (он запоминает все значения данных и то, какой оператор был выполнен последним). Методы __iter__ и __next__ создаются автоматически.
```python
def reverse(data):
    for i in range(len(data)-1, -1, -1):
        yield data[i]

for i in reverse('spam'):
    print(i)
```
Выражения-генераторы более компактны, но менее универсальны, чем полные определения генераторов, и более удобны для памяти, чем эквивалентные определения списков.
```python
sum(i*i for i in range(10))
```


## File objects
Режимы открытия файла: `r` - только для чтения, `w` - только для записи (очищает), `a` - для добавления, `r+` - для чтения и записи. Добавление `b` откроет в двоичном режиме. Рекомендуется использовать с конструкцией with, файл корректно закроется после завершения работы. Иначе необходимо вручную закрывать файл.
```python
f = open(filename, mode='r', encoding=None)
f.close()
# Или
with open('filepath', encoding="utf-8") as f:
    read_data = f.read()
```

Методы:
- **`read`**: Считывает некоторое количество данных и возвращает в виде строки или байтового обьекта.
- **`readline`**: Считывает одну строку из файла.
- **`readlines`**: Все строки файла в списке.
- **`write`**: Записывает строку в файл и возвращает кол-во записанных символов.
- **`tell`**: Возвращает целое число, указывающее текущую позицию файлового обьекта в файле, представленное как кол-во байтов от начала файла в двоичном режиме.
- **`seek`**: Изменение положения файлового обьекта.



## Iterator
Объект-итератор - обьект, представляющий поток данных. Итератор должен реализовать два метода: `__iter__()` - возвращает обьект итератора; `__next__()` - возвращает следующий элемент из итератора или `StopIteration`, если элементов нет.
```python
class SimpleIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration

my_iterator = SimpleIterator(1, 5)

for value in my_iterator:
    print(value)
```


## Annotations
Аннотации типов предназначены для предоставления информации о типах данных переменных, аргументов функций и возвращаемых значений. Аннотации типов являются необязательными и не влияют на фактическое выполнение кода во время выполнения программы. Основные встроенные типы аннотаций - `Generic Alias`, `Union`. `GenericAlias` чаще всего используется с классами-контейнерами (`list(int)`).
```python
def send_post_request(url: str, body: dict[str, int]) -> None: pass
```


## Context manager
Контекстный менеджер - объект, который реагирует, когда контекст начинается и заканчивается. Используется с `with`. Реализуется с помощью методов `__enter__()` и `__exit__()`, которые позволяют выполнить действия до выполнения кода и после. Например, файловые обьекты возвращают себя из `__enter__()`, чтобы их можно было открыть.
Кастомный контекстный менеджер:
```python
import contextlib
@contextlib.contextmanager
def context_manager(num):
      print('Enter')
      yield num + 1
      print('Exit')
with context_manager(2) as cm:
      print('Right in the middle with cm = {}'.format(cm))
# Enter
# Right in the middle with cm = 3
# Exit
```
Контекстный менеджер на основе класса:
```python
class ContextManager:
      def __enter__(self, *args, **kwargs):
            print("--enter--")

      def __exit__(self, *args):
            print("--exit--")

with ContextManager():
    print("test")
# --enter--
# test
# --exit--
```


## Args & Kwargs
`args` и `kwargs` - позволяют передавать функции неопределенное количество аргументов. Названия являются условными и могут быть изменены.
`args` позволяет передавать функции неограниченное количество безымянных аргументов.
```python
def foo(*args):
      print(f'Arguments passed: {args} as {type(args)}')

foo('arg1', 'arg2', 'arg3')  # Arguments passed: ('arg1', 'arg2', 'arg3') as <class 'tuple'>
```
`kwargs` позволяет передавать функции неограниченное количество именованных аргументов.
```python
def foo2(**kwargs):
      print(f'keywords: {kwargs} as {type(kwargs)}')

foo2(key1='arg1', key2='arg2')  # keywords: {'key1': 'arg1', 'key2': 'arg2'} as <class 'dict'>
```


## Standard modules

1. Модули
    1. [Обработка текста](src/modules/5_1_modules.md)
         1. [string - Общие строковые операции](src/modules/5_1_modules.md#1)
         2. [re - Операции с регулярными выражениями](src/modules/5_1_modules.md#2)
         3. [difflib - Помощники для вычисления дельт](src/modules/5_1_modules.md#3)
         4. [textwrap - Перенос и заполнение текста](src/modules/5_1_modules.md#4)
         5. [unicodedata - База данных Юникод](src/modules/5_1_modules.md#5)
         6. [stringprep - Подготовка интернет-строки](src/modules/5_1_modules.md#6)
         7. [readline - Интерфейс чтения GNU](src/modules/5_1_modules.md#7)
         8. [rlcompleter - Функция завершения для строки чтения GNU](src/modules/5_1_modules.md#8)
    2. [Двоичные данные](src/modules/5_2_modules.md)
         1. [struct - Интерпретирование байтов, как упакованные двоичные данные](src/modules/5_2_modules.md#1)
         2. [codecs - Реестр кодеков и базовые классы](src/modules/5_2_modules.md#2)
    3.  [Типы данных](src/modules/5_3_modules.md)
          1. [datetime - Основные типы даты и времени](src/modules/5_3_modules.md#1)
          2. [zoneinfo - Поддержка часовых поясов IANA](src/modules/5_3_modules.md#2)
          3. [calendar - Общие функции, связанные с календарем](src/modules/5_3_modules.md#3)
          4. [collections - Типы данных контейнера](src/modules/5_3_modules.md#4)
          5. [collections.abc - Абстрактные базовые классы для контейнеров](src/modules/5_3_modules.md#5)
          6. [heapq - Алгоритм очереди в куче](src/modules/5_3_modules.md#6)
          7. [bisect - Алгоритм деления массива пополам](src/modules/5_3_modules.md#7)
          8. [array - Эффективные массивы числовых значений](src/modules/5_3_modules.md#8)
          9. [weakref - Слабые ссылки](src/modules/5_3_modules.md#9)
          10. [types - Динамическое создание типов и имена для встроенных типов](src/modules/5_3_modules.md#10)
          11. [copy - Операции поверхностного и глубокого копирования](src/modules/5_3_modules.md#11)
          12. [pprint - Симпатичный принтер данных](src/modules/5_3_modules.md#12)
          13. [reprlib - Альтернативная реализация repr()](src/modules/5_3_modules.md#13)
          14. [enum - Поддержка перечислений](src/modules/5_3_modules.md#14)
          15. [graphlib - Функционал для работы с графоподобными структурами](src/modules/5_3_modules.md#15)
    4.  [Числа и математика](src/modules/5_4_modules.md)
          1. [numbers - Числовые абстрактные базовые классы](src/modules/5_4_modules.md#1)
          2. [math - Математические функции](src/modules/5_4_modules.md#2)
          3. [cmath - Математические функции для комплексных чисел](src/modules/5_4_modules.md#3)
          4. [decimal - Десятичная арифметика с фиксированной запятой и с плавающей запятой](src/modules/5_4_modules.md#4)
          5. [fractions - Рациональное число](src/modules/5_4_modules.md#5)
          6. [random - Генерация псевдослучайных чисел](src/modules/5_4_modules.md#6)
          7. [statistics - Функции математической статистики](src/modules/5_4_modules.md#7)
    5.  [Функциональное программирование](src/modules/5_5_modules.md)
          1. [itertools - Функции, создающие итераторы для эффективного цикла](src/modules/5_5_modules.md#1)
          2. [functools - Функции высшего порядка и операции над вызываемыми объектами](src/modules/5_5_modules.md#2)
          3. [operator - Стандартные операторы как функции](src/modules/5_5_modules.md#3)
    6.  [Доступ к файлам и каталогам](src/modules/5_6_modules.md)
          1. [pathlib - Пути к объектно-ориентированной файловой системе](src/modules/5_6_modules.md#1)
          2. [fileinput - Перебор строк из нескольких входных потоков](src/modules/5_6_modules.md#2)
          3. [stat - Интерпретация stat() результатов](src/modules/5_6_modules.md#3)
          4. [filecmp - Сравнение файлов и каталогов](src/modules/5_6_modules.md#4)
          5. [tempfile - Генерировать временные файлы и каталоги](src/modules/5_6_modules.md#5)
          6. [glob - Расширение шаблона пути в стиле Unix](src/modules/5_6_modules.md#6)
          7. [fnmatch - Сопоставление шаблонов имен файлов Unix](src/modules/5_6_modules.md#7)
          8. [linecache - Произвольный доступ к текстовым строкам](src/modules/5_6_modules.md#8)
          9. [shutil - Высокоуровневые файловые операции](src/modules/5_6_modules.md#9)
    7.  [Сохранение данных](src/modules/5_7_modules.md)
          1. [pickle - Сериализация объектов Python](src/modules/5_7_modules.md#1)
          2. [copyreg - Регистрация pickle функций поддержки](src/modules/5_7_modules.md#2)
          3. [shelve - Сохранение объектов Python](src/modules/5_7_modules.md#3)
          4. [marshal - Внутренняя сериализация объектов Python](src/modules/5_7_modules.md#4)
          5. [dbm - Интерфейсы к «базам данных» Unix](src/modules/5_7_modules.md#5)
          6. [sqlite3 - Интерфейс DB-API 2.0 для баз данных SQLite](src/modules/5_7_modules.md#6)
    8.  [Сжатие и архивирование данных](src/modules/5_8_modules.md)
          1. [zlib - Сжатие, совместимое с gzip](src/modules/5_8_modules.md#1)
          2. [gzip - Поддержка файлов gzip](src/modules/5_8_modules.md#2)
          3. [bz2 - Поддержка сжатия bzip2](src/modules/5_8_modules.md#3)
          4. [lzma - Сжатие с использованием алгоритма LZMA](src/modules/5_8_modules.md#4)
          5. [zipfile - Работа с ZIP-архивами](src/modules/5_8_modules.md#5)
          6. [tarfile - Чтение и запись файлов tar-архива](src/modules/5_8_modules.md#6)
    9.  [Форматы файлов](src/modules/5_9_modules.md)
          1. [csv - Чтение и запись CSV-файлов](src/modules/5_9_modules.md#1)
          2. [configparser - Парсер конфигурационного файла](src/modules/5_9_modules.md#2)
          3. [tomllib - Разбор файлов TOML](src/modules/5_9_modules.md#3)
          4. [netrc - обработка файлов netrc](src/modules/5_9_modules.md#4)
          5. [plistlib - Генерация и анализ .plist файлов Apple](src/modules/5_9_modules.md#5)
    10. [Криптография](src/modules/5_10_modules.md)
          1.  [hashlib - Безопасные хэши и дайджесты сообщений](src/modules/5_10_modules.md#1)
          2.  [hmac - Хеширование ключей для аутентификации сообщений](src/modules/5_10_modules.md#2)
          3.  [secrets - Генерация безопасных случайных чисел для управления секретами](src/modules/5_10_modules.md#3)
    11. [Службы ОС](src/modules/5_11_modules.md)
          1.  [os - Различные интерфейсы операционной системы](src/modules/5_11_modules.md#1)
          2.  [io - Основные инструменты для работы с потоками](src/modules/5_11_modules.md#2)
          3.  [time - Доступ ко времени и конверсии](src/modules/5_11_modules.md#3)
          4.  [argparse - Анализатор параметров командной строки, аргументов и подкоманд](src/modules/5_11_modules.md#4)
          5.  [getopt - Синтаксический анализатор в стиле C для параметров командной строки](src/modules/5_11_modules.md#5)
          6.  [logging - Возможность ведения журнала для Python](src/modules/5_11_modules.md#6)
          7.  [getpass - Портативный ввод пароля](src/modules/5_11_modules.md#7)
          8.  [curses - Обработка терминала для отображения символьных ячеек](src/modules/5_11_modules.md#8)
          9.  [platform - Доступ к идентификационным данным базовой платформы](src/modules/5_11_modules.md#9)
          10. [errno - Стандартные системные символы ошибок](src/modules/5_11_modules.md#10)
          11. [ctypes - Чужая библиотека функций для Python](src/modules/5_11_modules.md#11)
    12. [Параллельное выполнение](src/modules/5_12_modules.md)
          1.  [threading - Потоковый параллелизм](src/modules/5_12_modules.md#1)
          2.  [multiprocessing - Параллелизм на основе процессов](src/modules/5_12_modules.md#2)
          3.  [concurrent - запуск параллельных задач](src/modules/5_12_modules.md#3)
          4.  [subprocess - Управление подпроцессами](src/modules/5_12_modules.md#4)
          5.  [sched - Планировщик событий](src/modules/5_12_modules.md#5)
          6.  [queue - Класс синхронизированной очереди](src/modules/5_12_modules.md#6)
          7.  [contextvars - Контекстные переменные](src/modules/5_12_modules.md#7)
          8.  [thread - Низкоуровневый API многопоточности](src/modules/5_12_modules.md#8)
    13. [Сети и межпроцессорное взаимодействие](src/modules/5_13_modules.md)
          1.  [asyncio - Асинхронный ввод-вывод](src/modules/5_13_modules.md#1)
          2.  [socket - Низкоуровневый сетевой интерфейс](src/modules/5_13_modules.md#2)
          3.  [ssl - Оболочка TLS/SSL для объектов сокетов](src/modules/5_13_modules.md#3)
          4.  [select - Ожидание завершения ввода-вывода](src/modules/5_13_modules.md#4)
          5.  [selectors - Высокоуровневое мультиплексирование ввода-вывода](src/modules/5_13_modules.md#5)
          6.  [signal - Установите обработчики асинхронных событий](src/modules/5_13_modules.md#6)
          7.  [mmap - Поддержка файлов, отображаемых в памяти](src/modules/5_13_modules.md#7)
    14. [Обработка данных через Интернет](src/modules/5_14_modules.md)
          1.  [email - Пакет обработки электронной почты и MIME](src/modules/5_14_modules.md#1)
          2.  [json - Кодер и декодер JSON](src/modules/5_14_modules.md#2)
          3.  [mailbox - Работа с почтовыми ящиками различных форматов](src/modules/5_14_modules.md#3)
          4.  [mimetypes - Сопоставление имен файлов с типами MIME](src/modules/5_14_modules.md#4)
          5.  [base64 - Кодировки данных Base16, Base32, Base64, Base85](src/modules/5_14_modules.md#5)
          6.  [binascii - Преобразование между двоичным кодом и ASCII](src/modules/5_14_modules.md#6)
          7.  [quopri - Кодирование и декодирование MIME-данных, пригодных для печати](src/modules/5_14_modules.md#7)
    15. [Обработка структурированной разметки](src/modules/5_15_modules.md)
          1.  [html - Поддержка языка гипертекстовой разметки](src/modules/5_15_modules.md#1)
          2.  [Модули обработки XML](src/modules/5_15_modules.md#2)
    16. [Интернет-протоколы и поддержка](src/modules/5_16_modules.md)
          1.  [webbrowser - Контроллер веб-браузера](src/modules/5_16_modules.md#1)
          2.  [wsgiref - Утилиты WSGI и эталонная реализация](src/modules/5_16_modules.md#2)
          3.  [urllib - Модули обработки URL-адресов](src/modules/5_16_modules.md#3)
          4.  [http - HTTP-модули](src/modules/5_16_modules.md#4)
          5.  [ftplib - Клиент FTP-протокола](src/modules/5_16_modules.md#5)
          6.  [poplib - Клиент протокола POP3](src/modules/5_16_modules.md#6)
          7.  [imaplib - Клиент протокола IMAP4](src/modules/5_16_modules.md#7)
          8.  [smtplib - Клиент протокола SMTP](src/modules/5_16_modules.md#8)
          9.  [uuid - Объекты UUID](src/modules/5_16_modules.md#9)
          10. [socketserver - Фреймворк для сетевых серверов](src/modules/5_16_modules.md#10)
          11. [xmlrpc - Серверные и клиентские модули XMLRPC](src/modules/5_16_modules.md#11)
          12. [ipaddress - Библиотека манипуляций IPv4/IPv6](src/modules/5_16_modules.md#12)
    17. [Мультимедиа](src/modules/5_17_modules.md)
          1.  [wave - Чтение и запись файлов WAV](src/modules/5_17_modules.md#1)
          2.  [colorsys - Преобразования между цветовыми системами](src/modules/5_17_modules.md#2)
    18. [Интерналионализация](src/modules/5_18_modules.md)
          1.  [gettext - Услуги многоязычной интернационализации](src/modules/5_18_modules.md#1)
          2.  [locale - Услуги по интернационализации](src/modules/5_18_modules.md#2)
    19. [Рамки программы](src/modules/5_19_modules.md)
          1.  [turtle - Графика черепахи](src/modules/5_19_modules.md#1)
          2.  [cmd - Поддержка интерпретаторов строко-ориентированных команд](src/modules/5_19_modules.md#2)
          3.  [shlex - Простой лексический анализ](src/modules/5_19_modules.md#3)
    20. [Графические инструменты](src/modules/5_20_modules.md)
          1. [tkinter - Интерфейс Python для Tcl/Tk](src/modules/5_20_modules.md#1)
    21. [Инструменты разработки](src/modules/5_21_modules.md)
          1.  [typing - Аннотации типов](src/modules/5_21_modules.md#1)
          2.  [pydoc - Генератор документации и онлайн-справочная система](src/modules/5_21_modules.md#2)
          3.  [doctest - Тест интерактивных примеров](src/modules/5_21_modules.md#3)
          4.  [2to3 - Автоматический перевод кода Python 2 на 3](src/modules/5_21_modules.md#4)
          5.  [unittest - Фреймворк модульного тестирования](src/modules/5_21_modules.md#5)
          6.  [test - Пакет регрессионных тестов для Python](src/modules/5_21_modules.md#6)
    22. [Отладка и профилирование](src/modules/5_22_modules.md)
          1.  [bdb - Фреймворк отладчика](src/modules/5_22_modules.md#1)
          2.  [faulthandler - Дамп обратной трассировки Python](src/modules/5_22_modules.md#2)
          3.  [pdb - Отладчик Python](src/modules/5_22_modules.md#3)
          4.  [timeit - Измерение времени выполнения небольших фрагментов кода](src/modules/5_22_modules.md#4)
          5.  [trace - Отслеживание или отслеживание выполнения операторов Python](src/modules/5_22_modules.md#5)
          6.  [tracemalloc - Отслеживание распределения памяти](src/modules/5_22_modules.md#6)
    23. [Упаковка и распространение ПО](src/modules/5_23_modules.md)
          1.  [ensurepip - Загрузка pip установщика](src/modules/5_23_modules.md#1)
          2.  [venv - Создание виртуальных сред](src/modules/5_23_modules.md#2)
          3.  [zipapp - Управление исполняемыми zip-архивами Python](src/modules/5_23_modules.md#3)
    24. [Время выполнения Python](src/modules/5_24_modules.md)
          1.  [sys - Параметры и функции, специфичные для системы](src/modules/5_24_modules.md#1)
          2.  [sysconfig - Информация о конфигурации Python](src/modules/5_24_modules.md#2)
          3.  [builtins - Встроенные объекты](src/modules/5_24_modules.md#3)
          4.  [\_\_main__ - Среда кода верхнего уровня](src/modules/5_24_modules.md#4)
          5.  [warnings - Контроль предупреждения](src/modules/5_24_modules.md#5)
          6.  [dataclasses - Классы данных](src/modules/5_24_modules.md#6)
          7.  [contextlib - Утилиты для with контекстов операторов](src/modules/5_24_modules.md#7)
          8.  [abc - Абстрактные базовые классы](src/modules/5_24_modules.md#8)
          9.  [atexit - Обработчики выхода](src/modules/5_24_modules.md#9)
          10. [traceback - Распечатать или получить обратную трассировку стека](src/modules/5_24_modules.md#10)
          11. [\_\_future__ - Определения будущих операторов](src/modules/5_24_modules.md#11)
          12. [gc - Интерфейс сборщика мусора](src/modules/5_24_modules.md#12)
          13. [inspect - Осмотр живых объектов](src/modules/5_24_modules.md#13)
          14. [site - Перехватчик конфигурации для конкретного сайта](src/modules/5_24_modules.md#14)
    25. [Пользовательские интерпретаторы](src/modules/5_25_modules.md)
          1.  [code - Базовые классы интерпретатора](src/modules/5_25_modules.md#1)
          2.  [codeop - Скомпилировать код Python](src/modules/5_25_modules.md#2)
    26. [Импорт модулей](src/modules/5_26_modules.md)
          1.  [zipimport - Импорт модулей из Zip-архивов](src/modules/5_26_modules.md#1)
          2.  [pkgutil - Утилита расширения пакета](src/modules/5_26_modules.md#2)
          3.  [modulefinder - Найти модули, используемые скриптом](src/modules/5_26_modules.md#3)
          4.  [runpy - Поиск и выполнение модулей Python](src/modules/5_26_modules.md#4)
          5.  [importlib - Реализация import](src/modules/5_26_modules.md#5)
    27. [Языковые службы Python](src/modules/5_27_modules.md)
          1.  [ast - Абстрактные синтаксические деревья](src/modules/5_27_modules.md#1)
          2.  [symtable - Доступ к таблицам символов компилятора](src/modules/5_27_modules.md#2)
          3.  [token - Константы, используемые с деревьями синтаксического анализа Python](src/modules/5_27_modules.md#3)
          4.  [keyword - Тестирование ключевых слов Python](src/modules/5_27_modules.md#4)
          5.  [tokenize - Токенизатор для исходного кода Python](src/modules/5_27_modules.md#5)
          6.  [tabnanny - Обнаружение неоднозначного отступа](src/modules/5_27_modules.md#6)
          7.  [pyclbr - Поддержка браузера модуля Python](src/modules/5_27_modules.md#7)
          8.  [py_compile - Скомпилируйте исходные файлы Python](src/modules/5_27_modules.md#8)
          9.  [compileall - Байт-компилируемые библиотеки Python](src/modules/5_27_modules.md#9)
          10. [dis - Дизассемблер для байт-кода Python](src/modules/5_27_modules.md#10)
          11. [pickletools - Инструменты для разработчиков Pickle](src/modules/5_27_modules.md#11)
    28. Специальные службы для Windows
    29. Специальные службы для Unix
2. [Глоссарий](src/6_glossary.md)
3. [ООП](src/7_oop.md)




## Other


