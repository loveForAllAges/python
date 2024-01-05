# Встроенные функции

1. [abs](#abs)
2. [aiter](#aiter)
3. [all](#all)
4. [anext](#anext)
5. [any](#any)
6. [ascii](#ascii)
7. [bin](#bin)
8. [bool](#bool)
9. [breakpoint](#breakpoint)
10. [bytearray](#bytearray)
11. [bytes](#bytes)
12. [callable](#callable)
13. [chr](#chr)
14. [@classmethod](#classmethod)
15. [compile](#compile)
16. [complex](#complex)
17. [delattr](#delattr)
18. [dict](#dict)
19. [dir](#dir)
20. [divmod](#divmod)
21. [enumerate](#enumerate)
22. [eval](#eval)
23. [exec](#exec)
24. [filter](#filter)
25. [float](#float)
26. [format](#format)
27. [frozenset](#frozenset)
28. [getattr](#getattr)
29. [globals](#globals)
30. [hasattr](#hasattr)
31. [hash](#hash)
32. [help](#help)
33. [hex](#hex)
34. [id](#id)
35. [input](#input)
36. [int](#int)
37. [isinstance](#isinstance)
38. [issubclass](#issubclass)
39. [iter](#iter)
40. [len](#len)
41. [list](#list)
42. [locals](#locals)
43. [map](#map)
44. [max](#max)
45. [memoryview](#memoryview)
46. [min](#min)
47. [next](#next)
48. [object](#object)
49. [oct](#oct)
50. [open](#open)
51. [ord](#ord)
52. [pow](#pow)
53. [print](#print)
54. [property](#property)
55. [@getter](#getter)
56. [@setter](#setter)
57. [@deleter](#deleter)
58. [range](#range)
59. [repr](#repr)
60. [reversed](#reversed)
61. [round](#round)
62. [set](#set)
63. [setattr](#setattr)
64. [slice](#slice)
65. [sorted](#sorted)
66. [@staticmethod](#staticmethod)
67. [str](#str)
68. [sum](#sum)
69. [super](#super)
70. [tuple](#tuple)
71. [type](#type)
72. [vars](#vars)
73. [zip](#zip)
74. [\_\_import__](#import)

## <a id="abs">abs(x)</a>
Возвращает абсолютное значение числа. Аргумент может быть целым числом, числом с плавающей запятой или объектом, реализующим \_\_abs__(). Если аргумент является комплексным числом, возвращается его величина.
## <a id="aiter">aiter(async_iterable)</a>
Возвращает асинхронный итератор для асинхронной итерации. Эквивалент звонка x.\_\_aiter__(). В отличие от iter(), aiter()не имеет варианта с двумя аргументами:
## <a id="all">all(iterable)</a>
Возвращает значение True, если все элементы итерируемого объекта истинны (или если итерируемый объект пуст):
## <a id="anext">anext(async_iterator)</a>
При ожидании вернуть следующий элемент из заданного асинхронного итератора или значения по умолчанию, если он задан и итератор исчерпан. Это асинхронный вариант встроенной функции next(), который ведет себя аналогично.
## <a id="any">any(iterable)</a>
Возвращает значение True, если какой-либо элемент итерируемого объекта имеет значение true. Если итерируемый объект пуст, верните False.
## <a id="ascii">any(object)</a>
Возвращает строку, содержащую печатное представление объекта, но экранирует символы, отличные от ASCII.
## <a id="bin">bin(x)</a>
Преобразует целое число в двоичную строку с префиксом «0b».
## <a id="bool">class bool(x=False)</a>
Возвращает логическое значение. Если x имеет значение false или опущено, возвращается False; в противном случае он возвращает True. Является подклассом int.
## <a id="breakpoint">breakpoint(*args, **kws)</a>
Отправляет в отладчик на месте вызова.
## <a id="bytearray">class bytearray(source)</a>
Представляет собой изменяемую последовательность целых чисел в диапазоне 0 <= x < 256. От типа bytes отличается только тем, что является изменяемым.
## <a id="bytes">class bytes(source)</a>
Возвращает новый объект «байты», который представляет собой неизменяемую последовательность целых чисел в диапазоне 0 <= x < 256.
## <a id="callable">class callable(object)</a>
Возвращает True, если object вызываемый, иначе False. Классы являются вызываемыми (вызов класса возвращает новый экземпляр); экземпляры являются вызываемыми, если их класс имеет \_\_call__() метод.
## <a id="chr">chr(i)</a>
Возвращает строку, являющуюся символом Юникода. Допустимый диапазон аргумента — от 0 до 1 114 111 (0x10FFFF в системе счисления 16).
## <a id="classmethod">@classmethod</a>
Используется, когда нужно получить методы, не относящиеся к какому-либо конкретному экземпляру, но привязанные к классу. Можно переопределить дочерними классами. Получает класс в качестве неявного первого аргумента, точно так же, как обычный метод экземпляра получает экземпляр. Это означает, что можно использовать класс и его свойства внутри этого метода, а не конкретного экземпляра.
```python
class C:
    @classmethod
    def f(cls, arg1, arg2):
        pass
C.f()
```
## <a id="compile">compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)</a>
Возвращает переданный, в качестве аргумента источник, в виде объекта кода, готового к выполнению. Объекты кода, полученные в результате выполнения функции compile() могут быть выполнены с помощью exec() или eval():
```python
x = compile('x = 1\nz = x + 5\nprint(z)', 'test', 'exec')
exec(x)
```
## <a id="complex">class complex(real=0, imag=0)</a>
Возвращает комплексное число со значением вещественное + imag *1j или преобразует строку или число в комплексное число. Если первый параметр является строкой, он будет интерпретироваться как комплексное число, и функцию необходимо вызывать без второго параметра. Второй параметр никогда не может быть строкой. Каждый аргумент может иметь любой числовой тип (включая комплексный). Если imag опущен, по умолчанию он равен нулю, а конструктор выполняет числовое преобразование, например int и float. Если оба аргумента опущены, возвращается 0j.
## <a id="delattr">class delattr(object, name)</a>
Аргументами являются объект и строка. Строка должна быть именем одного из атрибутов объекта. Функция удаляет именованный атрибут, если объект это позволяет. Например, delattr(x, 'foobar') равно del x.foobar.
## <a id="dict">class dict(**kwarg)</a>
Создает новый словарь.
## <a id="dir">class dir(object)</a>
Возвращает список имен в текущей локальной области или список допустимых атрибутов для обьекта. Если у объекта есть метод с именем \_\_dir__(), этот метод будет вызван и должен вернуть список атрибутов.
## <a id="divmod">class divmod(a, b)</a>
Возвращает пару частное-остаток от деления аргументов.
## <a id="enumerate">class enumerate(iterable, start=0)</a>
Возвращает перечисляемый объект. iterable должен быть последовательностью, итератором или каким-либо другим объектом, поддерживающим итерацию. Метод \_\_next__()итератора, возвращаемый, enumerate() возвращает кортеж, содержащий счетчик (от начала, который по умолчанию равен 0) и значения, полученные в результате итерации по iterable. Эквивалентно:
```python
def enumerate(iterable, start=0):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1
```
## eval
## exec
## filter
## float
## format
## frozenset
## getattr
## globals
## hasattr
## hash
## help
## hex
## id
## input
## int
## isinstance
## issubclass
## iter
## len
## list
## locals
## map
## max
## memoryview
## min
## next
## object
## oct
## open
## ord
## pow
## print
## property
## @getter
## @setter
## @deleter
## range
## repr
## reversed
## round
## set
## setattr
## slice
## sorted
## @staticmethod
## str
## sum
## super
## tuple
## type
## vars
## zip
## \_\_import__