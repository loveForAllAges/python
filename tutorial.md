# Документация по ЯП Python

1. [Функции](1_functions.md)
2. Типы
3. Исключения
4. Примеры
5. Модули
5.1. Обработка текста
5.2. Двоичные данными
5.3. Типы данных


5.4. числовые и математические
5.5. функционального программирования
5.6. для доступа к файлам и каталогам
5.7. сохранения данных
5.8. сжатия и архивирования данных
5.9. форматов файлов
5.10. криптографии
5.11. служб ОС
5.12. параллельного выполнения
5.13. сетей и межпроцессорного взаимодействия
5.14. обработки данных через Интернет
5.15. обработки структурированной разметки
5.16. с интернет-протоколами и поддержкой
5.17. мультимедийные
5.18. интернализации
5.19. программы
5.20. с графическими инструментами
5.21. с инструментами разработки
5.22. отладки и профилирования
5.23. упаковки и распространения ПО
5.24. времени выполнения
5.25. пользовательских интерпретаторов
5.26. импорта
5.27. языковые
5.28. специальные для Windows.
5.29. специальные для Unix.
5.30. интерфейса командной строки.
5.31. замененные



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
