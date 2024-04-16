# Python Cheatsheet
Version: 3.12.3

## Contents
- Built-in functions
- Types
- Exceptions
- Standard modules
- OOP


## Built-in functions
- __`abs`__: Возвращает абсолютное значение числа. [_Подробнее_](#abs)
- __`aiter`__: Возвращает асинхронный итератор для асинхронной итерации. [_Подробнее_](#aiter)
- __`all`__: Имеют ли все элементы итерируемого объекта значение True. [_Подробнее_](#all)
- __`anext`__: Возвращает следующий элемент из асинхронного итератора. [_Подробнее_](#anext)
- __`any`__: Имеет ли какой-либо элемент итерируемого объекта значение True. [_Подробнее_](#any)
- __`ascii`__: Возвращает строку с печатным представлением объекта. [_Подробнее_](#ascii)
- __`bin`__: Преобразует целое число в двоичную строку. [_Подробнее_](#bin)
- __`bool`__: Возвращает логическое значение. [_Подробнее_](#bool)
- __`breakpoint`__: Помещает в отладчик на месте вызова. [_Подробнее_](#breakpoint)
- __`bytearray`__: Возвращает изменяемый массив байт. [_Подробнее_](#bytearray)
- __`bytes`__: Возвращает неименяемый массив байт. [_Подробнее_](#bytes)
- __`callable`__: Является ли объект вызываемым. [_Подробнее_](#callable)
- __`chr`__: Возвращает символ по коду Юникода. [_Подробнее_](#chr)
- __`classmethod`__: Преоразует метод в метод класса. [_Подробнее_](#classmethod)
- __`compile`__: Компилирует строку в код, готовый к выполнению. [_Подробнее_](#compile)
- __`complex`__: Возвращает комплексное число. [_Подробнее_](#complex)
- __`delattr`__: Удаляет именованный атрибут объекта. [_Подробнее_](#delattr)
- __`dict`__: Возвращает словарь. [_Подробнее_](#dict)
- __`dir`__: Список имен в пространстве имен или атрибуты объекта. [_Подробнее_](#dir)
- __`divmod`__: Возвращает частное и остаток введенных чисел. [_Подробнее_](#divmod)
- __`enumerate`__: Возвращает перечисляемый объект. [_Подробнее_](#enumerate)
- __`eval`__: Вычисляет и выполняет введенное выражение. [_Подробнее_](#eval)
- __`exec`__: Выполняет Python код, полученный из строки. [_Подробнее_](#exec)
- **`filter`**: Фильтрует итерируемый объект заданной функцией. [_Подробнее_](#filter)
- __`float`__: Возвращает число с плавающей запятой. [_Подробнее_](#float)
- __`format`__: Форматирует строку. [_Подробнее_](#format)
- __`frozenset`__: Возвращает frozenset. [_Подробнее_](#frozenset)
- __`getattr`__: Возвращает значение именованного атрибута объекта. [_Подробнее_](#getattr)
- __`globals`__: Возвращает словарь глобальных переменных. [_Подробнее_](#globals)
- __`hasattr`__: Существует ли атрибут у объекта. [_Подробнее_](#hasattr)
- __`hash`__: Возвращает хеш объекта. [_Подробнее_](#hash)
- __`help`__: Вызов встроенной справочной системы. [_Подробнее_](#help)
- __`hex`__: Преобразует целое число в шестнадцатеричную строку. [_Подробнее_](#hex)
- __`id`__: ID объекта. [_Подробнее_](#id)
- __`input`__: Принимает входные данные. [_Подробнее_](#input)
- __`int`__: Возвращает целочисленный объект. [_Подробнее_](#int)
- __`isinstance`__: Является ли объект экземпляром другого объекта. [_Подробнее_](#isinstance)
- __`issubclass`__: Является ли класс является подклассом другого класса. [_Подробнее_](#issubclass)
- __`iter`__: Возвращает объект итератора. [_Подробнее_](#iter)
- __`len`__: Возвращает длину объекта. [_Подробнее_](#len)
- __`list`__: Возвращает объект список. [_Подробнее_](#list)
- __`locals`__: Возвращает словарь локальных переменных. [_Подробнее_](#locals)
- __`map`__: Возвращает итератор, который применяет функцию к каждому итерируемому объекту. [_Подробнее_](#map)
- __`max`__: Возвращает наибольший элемент. [_Подробнее_](#max)
- __`memoryview`__: Возвращает объект memoryview. [_Подробнее_](#memoryview)
- __`min`__: Возвращает наименьший элемент. [*Подробнее*](#min)
- __`next`__: Получает следующий элемент итератора. [_Подробнее_](#next)
- __`object`__: Возвращает новый объект. [_Подробнее_](#object)
- __`oct`__: Преобразует целое число в восьмеричную строку. [_Подробнее_](#oct)
- __`open`__: Открывает файл и возвращает файловый объект. [_Подробнее_](#open)
- __`ord`__: Возвращает код Юникода по символу. [_Подробнее_](#ord)
- __`pow`__: Возводит число в степень. [_Подробнее_](#pow)
- __`print`__: Выводит объекты. [_Подробнее_](#print)
- __`property`__: Возвращает атрибут свойства. [_Подробнее_](#property)
- __`range`__: Возвращает неизменяемый тип последовательности range. [_Подробнее_](#range)
- __`repr`__: Возвращает строку с представлением объекта. [_Подробнее_](#repr)
- __`reversed`__: Возвращает обратный итератор. [_Подробнее_](#reversed)
- __`round`__: Округляет число. [_Подробнее_](#round)
- __`set`__: Возвращает объект set. [_Подробнее_](#set)
- __`setattr`__: Присваивает значение атрибуту. [_Подробнее_](#setattr)
- __`slice`__: Возвращает часть объекта. [_Подробнее_](#slice)
- __`sorted`__: Возвращает новый отсортированный список. [_Подробнее_](#sorted)
- __`staticmethod`__: Преобразует метод в статический. [_Подробнее_](#staticmethod)
- __`str`__: Возвращает объект str. [_Подробнее_](#str)
- __`sum`__: Возвращает сумму элементов. [_Подробнее_](#sum)
- __`super`__: Делегирует вызовы методов родительскому объекту. [_Подробнее_](#super)
- __`tuple`__: Возвращает неизменяемый тип последовательности tuple. [_Подробнее_](#tuple)
- __`type`__: Возвращает тип объекта. [_Подробнее_](#type)
- __`vars`__: Возвращает атрибут dict. [_Подробнее_](#vars)
- __`zip`__: Возвращает итератор кортежей. [_Подробнее_](#zip)
- __`import`__: Вызывается оператором импорта. [_Подробнее_](#import)


## Types


## Exceptions


## Standard modules


1. [Функции](src/1_functions.md)
2. [Типы](src/2_types.md)
3. Исключения
4. [Примеры](src/4_examples.md)
5. Модули
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
6. [Глоссарий](src/6_glossary.md)
7. [ООП](src/7_oop.md)




## Other


### abs
`abs(x)`. Возвращает абсолютное значение числа. Аргумент может быть целым числом, числом с плавающей запятой или объектом, реализующим \_\_abs__(). Если аргумент является комплексным числом, возвращается его величина.
```python
abs(-1) # 1
abs(0) # 0
abs(1) # 1
abs(3.14) # 3.14
abs(3 + 2j) # 3.6055512754639896
abs(0x10) # 16
abs(0b10) # 2
abs(0o20) # 16
```


### aiter
`aiter(async_iterable)`. Возвращает асинхронный итератор для асинхронной итерации. Эквивалент звонка x.\_\_aiter__(). В отличие от iter(), aiter() не имеет варианта с двумя аргументами.
```python
async def aitersync(iterable):
    results = []
    async for x in aiter(iterable):
        results.append(x)
    return iter(results)
```


### all
`all(iterable)`. Возвращает значение True, если все элементы итерируемого объекта истинны (или если итерируемый объект пуст).
```python
all([True, True, True]) # True
all((0, True, False)) # False
all({1, 1, 1}) # True
```


### anext
`anext(async_iterator)`. При ожидании вернуть следующий элемент из заданного асинхронного итератора или значения по умолчанию, если он задан и итератор исчерпан. Это асинхронный вариант встроенной функции next(), который ведет себя аналогично.
```python

```


### any
`any(iterable)`. Возвращает значение True, если какой-либо элемент итерируемого объекта имеет значение true. Если итерируемый объект пуст, верните False.
```python
any([False, False, False]) # False
any((0, True, False)) # True
any({0, 0, 0}) # False
```


### ascii
`ascii(object)`. Возвращает строку, содержащую печатное представление объекта, но экранирует символы, отличные от ASCII.
```python
ascii('A') # 'A'
ascii('ë') # '\xeb'
ascii(['A', 'ë']) # ['A', '\xeb']
```


### bin
`bin(x)`. Преобразует целое число в двоичную строку с префиксом «0b».
```python
bin(1) # '0b1'
bin(10) # '0b1010'
bin(100) # '0b1100100'
bin(1000) # '0b1111101000'
```


### bool
`bool(x=False)`. Возвращает логическое значение. Если x имеет значение false или опущено, возвращается False; в противном случае он возвращает True. Является подклассом int.
```python
bool(0) # False
bool(1) # True
bool(2) # True
bool('3') # True
bool(False) # False
bool(True) # True
```


### breakpoint
`breakpoint(*args, **kws)`. Отправляет в отладчик на месте вызова.
```python
for i in range(5):
    if i == 2:
        breakpoint()
```


### bytearray
`bytearray(source)`. Представляет собой изменяемую последовательность целых чисел в диапазоне 0 <= x < 256. От типа bytes отличается только тем, что является изменяемым. Похож на список целых чисел, но хранит байты. Байты могут представлять двоичные данные, такие как изображение или файл, или текст в кодировке ASCII или UTF-8.
```python
data = "Hello, World!"
bytearray_obj = bytearray(data, "utf-8") # bytearray(b'Hello, World!')

data = b"Hello, World!"
bytearray_obj = bytearray(data) # bytearray(b'Hello, World!')
```


### bytes
`bytes(source)`. Возвращает новый объект «bytes», который представляет собой неизменяемую последовательность целых чисел в диапазоне 0 <= x < 256. Используется для представления изображений, аудио и других подобных файлов.
```python
data = "Hello, World!"
bytes_obj = bytes(data, "utf-8") # b'Hello, World!'

data = b"Hello, World!" # b'Hello, World!'
```


### callable
`callable(object)` возвращает True, если object вызываемый, иначе False. Классы являются вызываемыми (вызов класса возвращает новый экземпляр); экземпляры являются вызываемыми, если их класс имеет \_\_call__() метод.
```python
def my_function():
      pass

class MyClass:
      def __call__(self):
            pass

x = 5
y = my_function
z = MyClass()
a = lambda: None

print(callable(x)) # False
print(callable(y)) # True
print(callable(z)) # True
print(callable(a)) # True
```


### chr
`chr(i)` возвращает строку, являющуюся символом Юникода. Допустимый диапазон аргумента — от 0 до 1 114 111 (0x10FFFF в системе счисления 16).
```python
print(chr(97)) # 'a'
print(chr(65)) # 'A'
print(chr(120)) # 'x'
```


### classmethod
`@classmethod` используется, когда нужно получить методы, не относящиеся к какому-либо конкретному экземпляру, но привязанные к классу. Можно переопределить дочерними классами. Получает класс в качестве неявного первого аргумента, точно так же, как обычный метод экземпляра получает экземпляр. Это означает, что можно использовать класс и его свойства внутри этого метода, а не конкретного экземпляра.
```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    @classmethod
    def get_new_instance(cls):
        return cls()

if __name__ == "__main__":
    counter = Counter()
    print(counter.increment()) # 1

    counter = counter.get_new_instance()
    print(counter.increment()) # 1
```


### compile
`compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)` возвращает переданный, в качестве аргумента источник, в виде объекта кода, готового к выполнению. Объекты кода, полученные в результате выполнения функции compile() могут быть выполнены с помощью exec() или eval():
```python
x = compile('x = 1\nz = x + 5\nprint(z)', 'test', 'exec')
exec(x)
```


### complex
`complex(real=0, imag=0)` возвращает комплексное число со значением real + imag *1j или преобразует строку или число в комплексное число. Если первый параметр является строкой, он будет интерпретироваться как комплексное число, и функцию необходимо вызывать без второго параметра. Второй параметр никогда не может быть строкой. Каждый аргумент может иметь любой числовой тип (включая комплексный). Если imag опущен, по умолчанию он равен нулю, а конструктор выполняет числовое преобразование, например int и float. Если оба аргумента опущены, возвращается 0j.
```python
complex(1) # (1+0j)
complex('1') # (1+0j)
complex(100) # (100+0j)
complex('100') # (100+0j)
```


### delattr
`delattr(object, name)` аргументами являются объект и строка. Строка должна быть именем одного из атрибутов объекта. Функция удаляет именованный атрибут, если объект это позволяет. Например, delattr(x, 'foobar') равно del x.foobar.
```python

```


### dict
`dict(**kwarg)` создает новый словарь.
```python
a = dict()
type(a) # <class 'dict'>
```


### dir
`dir(object)` возвращает список имен в текущей локальной области или список допустимых атрибутов для обьекта. Если у объекта есть метод с именем \_\_dir__(), этот метод будет вызван и должен вернуть список атрибутов. Используется для анализа объектов, модулей и классов, помогая обнаружить доступные методы, атрибуты и имена.
```python
class MyClass:
    def __init__(self):
        self.x = 5
        self.y = "Hello"

obj = MyClass()
print(dir(obj))


my_list = [1, 2, 3]
print(dir(my_list))


a = 10
b = "Hello"
def my_function():
    pass

print(dir())
```


### divmod
`divmod(a, b)` принимает два числа в качестве аргументов и возвращает частное и остаток от целочисленного деления.
```python
divmod(2, 2) # (1, 0)
divmod(10, 2) # (5, 0)
divmod(7, 2) # (3, 1)
```


### enumerate
`enumerate(iterable, start=0)` возвращает перечисляемый объект. iterable должен поддерживать итерацию. Возвращает кортеж, содержащий счетчик (от начала, который по умолчанию равен 0) и значения, полученные в результате итерации по iterable.
```python
# Аналог enumerate:
def enumerate(iterable, start=0):
      n = start
      for elem in iterable:
            yield n, elem
            n += 1


for i, item in enumerate([1, 2, 3, 4, 5]):
      print(f"Index: {i}, Item: {item}")
# Index: 0, Item: 1
# Index: 1, Item: 2
# Index: 2, Item: 3
# Index: 3, Item: 4
# Index: 4, Item: 5


l = enumerate([1, 2, 3]) # <enumerate object at 0x7fcac409cc40>
l.__next__() # (0, 1)
l.__next__() # (1, 2)
l.__next__() # (2, 3)
l.__next__() # StopIteration
```


### eval
`eval(expression, globals=None, locals=None)` динамическое исполнение выражений из ввода на основе строки или скомпилированного кода. Если вы передаете в eval() строку, то функция анализирует ее, компилирует в байт-код и выполняет как выражение Python. expression - выражение python, globals - словарь, locals - обьект сопоставления.
```python
eval('1 + 4') # 5
eval('print("Hello World!")') # Hello World!
x = 10
eval('x == 10') # True
```


### exec
`exec(object, globals=None, locals=None, /, *, closure=None` поддерживает динамическое выполнение кода и принимает большие блоки кода, в отличие от eval(). Принимает либо строку, либо объект кода, например сгенерированный функцией compile(). object - строка с кодом, globals - словарь с глобальным пространством имен (по умолчанию используется текущее глобальное пространство имен), locals - словарь с локальным пространством имен (по умолчанию текущее локальное пространство имен).
```python
code_to_execute = "print('Hello, exec()!')"
exec(code_to_execute) # Output: Hello, exec()!


code = """
for i in range(5):
    print(i)
"""
exec(code)
# Output: 0
#         1
#         2
#         3
#         4


x = 10
code = "x += 5"
exec(code)
print(x)  # Output: 15


x = 5
code = "x = x * 2"
globals_dict = {"x": 10}
locals_dict = {"x": 20}
exec(code, globals_dict, locals_dict)
print(x)             # Output: 5 (unchanged)
print(globals_dict)  # Output: {'x': 10}
print(locals_dict)   # Output: {'x': 40}


def create_dynamic_function(name, args):
    code = f"def {name}({', '.join(args)}): return sum({args})"
    exec(code)

create_dynamic_function("add_numbers", ["a", "b", "c"])
result = add_numbers(2, 3, 5)
print(result)  # Output: 10
```


### filter
`filter(function, iterable)` фильтрует последовательность, применяя определенное условие к каждому элементу последовательности. Возвращает новую последовательность, содержащую только элементы, соответствующие указанному условию.
```python
def is_even(num):
      return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))
print(even_numbers) # [2, 4, 6]
```


### float
`float(x=0.0)` возвращает число с плавающей запятой, составленное из числа или строки.
```python
float('+1.23') # 1.23
float('   -12345\n') # -12345.0
float('1e-003') # 0.001
float('+1E6') # 1000000.0
float('-Infinity') # -inf
```


### format
`format(value, format_spec='')` форматирует строку.
```python
'{0}, {1}, {2}'.format('a', 'b', 'c')


# Formatting string (faster and easier)
print(f"My name is {name} and I work for {company}.")
```

### frozenset
`frozenset(iterable=set())` возвращает новый frozenset объект с элементами из итерируемого объекта.
```python
frozenset([1, 2, 3]) # frozenset({1, 2, 3})
frozenset({1, 2, 3}) # frozenset({1, 2, 3})
frozenset((1, 2, 3)) # frozenset({1, 2, 3})
```


### getattr
`getattr(object, name, default)` возвращает значение атрибута объекта. object - объект, name - имя атрибута, default - значение, если атрибут не найден.
```python
class My:
      attr1 = 'yes'
my = My()
getattr(my, 'attr1')


class Example:
    attribute = "Hello, World!"

obj = Example() # Creating an instance of the class
value = getattr(obj, 'attribute', 'Nothing found') # Using getattr to access the attribute

print(value) # Output: Hello, World!
```


### globals
`globals()` возвращает словарь пространства имен текущего модуля. Для кода внутри функций это значение устанавливается при определении функции и остается неизменным независимо от того, где функция вызывается.


### hasattr
`hasattr(object, name)` возвращает True, если объект имеет атрибут name, иначе False.


### hash
`hash(object)` возвращает хеш-значение объекта (если оно есть). Хэш-значения являются целыми числами. Они используются для быстрого сравнения ключей словаря во время поиска по словарю.
```python
hash(1) # 1
hash('1') # -3658718886659147670
hash('10') # 5216539490891759533
```


### help
`help(request)` вызов встроенной справочной системы. Если аргументом является строка, то эта строка ищется как имя модуля, функции, класса, метода, ключевого слова или раздела документации.
```python
help(type)
```


### hex
`hex(x)` преобразует целое число в шестнадцатеричную строку нижнего регистра с префиксом «0x». Если x не является int объектом, он должен определить \_\_index__() метод, возвращающий целое число.
```python
hex(1) # '0x1'
hex(10) # '0xa'
hex(100) # '0x64'
hex(1000) # '0x3e8'
```


### id
`id(object)` возвращает ID объекта. Это целое число, которое гарантированно будет уникальным и постоянным для этого объекта в течение его жизни. Два объекта с непересекающимися сроками жизни могут иметь одинаковое id() значение.
```python
id(1) # 9788960
id('1') # 140269689726000
id([1, 2]) # 140269672924928
```


### input
`input(prompt)` если prompt присутствует, он записывается в стандартный вывод без завершающего символа новой строки. Затем функция считывает строку из входных данных, преобразует ее в строку (удаляя конечный символ новой строки) и возвращает ее.
```python
print('What is your name?')   # ask for their name
my_name = input()
print('Hi, {}'.format(my_name))
# What is your name?
# Martha
# Hi, Martha
```


### int
`int(x, base=10)` возвращает целочисленный обьект, созданных из числа или строки x, иначе возвращает 0. Если x не является числом или задан base, то x должен быть bytes или bytearray экземпляром, представляющим целое число в системе счисления.
```python
from_integer = int('29') # 29
type(from_integer) # <class 'int'>
from_float = int(-3.14) # -3
type(from_float) # <class 'int'>
int() # 0
```

### isinstance
`isinstance(object, classinfo)` возвращает True, если object является экземпляром classinfo или его подкласса, иначе False.
```python
isinstance(1, int) # True
isinstance(1, str) # False
```

### issubclass
`issubclass(class, classinfo)` возвращает True, если object является подклассом classinfo, иначе False.
```python
class First:
    pass

class Second(First):
    pass

print(issubclass(Second, First))  # True
print(issubclass(First, Second)) # False
```


### iter
`iter(object, sentinel)` возвращает объект итератора. Первый аргумент интерпретируется по-разному в зависимости от наличия второго аргумента. Без второго аргумента объект должен быть объектом коллекции, который поддерживает \_\_iter__() метод, или он должен поддерживать метод \_\_getitem__() с целочисленными аргументами, начинающимися с 0. Если указан второй аргумент, то объект должен быть вызываемым объектом.
```python
i = iter([1, 2, 3]) # <list_iterator object at 0x7f93158badc0>
i.__next__() # 1
i.__next__() # 2
i.__next__() # 3
```


### len
`len(s)` возвращает длину обьекта (например, str, bytes, tuple, list, range, dict, set или frozenset).
```python
len('hello') # 5
len(['cat', 3, 'dog']) # 3
```


### list
`list(iterable)` возвращает изменяемый тип последовательности list.
```python
l = list()
l # []
l.append(1)
l.append(2)
l # [1, 2]
```


### locals
`locals()` обновляет и возвращает словарь, представляющий текущую локальную таблицу символов.
```python
def my_function():
      name = "Jim"
      age = 35
      print(locals())

my_function() # {'name': 'Jim', 'age': 35}
```


### map
`map(function, iterable, *iterables)` возвращает итератор, который применяет функцию к каждому элементу итерируемого объекта, получая результаты. Если передаются дополнительные итерируемые аргументы, функция должна принимать такое количество аргументов и применяться к элементам всех итераций параллельно.
```python
list(map(lambda x: x**2, [1,2,3,4,5])) # [1, 4, 9, 16, 25]


def max(a,b):
  if a > b: return a
  else: return b

list1= [1,1,1]
list2= [0,0,0,1,1,1,1,1,1,1]
result = list(map(max, list1, list2)) # [1, 1, 1]
```


### max
`max(arg1, arg2, *args, key=None)` если указан один позиционный аргумент, он должен быть итерируемым. Возвращается самый большой элемент в итерации. Если указаны два или более позиционных аргумента, возвращается наибольший из позиционных аргументов.
```python
max([1, 2, 10, 40, 5]) # 40
max((1, 2, 10, 40, 5)) # 40
```


### memoryview
`memoryview(object)` возвращает объект memoryview, созданный на основе данного аргумента.


### min
`min(arg1, arg2, *args, key=None)` если указан один позиционный аргумент, он должен быть итерируемым. Возвращается наименьший элемент в итерации. Если указаны два или более позиционных аргумента, возвращается наименьший из позиционных аргументов.
```python
min([1, 2, 10, 40, 5]) # 1
min((1, 2, 10, 40, 5)) # 1
```

### next
`next(iterator, default)` получает следующий элемент из итератора, вызвав \_\_next__()метод. Возвращается default или StopIteration, если итератор исчерпан.
```python
i = iter([1,2,3])
next(i) # 1
```


### object
`object` возвращает новый объект. object является базой для всех классов. Он имеет методы, общие для всех экземпляров классов. Эта функция не принимает никаких аргументов.


### oct
`oct(x)` преобразует целое число в восьмеричную строку с префиксом «0o».
```python
oct(1) # '0o1'
oct(10) # '0o12'
oct(100) # '0o144'
oct(1000) # '0o1750'
```


### open
`open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)` открывает файл и возвращает файловый объект, иначе OSError. file - путь (абсолютный или относительный к текущему рабочему каталогу) файла. mode - режим открытия файла.
Символ | Значение
--- | ---
`r` | открыть для чтения (по умолчанию)
`w` | открыть для записи, предварительно обрезав файл
`x` | открыт для эксклюзивного создания, сбой, если файл уже существует
`a` | открыть для записи, добавляя в конец файла, если он существует
`b` | двоичный режим
`t` | текстовый режим (по умолчанию)
`+` | открыт для обновления (чтение и запись)
buffering - политика буферизации (0 - отключить буферизацию (разрешено только в двоичном режиме), 1 - выбрать буферизацию строк (можно использовать только при записи в текстовом режиме), и целое число > 1 - указать размер в байтах буфера фрагментов фиксированного размера.). encoding - имя кодировки, используемой для декодирования или кодирования файла. newline - определяет, как анализировать символы новой строки из потока. Это может быть None, '', '\n', '\r', и '\r\n'. closefd - базовый дескриптор файла будет оставаться открытым при закрытии файла, если указан дескриптор файла и closefd=False. opener - дескриптор открытого файла.
```python
spam = open('spam.txt', mode='x')
spam.write('My first line\n\n')
spam.close()

with open('spam.txt', mode='a') as spam:
      spam.write('My second line')

with open('spam.txt') as spam:
      content = spam.read()
```








### ord
`ord(c)` возвращает целое число, предоставляющее код Юникода, полученного символа Юникода.
```python
ord('1') # 49
ord('a') # 97
```


### pow
`pow(base, exp, mod=None)` возвращает base в степени exp. Если mod присутствует, возвращает base в степени exp по модулю.
```python
pow(2, 3) # 8
```

### print
`print(*objects, sep=' ', end='\n', file=None, flush=False)` выводит обьекты в консоль, разделяя sep и оканчивая end. Все аргументы без ключевого преобразуются в строки и выводятся.
```python
print('Hello world!') # Hello world!

a = 1
print('Hello world!', a) # Hello world! 1

phrase = ['printed', 'with', 'a', 'dash', 'in', 'between']
for word in phrase:
      print(word, end='-')
# printed-with-a-dash-in-between-

print('cats', 'dogs', 'mice', sep=',') # cats,dogs,mice
```


### property
`property(fget=None, fset=None, fdel=None, doc=None)` возвращает атрибут свойства. fget - функция получения значения атрибута, fset - функция установки значения атрибута, fdel - функция удаления значения атрибута, doc - создает строку документации для атрибута:
```python
class C:
      def __init__(self):
            self._x = None

      def getx(self):
            return self._x

      def setx(self, value):
            self._x = value

      def delx(self):
            del self._x

      x = property(getx, setx, delx, "I'm the 'x' property.")


class Parrot:
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Декоратор @property превращает voltage() в метод получения атрибута с тем же именем, доступного только для чтения"""
        return self._voltage


# Этот код в точности эквивалентен первому примеру. Обязательно дайте дополнительным функциям то же имя, что и исходному свойству.
class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """Обьект свойства имеет методы `getter`, `setter`, `deleter`, которые можно использовать в качестве декораторов, которые создают копию св-ва с соответствующей функцией доступа"""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
```


### range
`range(start, stop, step=1)` неизменяемый тип последовательности.


### repr
`repr(object)` возвращает строку, содержающую печатное представление обьекта.


### reversed
`reversed(seq)` возвращает обратный итератор. seq должен поддерживать \_\_reversed__() или \_\_len__() и \_\_getitem__().
```python
i = reversed([1, 2, 3])
i.__next__() # 3
i.__next__() # 2
i.__next__() # 1
```


### round
`round(number, ndigits=None)` возвращает число number, округленное до ndigits знаков после запятой.
```python
round(1.4) # 1
round(1.5) # 2
round(2.1) # 2
round(2.9) # 3
round(2/3, ndigits=3) # 0.667
```


### set
`set(iterable)` возвращает новый обьект set с элементами из итерируемого объекта iterable.
```python
s = set()
s # set()
type(s) # <class 'set'>
```


### setattr
`setattr(object, name, value)` аналог getattr(). Принимает обьект, строку, произвольное значение. Присваивает значение атрибуту.
```python
setattr(x, 'name', 123)
```


### slice
`slice(start, stop, step=None)` возвращает обьект среза, представляющий набор индексов заданным `range(start, stop, step)`.
```python
furniture = ['table', 'chair', 'rack', 'shelf']
furniture[0:4] # ['table', 'chair', 'rack', 'shelf']
furniture[1:3] # ['chair', 'rack']
furniture[0:-1] # ['table', 'chair', 'rack']
furniture[:2] # ['table', 'chair']
furniture[1:] # ['chair', 'rack', 'shelf']
furniture[:] # ['table', 'chair', 'rack', 'shelf']


# Slice полного списка приводит к копированию:
spam2 = spam[:] # ['cat', 'bat', 'rat', 'elephant']
spam.append('dog')
spam # ['cat', 'bat', 'rat', 'elephant', 'dog']
spam2 # ['cat', 'bat', 'rat', 'elephant']
```


### sorted
`sorted(iterable, /, *, key=None, reverse=False)` возвращает новый отсортированный список из элементов iterable. key - функция для извлечения ключа сравнения из каждого элемента в итерации, reverse - производить ли обратную сортировку.
```python
sorted([1, 2, 3, 7, 4]) # [1, 2, 3, 4, 7]
sorted(['a', 'h', 'e']) # ['a', 'e', 'h']
sorted([1, 2, 3, 7, 4], reverse=True) # [7, 4, 3, 2, 1]
sorted(['a', 'h', 'e'], reverse=True) # ['h', 'e', 'a']
```


### staticmethod
`@staticmethod` преобразует метод в статический метод. Статический метод не получает неявного первого аргумента.
```python
class C:
      @staticmethod
      def f(arg1, arg2, argN): pass


def regular_function(): pass

class C:
      method = staticmethod(regular_function)


class Class:
      @staticmethod
      def function():
            print("X")
Class.function() # X
```


### str
`str(object=b'', encoding='utf-8', errors='strict')` возвращает обьект str.
```python
from_integer = str(29)
from_integer # '29'
type(from_integer) # <class 'str'>
from_float = str(-3.14)
from_float # '-3.14'
type(from_float) # <class 'str'>
str() # ''
```


### sum
`sum(iterable, /, start=0)` возвращает сумму полученных обьектов.
```python
sum([2, 4, 6]) # 12
sum([10, 10, 10]) # 30
```


### super
`super(type, object_or_type=None)` возвращает прокси-обьект, который делегирует вызовы методом родительскому или родственному классу type. object_or_type - порядок разрешения метода для поиска. Используется для ссылки на родительские классы. не называя из явно или для поддержки совмесного множественного наследования в динамической среде выполения.


### tuple
`tuple(iterable)` неизменяемый тип последовательности.
```python
t = tuple()
type(t) # <class 'tuple'>
t # ()
l = [1, 2, 3]
tuple(l) # (1, 2, 3)
```


### type
`type(name, bases, dict, **kwds)` возвращает тип обьекта (object.\_\_class__).
```python
type('span') # <class 'str'>
type(99) # <class 'int'>
type(1.1) # <class 'float'>
type([1, 2]) # <class 'list'>
type((1, 2)) # <class 'tuple'>
type({1, 2}) # <class 'set'>
type({'a': 1, 'b': 2}) # <class 'dict'>
```


### vars
`vars(object)` Возвращает \_\_dict__ атрибут.
```python
class Person:
      def __init__(self, name, age):
            self.name = name
            self.age = age

my_person = Person("Dwight", 35)
my_vars = vars(my_person)
print(my_vars) # {'name': 'Dwight', 'age': 35}
```


### zip
`zip(*iterables, strict=False)` Возвращает итератор кортежей, где i-й кортеж содержит i-й элемент из каждой итерации аргументов. Превращает строки в столбцы, а столбцы в строки. Если итерации имеют одинаковую длину, то рекомендуется применить strict=True:
```python
list(zip(range(3), ['fee', 'fi', 'fo', 'fum'])) # [(0, 'fee'), (1, 'fi'), (2, 'fo')]


furniture = ['table', 'chair', 'rack', 'shelf']
price = [100, 50, 80, 40]

for item, amount in zip(furniture, price):
      print(f'The {item} costs ${amount}')
# The table costs $100
# The chair costs $50
# The rack costs $80
# The shelf costs $40
```


### \_\_import__
`__import__(name, globals=None, locals=None, fromlist=(), level=0)` вызывается оператором import.