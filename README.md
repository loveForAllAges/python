# Документация по ЯП Python

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
          1. [datetime - Основные типы даты и времени `Full`](src/modules/5_3_modules.md#1)
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
          2. [os.path - Общие манипуляции с путями](src/modules/5_6_modules.md#2)
          3. [fileinput - Перебор строк из нескольких входных потоков](src/modules/5_6_modules.md#3)
          4. [stat - Интерпретация stat() результатов](src/modules/5_6_modules.md#4)
          5. [filecmp - Сравнение файлов и каталогов](src/modules/5_6_modules.md#5)
          6. [tempfile - Генерировать временные файлы и каталоги](src/modules/5_6_modules.md#6)
          7. [glob - Расширение шаблона пути в стиле Unix](src/modules/5_6_modules.md#7)
          8. [fnmatch - Сопоставление шаблонов имен файлов Unix](src/modules/5_6_modules.md#8)
          9. [linecache - Произвольный доступ к текстовым строкам](src/modules/5_6_modules.md#9)
          10. [shutil - Высокоуровневые файловые операции](src/modules/5_6_modules.md#10)
    7.  [Сохранение данных](src/modules/5_7_modules.md)
          1. [pickle - Сериализация объектов Python](src/modules/5_7_modules.md#1)
          2. [copyreg - Регистрация pickle функций поддержки](src/modules/5_7_modules.md#2)
          3. [shelve - Сохранение объектов Python](src/modules/5_7_modules.md#3)
          4. [marshal - Внутренняя сериализация объектов Python](src/modules/5_7_modules.md#4)
          5. [dbm - Интерфейсы к «базам данных» Unix](src/modules/5_7_modules.md#5)
          6. [sqlite3 - Интерфейс DB-API 2.0 для баз данных SQLite](src/modules/5_7_modules.md#6)
    8.  Сжатие и архивирование данных
    9.  Форматы файлов
    10. Криптография
    11. Службы ОС
    12. Параллельное выполнение
    13. Сети и межпроцессорное взаимодействие
    14. Обработка данных через Интернет
    15. Обработка структурированной разметки
    16. Интернет-протоколы и поддержка
    17. Мультимедиа
    18. Интерналионализация
    19. Рамки программы
    20. Графические инструменты
    21. Инструменты разработки
    22. Отладка и профилирование
    23. Упаковка и распространение ПО
    24. Время выполнения
    25. Пользовательские интерпретаторы
    26. Импорт модулей
    27. Языковые службы
    28. Специальные службы для Windows
    29. Специальные службы для Unix
    30. Интерфейс командной строки
    31. Замененные модули
