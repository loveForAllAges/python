# Документация по ЯП Python
## 1. Введение
- PEP8 - руководство по стилю кода.
- Каждая функция должна иметь краткое описание себя.
- Желательно код должен иметь аннотации типов.
### Функция range
```python
range(start_value, end_value, step)
```
### Перебор словаря
```python
a = {1: 'f', 2: 's', 3: 't'}

for k, v in a.items():
    print(k, v)
else:
    print('OK')
```
### Конструкция match case
```python
def http_error(status):
    match status:
        case 100 | 101:
            print('100')
        case 200:
            print('200')
        case _:
            print('_')

http_error(101)
```
### Какая-то странная тема
```python
def f(a, l=[]):
    l.append(a)
    return l

print(f(1))
print(f(2))
print(f(3))
```
### Аргументы функции
```python
def foo(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

foo('a', 'b', 'c', 'd', e='e', f='f')
```
### lambda функции
```python
def foo(x):
    return lambda y: y ** x

print(foo(2)(2))
```
### Формат документирования функций
```python
def foo():
    """
    Краткое описание функции с точкой на конце.

    Если есть подробности, то они указываются через пустую строку.
    """
    return

print(foo.__doc__)
```
### Аннотации функций
```python
def foo(a: str) -> str:
    return 'OK'

print(foo.__annotations__)
```
### Методы обьектов списка
#### list.append(x)
Добавление элемента в список. Эквивалентно `a[len(a):] = [x]`.
#### list.extend(iterable)
Добавление элементов из итерируемого обьекта. Эквивалентно `a[len(a):] = iterable`.
#### list.insert(i, x)
Добавление элемента в заданную позицию. i - индекс элемента перед которым вставить. `a.insert(len(a), x)` эквивалентно `a.append(x)`.
#### list.remove(x)
Удаление первого элемента из списка значение которого равно x, иначе ValueError.
#### list.pop([i])
Удаление элемента в заданной позиции в списке и возврат его. Если i не указан, то удаляет последний элемент в списке.
#### list.clear()
Удаление всех элементов из списка. Эквивалентно `del a[:]`.
#### list.index(x[, start[, end]])
Возвращение индекса первого элемента равного x, иначе ValueError. start, end необязательны и используются для ограничения поиска.
#### list.count(x)
Возвращает количество совпадений x.
#### list.sort(*, key=None, reverse=False)
Сортировка.
#### list.reverse()
Разворот списка.
#### list.copy()
Возвращает неглубокую копию списка. Эквивалентно `a[:]`.
### Использование списков в качестве очередей
Списки можно использовать в качестве очереди, где первый добавленный элемент является первым полученным элементом. Списки неэффективны для этой цели, так как вставка и удаление из начала списка выполняется медленно. Для реализации очереди есть collections.deque.
### Пример использования списков
Способы создания списка:
```python
lst = list(map(lambda x: x**2, range(10)))
```
```python
lst = [x**2 for range(10)]
```
```python
lst = []
for x in range(10):
    lst.append(x**2)
```
Способы транспонирования матрицы
```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
```
```python
[[row[i] for row in matrix] for i in range(4)]
```
```python
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
```
```python
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
```
```python
list(zip(*matrix))
```
### del
Удаляет элементы из списка, переменные.
```python
del lst[0]
del lst[:]
del lst[2:3]
del var
```
### Тип данных: Набор
Набор - неупорядоченная коллекция без повторяющихся элементов.
```python
s = {'o', 't', 'th', 'f'}
s = set()
s = {x for x in 'abc' if x not in  'def'}
s1 = set('abc')
s2 = set('def')
s1 - s2
s1 | s2
s1 & s2
s1 ^ s2
```
### Методы работы с циклами
Для перебора словаря в виде ключ-значение используют `dict.items()`. Для перебора списка в виде ключ-значение используют `enumerate(list)`. Для перебора нескольких списков одновременно используют `zip(list1, list2)`. Для перебора обратной последовательности используют `reversed(...)`. Для перебора отсортированной последовательности используют `sorted(...)`.
### Функция dir() 
Возвращает отсортированный список строк имен модуля.
## 3. I/O
### Форматирование вывода
```python
str1 = f'Line {var}'
str2 = '{}'.format(var)
str2 = '{a}'.format(a=var)
str2 = '{0}'.format(var)
str3 = str(var)
str4 = repr(var)
str5 = ('str %i' % 1)
```
Форматированный вывод сгенерированной матрицы указанного размера.
```python
size = 20
matrix = [[j+i*size for j in range(1, size+1)] for i in range(size)]

[print(' '.join([str(j).rjust(len(str(size ** 2))) for j in i])) for i in matrix]
```
### Чтение-запись файлов
Режимы открытия файла: `r` - только для чтения, `w` - только для записи (очищает), `a` - для добавления, `r+` - для чтения и записи. Добавление `b` откроет в двоичном режиме.
```python
f = open(filename, mode='r', encoding=None)
```
Рекомендуется использовать с конструкцией with, файл корректно закроется после завершения работы:
```python
with open('filepath', encoding="utf-8") as f:
    read_data = f.read()
```
Иначе необходимо вручную закрывать файл:
```python
f.close()
```
#### Методы файловых обьектов
##### f.read(size)
Считывает некоторое количество данных и возвращает в виде строки или байтового обьекта. Если size не указан, то будет возвращено все содержимое файла.
##### f.readline()
Считывает одну строку из файла, которая заканчивается \n. Если достигнут конец файла, то возвращается пустая строка.
##### f.readlines()
Все строки файла в списке или list(f).
##### f.write(string)
Записывает строку в файл и возвращает кол-во записанных символов.
##### f.tell()
Возвращает целое число, указывающее текущую позицию файлового обьекта в файле, представленное как кол-во байтов от начала файла в двоичном режиме
##### f.seek(offset, whence)
Изменение положения файлового обьекта. offset - положение, whence - опорная точка (0 - начало файла, 1 - текущая позиция файла, 2 - конец файла). По умолчанию 0.
## Генераторы
При каждом вызове next() генератор возобновляет работу с того места, где остановился (он запоминает все значения данных и то, какой оператор был выполнен последним). Методы __iter__ и __next__ создаются автоматически.
```python
def reverse(data):
    for i in range(len(data)-1, -1, -1):
        yield data[i]

for i in reverse('spam'):
    print(i)
```
## Генераторные выражения
Выражения-генераторы более компактны, но менее универсальны, чем полные определения генераторов, и более удобны для памяти, чем эквивалентные определения списков.
```python
sum(i*i for i in range(10))
```

