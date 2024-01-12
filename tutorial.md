## Модули стандартной библиотеки
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
### locale
Модуль имеет доступ к БД форматов данных, обеспечивает прямой способ форматирования чисел с помощью разделителей групп:
```python
import locale
locale.setlocale(locale.LC_ALL, 'russian')
conv = locale.localeconv()
output = locale.format_string("%d %s", (1000000, conv['currency_symbol']), grouping=True)
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

