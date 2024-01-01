# Документация по ЯП Python
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