## Модули стандартной библиотеки
### os
Модуль для взаимодействия с ОС.
```python
import os
```
### shutil
Модуль для ежедневных задач, управления файлами и каталогами.
```python
import shutil
```
### glob
Модуль предоставляет функцию для создания списков файлов на основе поиска по подстановочным знакам в каталоге:
```python
import glob
glob.glob('*.py')
```
### sys
Модуль для обработки аргументов командной строки:
```python
import sys

print(sys.argv)
```
Также имеет атрибуты stdin, stdout, stderr. Полезно для вывода предупреждений и сообщений об ошибках, чтобы сделать их видимыми, даже если стандартный ввод был перенаправлен.
Способ завершить программу:
```python
sys.exit()
```
### argparse
Модуль для более сложной обработки аргументов командной строки:
```python
import argparse

'python top.py --lines=5 alpha.txt beta.txt'
parser = argparse.ArgumentParser(prog='top',description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
```
### re
Модуль предоставляет инструменты регулярных выражений для расширенной обработки строк. Предлагают краткие и оптимизированные решения для сложных сопоставлений и манипуляций:
```python
import re

re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
```
Для простых манипуляций рекомендуется использовать строковые методы, так как их легче читать и отлаживать:
```python
'tea for too'.replace('too', 'two')
```
### math
Модуль предоставляет доступ к базовым функциям библиотеки Си для вычислений с плавающей запятой:
```python
import math
math.cos(math.pi / 4)
math.log(1024, 2)
```
### random
Модуль предоставляет инструменты для случайного выбора:
```python
import random
random.choice(['apple', 'pear', 'banana'])
'apple'
random.sample(range(100), 10)
random.random()
random.randrange(6) 
```
### statistics
Модуль рассчитывает основные статические свойства (среднее значение, медиану, дисперсию и т.д.) числовых данных:
```python
import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)
statistics.median(data)
statistics.variance(data)
```
### urllib.request.urlopen
Простой модуль для доступа в Интернет, обработки интернет-протоколов и получения данных из URL адресов:
```python
from urllib.request import urlopen
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()
        if line.startswith('datetime'):
            print(line.rstrip())
```
### smptlib
Простой модуль для доступа в Интернет, обработки интернет-протоколов и отправки email. Необходим почтовый сервер на локальном хосте:
```python
import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('email@example.org', 'email@example.org',
"""To: email@example.org
From: email@example.org

Beware the Ides of March.
""")
server.quit()
```
### datetime
Модуль для управления датами и временем, поддерживает обьекты, учитывающие часовой пояс:
```python
from datetime import date
now = date.today()
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
birthday = date(1964, 7, 31)
age = now - birthday
age.days
```
### zlib
Модуль архивирования и сжатия данных:
```python
import zlib
s = b'witch which has which witches wrist watch'
t = zlib.compress(s)
zlib.decompress(t)
zlib.crc32(s)
```
### timeit.Timer
Модуль измерения времени выполнения кода
```python
from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
```
### doctest
Модуль для сканирования модуля и проверки тестов в строках документации:
```python
import doctest
def foo(i):
    """
    Foo desc

    >>> print(foo(2))
    4
    """
    return i*i
print(doctest.testmod())
```
### unittest
Модуль инструментов для тестирования:
```python
import unittest
class TestFoo(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(foo(2), 4)
unittest.main()
```
### reprlib
Модуль предоставляет версию repr() для сокращенного отображения больших или глубоко вложенных контейнеров:
```python
import reprlib
reprlib.repr(set('supercalifragilisticexpialidocious'))
```
### pprint
Модуль предоставляет более сложный контроль над выводом в консоль обьектов.
```python
import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""
print(textwrap.fill(doc, width=40))
```
### textwrap
Модуль форматирует абзацы текста по заданной ширине.
```python
import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""
print(textwrap.fill(doc, width=40))
```
### locale
Модуль имеет доступ к БД форматов данных, обеспечивает прямой способ форматирования чисел с помощью разделителей групп:
```python
import locale
locale.setlocale(locale.LC_ALL, 'russian')
conv = locale.localeconv()
output = locale.format_string("%d %s", (1000000, conv['currency_symbol']), grouping=True)
```
### string
Модуль включает Template() для редактирования конечными пользователями:
```python
from string import Template
t = Template('$atext new text $b.')
t.substitute(a='New', b='correct')
```
### struct
Модуль предоставляет функции pack() и unpack() для работы с форматами двоичных записей переменной длины.
```python
import struct
with open('myfile.zip', 'rb') as f:
    data = f.read()
start = 0
for i in range(3):
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields
    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)
    start += extra_size + comp_size
```
### threading
Модуль для выполнения задач в фоновом режиме - другом потоке. Основная проблема многопоточных приложений — координация потоков, которые совместно используют данные или другие ресурсы:
```python
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')
background.join()
print('Main program waited until background was done.')
```
### logging
Модуль предоставляет полнофункциональную и гибкую систему логирования. В самом простом случае сообщения журнала отправляются в файл или в sys.stderr:
```python
import logging
logging.debug('Debugging information')
```
### weakref
Модуль предоставляет инструменты для отслеживания без создания ссылки на них:
```python
import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
del a
gc.collect()
```
### array
Модуль предоставляет array(), похожий на список, который хранит только однородные данные и хранит их более компактно:
```python
from array import array
a = array('H', [4000, 10, 700, 22222])
```
### collections
Модуль предоставляет deque(), похожий на список, с более быстрым добавлением и извлечением с левой стороны, но более медленным поиском в середине. Подходит для реализации очередей и поиска по дереву в ширину:
```python
from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
d.popleft()
```
### bisect
Модуль с функциями для управления отсортированными списками:
```python
import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
```
### heapq
Модуль с функциями для реализации кучи на основе обычных списков. Запись с наименьшим значением всегда сохраняется в начале. Это полезно, когда неоднократно обращаются к наименьшему элементу, но не хотят выполнять полную сортировку списка:
```python
from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)
heappush(data, -5)
[heappop(data) for i in range(3)] 
```
### decimal
Модуль с Decimal типом данных для десятичной арифметики с плавающей запятой. Полезно для финансовых вычислений, точности десятичного представления, контроля округления, отслеживания значимых десятичных знаков:
```python
>>> from decimal import *
>>> round(Decimal('0.70') * Decimal('1.05'), 2)
Decimal('0.74')
>>> round(.70 * 1.05, 2)
0.73
```