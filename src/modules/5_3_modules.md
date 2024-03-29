# Типы данных
1. [datetime - Основные типы даты и времени](#1)
2. [zoneinfo - Поддержка часовых поясов IANA](#2)
3. [calendar - Общие функции, связанные с календарем](#3)
4. [collections - Типы данных контейнера](#4)
5. [collections.abc - Абстрактные базовые классы для контейнеров](#5)
6. [heapq - Алгоритм очереди в куче](#6)
7. [bisect - Алгоритм деления массива пополам](#7)
8. [array - Эффективные массивы числовых значений](#8)
9. [weakref - Слабые ссылки](#9)
10. [types - Динамическое создание типов и имена для встроенных типов](#10)
11. [copy - Операции поверхностного и глубокого копирования](#11)
12. [pprint - Симпатичный принтер данных](#12)
13. [reprlib - Альтернативная реализация repr()](#13)
14. [enum - Поддержка перечислений](#14)
15. [graphlib - Функционал для работы с графоподобными структурами](#15)


## <div id="1">1. datetime - Основные типы даты и времени</div>
Модуль предоставляет классы для управления датами и временем. Обьекты могут владеть информацией для определения часового пояса. Для этого `datetime` и `date` обьекты имеют дополнительный атрибут `tzinfo` с информацией об отклонении времени от UTC, названии часового пояса и о том, действует ли летнее время. Обьекты неизменяемы и хешируемы.


### Константы
#### MINYEAR
Наименьшее число года, разрешенное для обьектов `date`, `datetime`. По умолчанию `1`.
#### MAXYEAR
Максимальное число лет, разрешенное для обьектов `date`, `datetime`. По умолчанию `9999`.
#### UTC
Псевдоним для одноэлементного часового пояса UTC datetime.timezone.utc.


### Типы
#### class date(year, month, day)
Обьект представляет дату. Все аргументы обязательны. Аргументы должны быть целыми числами: MINYEAR <= year <= MAXYEAR; 1 <= month <= 12. Атрибуты: `year`, `month`, `day`.
##### date.today()
Возвращает текущую дату. Эквивалентно `date.fromtimestamp(time.time())`.
##### date.fromtimestamp(timestamp)
Возвращает локальную дату, соответствующую временной метке POSIX.
##### date.fromordinal(ordinal)
Возвращает дату, соответствующую григорианскому порядковому номеру, где 1 января 1 года имеет номер 1.
##### date.fromisoformat(date_string)
Возвращает обьект `date`, соответствующее строке `date_string`, указанной в любом ISO 8601 формате, за исключением порядковых дат (например, `YYYY-DDD`).
##### date.fromisocalendar(year, week, day)
Возвращает `date`, соответствующую календарю ISO, указанную годом, неделей, днем. Обратная функция `date.isocalendar()`.
##### date.min
Первая представимая дата.
##### date.max
Последняя представимая дата.
##### date.resolution
Наименьшая возможная разница между неравными обьектами даты.
##### date.year
Между MINYEAR и MAXYEAR.
##### date.month
От 1 до 12.
##### date.day
Между 1 и количеством дней в данном месяце данного года.
##### date.replace(year=self.year, month=self.month, day=self.day)
Возвращает дату с измененными и неизмененными значениями.
##### date.timetuple()
Возвращает `time.struct_time`. Часы, минуты, секунды равны 0, а флаг летнего времени равен -1.
##### date.toordinal()
Возвращает пролептический григорианский порядковый номер даты.
##### date.weekday()
Возвращает день недели как целое число (пн - 0, вс - 6).
##### date.isoweekday()
Возвращает день недели как целое число (пн - 1, вс - 7).
##### date.isocalendar()
Возвращает именованный обьект-кортеж (year, week, weekday).
##### date.isoformat()
Возвращает строку, представляющую дату в формате ISO 8601 (YYYY-MM-DD).
##### date.__str__()
Эквивалентно `date.isoformat()`.
##### date.ctime()
Возвращает строку, предствляющую дату. Эквивалентно `time.ctime(time.mktime(d.timetuple()))`.
##### date.strftime(format)
Возвращает строку, представляющую дату, управляемую строкой явного формата.
##### date.__format__(format)
Аналогично `date.strftime()`.
##### Операции
- `date2 = date1 + timedelta`
- `date2 = date1 - timedelta`
- `timedelta = date1 - date2`
- `date1 < date2`
##### Пример
```python
date(
    year=2000,
    month=10,
    day=10
) # datetime.date(2000, 10, 10)
```


#### class time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
Обьект представляет время, независимое от дня и подлежащее настройке с помощью `tzinfo`. `tzinfo` может быть `None` или экземпляром подкласса `tzinfo`.
##### time.min
Первый представимый `time` (`time(0,0,0,0)`).
##### time.max
Последний представимый `time` (`time(23, 59, 59, 999999)`).
##### time.resolution
Наименьшая возможная разница между `time` обьектами.
##### time.hour
`range(24)`.
##### time.minute
`range(60)`.
##### time.second
`range(60)`.
##### time.microsecond
`range(1000000)`.
##### time.tzinfo
Обьект передается конструктору в качестве аргумента `tzinfo`.
##### time.fold
`[0, 1]`. Используется для устранения неоднозначности времени.
##### time.fromisoformat(time_string)
Возвращает значение `time` соответствующее `time_string` любого формата ISO 8601.
```python
time.fromisoformat("04:20:00")
```
##### time.replace(hour=self.hour, minute=self.minute, second=self.second, microsecond=self.microsecond, tzinfo=self.tzinfo, *, fold=0)
Возвращает `time` с измененными и неизменными значениями.
##### time.isoformat(timespec='auto')
Возвращает строку времени в формате ISO 8601.
```python
dt = time(hour=12, minute=34, second=56, microsecond=0)
dt.isoformat(timespec='microseconds') # '12:34:56.000000'
dt.isoformat(timespec='auto') # '12:34:56'
```
##### time.__str__()
Эквивалентно `time.isoformat()`.
##### time.strftime(format)
Возвращает сроку времени в формате `format`.
##### time.__format__(format)
Эквивалентно `time.strftime()`.
##### time.utcoffset()
Возвращает `None`, если `tzinfo is None`, иначе `self.tzinfo.utcoffset(None)`.
##### time.dst()
Возвращает `None`, если `tzinfo is None`, иначе `self.tzinfo.dst(None)`.
##### time.tzname()
Возвращает `None`, если `tzinfo is None`, иначе `self.tzinfo.tzname(None)`.
##### Пример
```python
time(
    hour=23,
    minute=59,
    second=59,
)
```


#### class datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
Содержит информацию об `date` и `time` обьектах. Аргументы: 
- MINYEAR <= year <= MAXYEAR; 
- 1 <= month <= 12; 
- 0 <= hour < 24; 
- 0 <= minute < 60; 
- 0 <= second < 60; 
- 0 <= microsecond < 1000000; 
- fold in [0, 1].
##### datetime.today()
Возвращает текущую локальную дату и время с `tzinfo` = `None`. Эквивалентно `datetime.fromtimestamp(time.time())`.
##### datetime.now(tz=None)
Возвращает текущую местую дату и время.
##### datetime.fromtimestamp(timestamp, tz=None)
Возвращает локальную дату и время, соответствующие временной метке `timestamp` POSIX.
##### datetime.fromordinal(ordinal)
Возвращает `datetime` соответствующее `ordinal` номеру по григорианскому календарю.
##### datetime.combine(date, time, tzinfo=time.tzinfo)
Возвращает новый `datetime`, компоненты даты которого равны компонентам `date`, а компоненты времени равны компонентам `time`.
##### datetime.fromisoformat(date_string)
Возвращает значение `datetime`, соответствующее строку `date_string`, в любом допустимом формате ISO 8601
##### datetime.fromisocalendar(year, week, day)
Возвращает `datetime`, соответствующую календарю ISO по году, неделе, дню.
##### datetime.strptime(date_string, format)
Возвращает `datetime`, соответствующий формату `date_string`.
##### datetime.min
Первый представимый `datetime`.
##### datetime.max
Последний представимый `datetime`.
##### datetime.resolution
Наименьшая возможная разница между `datetime` обьектами.
##### datetime.year (см. выше)
##### datetime.day (см. выше)
##### datetime.hour (см. выше)
##### datetime.minute (см. выше)
##### datetime.second (см. выше)
##### datetime.microsecond (см. выше)
##### datetime.tzinfo
Обьект передается конструктору в качестве аргумента `tzinfo` в `datetime`.
##### datetime.fold
Используется для устранения неоднозначночти времени (0 (1) - ранний (поздний) из двух моментов).
##### datetime.date()
Возвращает обьект `date`.
##### datetime.time()
Возвращает обьект `time`.
##### datetime.timetz()
Возвращает обьект `time` с `tzinfo`.
##### datetime.replace(year=self.year, month=self.month, day=self.day, hour=self.hour, minute=self.minute, second=self.second, microsecond=self.microsecond, tzinfo=self.tzinfo, *, fold=0)
Возвращает дату и время с измененными и неизмененными атрибутами.
##### datetime.astimezone(tz=None)
Возвращает обьект `datetime` с новым `tzinfo` атрибутом и корректированным временем.
##### datetime.utcoffset()
Возвращает `None`, если `tzinfo = None`, иначе возвращает `self.tzinfo.utcoffset(self)`.
##### datetime.dst()
Возвращает `None`, если `tzinfo = None`, иначе возвращает `self.tzinfo.dst(self)`.
##### datetime.tzname()
Возвращает `None`, если `tzinfo = None`, иначе возвращает `self.tzinfo.tzname(self)`.
##### datetime.timetuple()
Возвращает `time.struct_time`.
##### datetime.utctimetuple()
Схоже с `datetime.timetuple()`.
##### datetime.toordinal()
Возвращает григорианский порядковый номер даты.
##### datetime.timestamp()
Возвращает временную метку POSIX, соответствующую экземпляру `datetime`.
##### datetime.weekday() (см. выше)
##### datetime.isoweekday() (см. выше)
##### datetime.isocalendar() (см. выше)
##### datetime.isoformat(sep='T', timespec='auto') (см. выше)
##### datetime.__str__() (см. выше)
##### datetime.ctime() (см. выше)
##### datetime.strftime(format) (см. выше)
##### datetime.__format__(format) (см. выше)
##### Операции
- `datetime2 = datetime1 + timedelta`
- `datetime2 = datetime1 - timedelta`
- `timedelta = datetime1 - datetime2`
- `datetime < datetime2`
##### Пример
```python
datetime(
    year=2000,
    month=10,
    day=10,
    hour=10,
    minute=10,
    second=10
) # datetime.datetime(2000, 10, 10, 10, 10, 10)
```


#### class timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
Обьект представляет продолжительность между двумя `date`, `datetime` или `time`. Все аргументы необязательны. Внутри хранятся только дни, секунды и микросекунды. Преобразования аргументов: Миллисекунда преобразуется в 1000 микросекунд; Минута конвертируется в 60 секунд; Час преобразуется в 3600 секунд; Неделя преобразуется в 7 дней. Затем данные нормализуются: 0 <= микросекунды < 100000; 0 <= секунды < 3600*24; -999999999 <= дни <= 999999999.
##### timedelta.min
Самый негативный обьект.
##### timedelta.max
Самый позитивный обьект.
##### timedelta.resolution
Наименьшая возможная разница между неравными обьектами.
##### timedelta.total_seconds()
Возвращает общее количество секунд.
##### Операции
- `t1 = t2 + t3`
- `t1 = t2 - t3`
- `t1 = t2 * int`
- `t1 = t2 * float`
- `float = t2 / t3`
- `t1 = t2 / float`, `t1 = t2 / int`
- `t1 = t2 // int`, `t1 = t2 // t3`
- `t1 = t2 % t3`
- `q, r = divmod(t1, t2)`
- `+t1`
- `-t1`
- `abs(t)`
- `str(t)`
- `repr(t)`
- операции сложения и вычитания `date`, `datetime`
##### Пример
```python
timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
) # datetime.timedelta(days=64, seconds=29156, microseconds=10)
```


#### tzinfo
Абстрактный базовый класс для обьектов информации о часовом поясе. Используется `datetime` и `time` для определения часового пояса.
##### tzinfo.utcoffset(dt)
Возвращает смещение местного времени от UTC в виде `timedelta` объекта, положительного к востоку от UTC. Если местное время находится к западу от UTC, оно должно быть отрицательным.
##### tzinfo.dst(dt)
Возвращает настройку летнего времени (DST) в виде `timedelta` объекта или `None` если информация о летнем времени неизвестна.
##### tzinfo.tzname(dt)
Возвращает имя часового пояса, соответствующее объекту `datetime` dt, в виде строки.
##### tzinfo.fromutc(dt)
Вызывается из `datetime.astimezone()`.


#### class timezone(offset, name=None)
Является подклассом `tzinfo`, каждый экземпляр которого представляет часовой пояс, определенный фиксированным смещением от UTC. `offset` должен быть указан как `timedelta` объект, представляющий разницу между местным временем и временем в формате UTC. Оно должно находиться строго между `-timedelta(hours=24)` и `timedelta(hours=24)`.
##### timezone.utcoffset(dt)
Возвращает фиксированное значение, указанное при создании `timezone` экземпляра.
##### timezone.tzname(dt)
Возвращает фиксированное значение, указанное при `timezone` создании экземпляра.
##### timezone.dst(dt)
Всегда возвращает `None`.
##### timezone.fromutc(dt)
Возвращает `dt + offset`. `dt` - экземпляр `datetime` с `tzinfo`.
##### timezone.utc
Часовой пояс UTC, `timezone(timedelta(0))`.
#### Коды форматов strftime и strptime
Код | Описание
--- | ---
`%a` | День недели как сокращенное название локали (Sun, Mon, ..., Sat).
`%A` | День недели в качестве полного названия локали (Sunday, Monday, ..., Saturday).
`%w` | День недели в виде десятичного числа, где 0 — воскресенье, а 6 — суббота (0, 1, ..., 6).
`%d` | День месяца в виде десятичного числа, дополненного нулями (01, 02, ..., 31).
`%b` | Месяц как сокращенное название локали (Jan, Feb, ..., Dec).
`%B` | Месяц как полное название локали (January, February, ..., December).
`%m` | Месяц в виде десятичного числа, дополненного нулями (01, 02, ..., 12).
`%y` | Год без столетия в виде десятичного числа с нулевым дополнением (00, 01, ..., 99).
`%Y` | Год со столетием в виде десятичного числа (0001, 0002, ..., 2013, 2014, ..., 9998, 9999).
`%H` | Час (24-часовой формат) в виде десятичного числа с добавлением нуля (00, 01, ..., 23).
`%I` | Час (12-часовой формат) в виде десятичного числа с добавлением нуля (01, 02, ..., 12).
`%p` | Региональный эквивалент AM или PM (AM, PM).
`%M` | Минуты в виде десятичного числа, дополненного нулями (00, 01, …, 59).
`%S` | Второе в виде десятичного числа, дополненного нулями (00, 01, …, 59).
`%f` | Микросекунда как десятичное число, дополненное нулями до 6 цифр (000000, 000001, ..., 999999).
`%z` | Смещение UTC в форме `±HHMM[SS[.ffffff]]` (пустая строка, если объект является наивным) ((пусто), +0000, -0400, +1030, +063415, -030712.345216).
`%Z` | Имя часового пояса (пустая строка, если объект является наивным) ((пусто), UTC, GMT).
`%j` | День года в виде десятичного числа с нулевым дополнением (001, 002, ..., 366).
`%U` | Номер недели года (воскресенье как первый день недели) в виде десятичного числа с добавлением нуля. Все дни нового года, предшествующие первому воскресенью, считаются неделей 0 (00, 01, ..., 53).
`%W` | Номер недели года (понедельник как первый день недели) в виде десятичного числа с добавлением нуля. Все дни нового года, предшествующие первому понедельнику, считаются неделей 0 (00, 01, ..., 53).
`%v` | Соответствующее языковому стандарту представление даты и времени (Tue Aug 16 21:30:00 1988).
`%x` | Соответствующее языковому стандарту представление даты (08/16/88 (None);
08/16/1988).
`%X` | Представление времени, соответствующее локали (21:30:00).
`%%` | Символ '%'.






## <div id="2">2. zoneinfo - Поддержка часовых поясов IANA</div>
> Модуль предоставляет улучшенный способ работы с временными зонами по сравнению с устаревшими модулями (datetime, pytz). Модуль позволяет переводить даты и время из одной временной зоны в другую.

## <div id="3">3. calendar - Общие функции, связанные с календарем</div>
> Модуль предоставляет функции для работы с календарем.


## <div id="4">4. collections - Типы данных контейнера</div>
> Модуль реализует специализированные типы данных контейнеров, предоставляя альтернативу встроенным контейнерам (dict, list, set, tuple).
### Использование
- Создание частотных словарей для подсчета количества элементов в итерируемом обьекте.
- Создание словарей со значениями по умолчанию.
- Создание словарей с сохранением порядка вставки элементов.
- Создание именнованных кортежей с явными именами полей.
- Создание двустронней очереди, которая более эффективна при удалении и добавлении элементов с начала или конца.
- Реализация очередей, поиск по дереву в ширину.
### Пример
Модуль предоставляет `deque`, похожий на список, с более быстрым добавлением и извлечением с левой стороны, но более медленным поиском в середине. Подходит для реализации очередей и поиска по дереву в ширину:
```python
d = deque(["task1", "task2", "task3"])
d.append("task4")
d.popleft()
```

## <div id="5">5. collections.abc - Абстрактные базовые классы для контейнеров</div>
> Модуль предоставляет абстрактные базовые классы для коллекций. Эти классы определяют общий интерфейс для различных типов данных (списки, множества, словари и т.д.). 


## <div id="6">6. heapq - Алгоритм очереди в куче</div>
> Модуль предоставляет реализацию двоичной кучи. Кучи — это двоичные деревья, в которых каждый родительский узел имеет значение, меньшее или равное любому из его дочерних узлов. В этой реализации используются массивы, для которых `heap[k] <= heap[2*k+1]` и `heap[k] <= heap[2*k+2]` для всех k, считая элементы с нуля. Для сравнения несуществующие элементы считаются бесконечными. Интересное свойство кучи состоит в том, что ее наименьший элемент всегда является корнем, `heap[0]`.
### Использование
- Очередь с приоритетами.
- Сортировка по частям.
- Алгоритмы поиска.
- Планирование задач.
### Пример
Модуль с функциями для реализации кучи на основе обычных списков. Запись с наименьшим значением всегда сохраняется в начале. Это полезно, когда неоднократно обращаются к наименьшему элементу, но не хотят выполнять полную сортировку списка:
```python
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)
heappush(data, -5)
[heappop(data) for i in range(3)] 
```


## <div id="7">7. bisect - Алгоритм деления массива пополам</div>
> Модуль предоставляет поддержку хранения списка в отсортированном порядке без необходимости сортировки списка после каждой вставки. Использует базовый алгоритм деления пополам для поиска точки вставки. Вместо метода `__eq__()` использует метод `__lt__()`.
### Использование
- Поиск места вставки элемента в отсортированный список или массив.
- Эффективно для поиска диапазонов значений. Для поиска конкретных значений словари более эффективны.
- Функции поиска не сохраняют соостояние и отбрасывают результаты ключевых функций после их использования.
- Для длинных списков с дорогостоящими операциями сравнения это более эффективно, по сравнению с линейным поисков или частым обращением.
### Примеры
1\. Функция `bisect` может быть полезна для поиска в числовых таблицах. В этом примере используется поиск буквенной оценки за экзамен на основе набора упорядоченных числовых контрольных точек: от 90 и выше — «А», от 80 до 89 — «В» и так далее:
```python
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect(breakpoints, score)
    return grades[i]

[grade(score) for score in [33, 99, 77, 70, 89, 90, 100]] # ['F', 'A', 'C', 'C', 'B', 'A', 'A']
```
2\. Этот код находит индекс, в который можно вставить число 4 в отсортированный массив, чтобы сохранить порядок сортировки:
```python
arr = [1, 3, 3, 5, 7, 9]
bisect.bisect_left(arr, 4)  # 3
```


## <div id="8">8. array - Эффективные массивы числовых значений</div>
> Модуль определяет тип объекта, который может компактно представлять массив основных значений: символов, целых чисел, чисел с плавающей запятой. Массивы представляют собой типы последовательностей и ведут себя очень похоже на списки, за исключением того, что тип хранящихся в них объектов ограничен. Тип указывается во время создания объекта с помощью кода типа, который представляет собой один символ.
### Использование
- Использование меньшего количества памяти, чем обычные списки.
- Более эффективный доступ к памяти, чем в обычных списках.
- Добавление, удаление элементов более эффективно, чем в обычных списках.
- Эффективен при манипулировании большими обьемами данных.
### Примеры
```python
a = array('H', [4000, 10, 700, 22222])
```


## <div id="9">9. weakref - Слабые ссылки</div>
> Модуль позволяет создавать слабые ссылки на обьекты.
### Использование
- Реализация кэшей и отображений, содержащих большие обьекты, где желательно, чтобы большой обьект не оставался активным только потому, что он появляется в кэше или сопоставлении.
### Примеры
Например, если у вас есть несколько больших объектов двоичного изображения, вы можете захотеть связать имя с каждым. Если вы использовали словарь Python для сопоставления имен с изображениями или изображений с именами, объекты изображений оставались бы живыми только потому, что они появлялись в словарях как значения или ключи. Классы `WeakKeyDictionary` и `WeakValueDictionary`, предоставляемые модулем `weakref`, являются альтернативой, использующей слабые ссылки для создания отображений, которые не поддерживают активность объектов только потому, что они появляются в объектах сопоставления. Если, например, объект изображения является значением в a `WeakValueDictionary`, то, когда последние оставшиеся ссылки на этот объект изображения являются слабыми ссылками, содержащимися в слабых сопоставлениях, сборщик мусора может вернуть объект, а соответствующие записи в слабых сопоставлениях просто удаляются.


## <div id="10">10. types - Динамическое создание типов и имена для встроенных типов</div>
> Модуль определяет служебные функции, помогающие в динамическом создании новых типов. Предоставляет некоторые дополнительные служебные классы и функции, связанные с типами, которые недостаточно фундаментальны, чтобы быть встроенными.
### Использование
- Создание новых типов или функций.
- Использование типов для проверки типов обьектов.


## <div id="11">11. copy - Операции поверхностного и глубокого копирования</div>
> Модуль обеспечивает общие операции поверхностного и глубокого копирования, так как операторы Python не копируют обьекты, а создают привязки между целью и обьектом.
### Использование
- Создание поверхностных копий обьектов.
- Создание глубоких копий обьектов.
- Для коллекций, которые являются изменяемыми или содержат изменяемые элементы, иногда требуется копия, чтобы можно было изменить одну копию, не изменяя другую.
### Примеры
```python
original_list = [1, 2, [3, 4]]
copied_list = copy.copy(original_list)
original_list[2][0] = 999
print(original_list)  # [1, 2, [999, 4]]
print(copied_list)    # [1, 2, [999, 4]]
```
```python
original_list = [1, 2, [3, 4]]
deep_copied_list = copy.deepcopy(original_list)
original_list[2][0] = 999
print(original_list)      # [1, 2, [999, 4]]
print(deep_copied_list)   # [1, 2, [3, 4]]
```


## <div id="12">12. pprint - Симпатичный принтер данных</div>
> Модуль предоставляет "красивый" вывода структур данных, таких как словари и списки. Он предоставляет функциональность для форматирования и вывода этих данных в более читаемом виде, что особенно полезно при отладке или выводе информации для пользователя.


## <div id="13">13. reprlib - Альтернативная реализация repr()</div>
> Модуль предоставляет средства для создания представлений обьектов с ограничениями на размер результирующих строк. Предоставляет версию repr() для сокращенного отображения больших или глубоко вложенных контейнеров
### Использование
- Используется в отладчике.
- Создание краткого представления обьектав отладочных сообщениях, логах.
### Примеры
```python
reprlib.repr(set('supercalifragilisticexpialidocious'))
```

## <div id="14">14. enum - Поддержка перечислений</div>
> Модуль используется для создания перечислений, что упрощает работу с набором именованных констант. Перечисления предоставляют более понятные и читаемые способы представления данных, которые имеют фиксированных набор значений.
### Использование
- Создание перечислений.
- Работа с опциями конфигурации, статусами, цветами.
### Примеры
```python
class Color(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```


## <div id="15">15. graphlib - Функционал для работы с графоподобными структурами</div>
> Модуль предоставляет функции для работы с графами. Включает инструменты для создания и манипуляций направленными и ненаправленными графами.
### Использование
- Топологическая сортировка для направленных ациклических графов. Полезно при работе с зависимостями между задачами.
- Преобразования направленного ациклического графа в древовидную структуру.
- Определение наличия циклов в графе.
### Примеры
```python
graph = {'a': {'b', 'c'}, 'b': {'d'}, 'c': {'d'}, 'd': {}}

ts = graphlib.TopologicalSorter(graph)
sorted_nodes = list(ts.static_order())

print("Topologically sorted nodes:", sorted_nodes)
```