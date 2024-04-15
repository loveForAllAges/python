## <a id="setattr">setattr(object, name, value)</a>
Аналог getattr(). Принимает обьект, строку, произвольное значение. Присваивает значение атрибуту.
## <a id="slice">class slice(start, stop, step=None)</a>
Возвращает slice обьект, представляющий set индексов заданным `range(start, stop, step)`. 
## <a id="sorted">sorted(iterable, /, *, key=None, reverse=False)</a>
Возвращает новый отсортированный список из элементов iterable. key - функция для извлечения ключа сравнения из каждого элемента в итерации, reverse - производить ли обратную сортировку.
## <a id="staticmethod">@staticmethod</a>
Преобразует метод в статический метод. Статический метод не получает неявного первого аргумента:
```python
class C:
    @staticmethod
    def f(arg1, arg2, argN): pass


def regular_function(): pass

class C:
    method = staticmethod(regular_function)
```
## <a id="str">class str(object=b'', encoding='utf-8', errors='strict')</a>
Возвращает обьект str.
## <a id="sum">sum(iterable, /, start=0)</a>
Возвращает сумму полученных обьектов.
## <a id="super">class super(type, object_or_type=None)</a>
Возвращает прокси-обьект, который делегирует вызовы методом родительскому или родственному классу type. object_or_type - порядок разрешения метода для поиска. Используется для ссылки на родительские классы. не называя из явно или для поддержки совмесного множественного наследования в динамической среде выполения.
## <a id="tuple">class tuple(iterable)</a>
Неизменяемый тип последовательности.
## <a id="type">class type(name, bases, dict, **kwds)</a>
Возвращает тип обьекта (object.\_\_class__).
## <a id="vars">vars(object)</a>
Возвращает \_\_dict__ атрибут.
## <a id="zip">zip(*iterables, strict=False)</a>
Возвращает итератор кортежей, где i-й кортеж содержит i-й элемент из каждой итерации аргументов. Превращает строки в столбцы, а столбцы в строки. Если итерации имеют одинаковую длину, то рекомендуется применить strict=True:
```python
>>> list(zip(range(3), ['fee', 'fi', 'fo', 'fum']))
[(0, 'fee'), (1, 'fi'), (2, 'fo')]
```
## \_\_import__<a id="import">\_\_import__(name, globals=None, locals=None, fromlist=(), level=0)</a>
Вызывается оператором import.