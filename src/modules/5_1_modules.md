# Обработка текста
1. [string - Общие строковые операции](#1)
2. [re - Операции с регулярными выражениями](#2)
3. [difflib - Помощники для вычисления дельт](#3)
4. [textwrap - Перенос и заполнение текста](#4)
5. [unicodedata - База данных Юникод](#5)
6. [stringprep - Подготовка интернет-строки](#6)
7. [readline - Интерфейс чтения GNU](#7)
8. [rlcompleter - Функция завершения для строки чтения GNU](#8)


## <div id="1">1. string - Общие строковые операции</div>
Предоставляет возможность выполнять сложные замены переменных и форматирование значений с помощью `format()` метода. Класс `Formatter` позволяет создавать и настраивать собственные способы форматирования строк. Класс `Template` принимает сроку и позволяет интернационализировать ее.
#### Константы
##### string.ascii_letters
Обьединяет `ascii_lowercase` и `ascii_lowercase`.
##### string.ascii_lowercase
Строка `'abcdefghijklmnopqrstuvwxyz'`.
##### string.ascii_uppercase
Строка `'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`.
##### string.digits
Строка `'0123456789'`.
##### string.hexdigits
Строка `'0123456789abcdefABCDEF'`.
##### string.octdigits
Строка `'01234567'`.
##### string.punctuation
Строка символов пунктуации ASCII `'!"#$%&'()*+,-./:;<=>?@[\]^_{|}~'`.
##### string.printable
Строка печатуемых символов ASCII (`gidits`, `ascii_letters`, `punctuation`, `whitespace`).
##### string.whitespace
Строка пробелов ASCII (пробелы, табуляция, перевод строки, возврат, перевод страницы, вертикальная табуляция).


## <div id="2">2. re - Операции с регулярными выражениями</div>
Предоставляет операции сопоставления регулярных выражений (как в Perl). Модуль определяет несколько функций, констант, исключений.
#### Функции
##### re.compile(pattern, flags=0)
Компилирует шаблон регулярного выражения в обьект регулярного выражения, который можно использовать с помощью `match()`, `search()`.
##### re.search(pattern, string, flags=0)
Сканирует `string` в поисках первого места, где `pattern` совпадает и возвращает `Match`, иначе `None`.
##### re.match(pattern, string, flags=0)
Если ноль или более символов в начале `string` соответствуют `pattern`, то возвращает `Match`, иначе `None`.
##### re.fullmatch(pattern, string, flags=0)
Если `string` полностью соответствует `pattern`, то возвращается `Match`, иначе `None`.
##### re.split(pattern, string, maxsplit=0, flags=0)
Разделяет `string` по `pattern` `maxsplit` раз и возвращает список.
##### re.findall(pattern, string, flags=0)
Возвращает все совпадения `pattern` в `string` в виде списка строк или кортежей.
##### re.finditer(pattern, string, flags=0)
Возвращает итератор, возвращающий `Match` обьекты по всем совпадениям `pattern` в `string`.
##### re.sub(pattern, repl, string, count=0, flags=0)
Возвращает строку, полученную путем замены крайних левых вхождений `pattern` в `string` на `repl`.
##### re.subn(pattern, repl, string, count=0, flags=0)
Выполняет то же, что и `sub()`, но возвращает кортеж.
##### re.escape(pattern)
Экранирует специальные символы в `pattern`.
##### re.purge()
Очищает кеш регулярных выражений.


## <div id="3">3. difflib - Помощники для вычисления дельт</div>
Предоставляет классы и функции для сравнения последовательностей.
#### Классы и функции
##### class difflib.SequenceMatcher
Сравнивает пары при условии, что элементы последовательности хешируемы.
```python
>>> s1 = 'Hello world!'
>>> s2 = 'Hello peace!'
>>> d = difflib.SequenceMatcher(None, s1, s2)
>>> d.ratio()
0.5833333333333334
>>> d.get_opcodes()
[('equal', 0, 6, 0, 6), ('replace', 6, 11, 6, 11), ('equal', 11, 12, 11, 12)]
>>> d.get_matching_blocks()
[Match(a=0, b=0, size=6), Match(a=11, b=11, size=1), Match(a=12, b=12, size=0)]
```
##### class difflib.Differ
Сравнивает последовательность строк текста и создания удобочитаемых различий дельт.
Каждая строка начинается с буквенного кода:
Код | Значение
--- | ---
`- ` | строка, уникальная для последовательности 1
`+ ` | строка, уникальная для последовательности 2
` ` | линия, общая для обеих последовательностей
`? ` | строка отсутствует ни в одной входной последовательности


```python
>>> s1 = 'Hello world!'
>>> s2 = 'Hello peace!'
>>> d = difflib.Differ()
>>> d.compare(s1, s2)
>>> ''.join(d.compare(s1, s2))
'  H  e  l  l  o   - w- o- r- l- d+ p+ e+ a+ c+ e  !'
```
##### class difflib.HtmlDiff
Создает HTML-таблицу, показывающую параллельное, построчное сравнение текста с выделением межстрочных и внутристрочных интервалов.
__\_\_init\_\_(tabsize=8, wrapcolumn=None, linejunk=None, charjunk=IS_CHARACTER_JUNK)__ - инициализирует HtmlDiff.  `tabsize` - расстояние между позициями табуляции, `wrapcolumn` - номер столбца, в котором строки развываются и переносятся (по умолчанию строки не переносятся), `linejunk` и `charjunk` - ключевые слова `ndiff()`.
__make_file(fromlines, tolines, fromdesc='', todesc='', context=False, numlines=5, *, charset='utf-8')__ - сравнивает `fromlines` и `tolines` и возвращает строку HTML, содержащую таблицу с различиями. `fromdesc` и `todesc` - строки заголовков столбцов из/в файл, `context` - показывать ли контекстуальные различия или полные файлы, `numlines` - контролирует количество строк, которые отображаются перед выделением различия при использовании гиперссылок.
__make_table(fromlines, tolines, fromdesc='', todesc='', context=False, numlines=5)__ - Сравнивает `fromlines` и `tolines` и возвращает строку HTML, содержащую построчные различия с выделенными межстрочными и внутристрочными изменениями.
```python
>>> s1 = 'Hello world!'
>>> s2 = 'Hello peace!'
>>> d = difflib.HtmlDiff()
>>> d.make_file(s1, s2)
```
##### difflib.context_diff(a, b, fromfile='', tofile='', fromfiledate='', tofiledate='', n=3, lineterm='\n')
Сравнивает `a` и `b`. Возвращает генератор, генерирующий дельта-линии в формате контекстного различия (только измененные строки + несколько строк контекста).
```python
>>> s1 = 'Hello world!'
>>> s2 = 'Hello peace!'
>>> d = difflib.context_diff(s1.splitlines(), s2.splitlines())
>>> {i for i in d}
{'--- \n', '***************\n', '--- 1 ----\n', '! Hello peace!', '! Hello world!', '*** \n', '*** 1 ****\n'}
```
##### difflib.get_close_matches(word, possibilities, n=3, cutoff=0.6)
Возвращает список лучших совпадений по слову или фразе. `word` - последовательность, для которой желательны близкие совпадения, `possibilities` - список последовательностей с которыми сопоставляется `word`, `n` - максимальное количество возвращаемых близких совпадений, `cutoff` - пороговое значение схожести.
```python
>>> difflib.get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy'])
['apple', 'ape']
```
##### difflib.ndiff(a, b, linejunk=None, charjunk=IS_CHARACTER_JUNK)
Сравнивает `a` и `b`. Возвращает генератор дельта-линий. `linejunk` - функция, которая принимает строковый аргумент и возвращает `True`, если строка мусорная, иначе `False`, `charjunk` - функция, которая принимает символ и возвращает значение, если символ является мусорным, иначе `False`.
```python
>>> diff = ndiff('one\ntwo\nthree\n'.splitlines(keepends=True), 'ore\ntree\nemu\n'.splitlines(keepends=True))
>>> print(''.join(diff), end="")
- one
?  ^
+ ore
?  ^
- two
- three
?  -
+ tree
+ emu
```
##### difflib.restore(sequence, which)
Возвращает одну из двух последовательностей, сгенерировавших дельту.
```python
>>> diff = ndiff('one\ntwo\nthree\n'.splitlines(keepends=True), 'ore\ntree\nemu\n'.splitlines(keepends=True))
>>> diff = list(diff)
>>> print(''.join(restore(diff, 1)), end="")
one
two
three
>>> print(''.join(restore(diff, 2)), end="")
ore
tree
emu
```
##### difflib.unified_diff(a, b, fromfile='', tofile='', fromfiledate='', tofiledate='', n=3, lineterm='\n')
Сравнивает `a` и `b`. Возвращает генератор дельта-линий в едином формате различий.
##### difflib.diff_bytes(dfunc, a, b, fromfile=b'', tofile=b'', fromfiledate=b'', tofiledate=b'', n=3, lineterm=b'\n')
Сравнивает `a` и `b` с помощью `dfunc` (например, `unified_diff()`, `context_diff()`). Возвращает последовательность дельта-строк в формате `dfunc`. Преобразовывает все входные данные в строку.
##### difflib.IS_LINE_JUNK(line)
Возвращает `True` для игнорируемых строк. `line` игнорируется, если строка пуста или содержит один `#`.
##### difflib.IS_CHARACTER_JUNK(ch)
Возвращает `True` для игнорируемых символов. Символ `ch` игнорируется, если является пробелом или табуляцией.
##### class difflib.SequenceMatcher(isjunk=None, a='', b='', autojunk=True)
`isjunk` - функция, которая принимает элемент последовательности и возвращает `True`, если элемент является мусорным, `a` и `b` - сравниваемые последовательности, `autojunk` - отключать ли автоматическую эвристику нежелательной почты.
##### class difflib.Differ(linejunk=None, charjunk=None)
`linejunk` - функция, которая принимает один строковый аргумент и возвращает `True`, если строка является мусорной, `charjunk` - фукнция, которая принимает аргумент из одного символа и возвращает `True`, если символ является мусорным.
__compare(a, b)__ - сравнивает две последовательности строк и генерирует дельту.


## <div id="4">4. textwrap - Перенос и заполнение текста</div>
Предоставляет фукнции и класс `TextWrapper` для форматирования текста по ширине экрана или определенному количеству символов.
#### Функции
##### textwrap.wrap(text, width=70, *, initial_indent='', subsequent_indent='', expand_tabs=True, replace_whitespace=True, fix_sentence_endings=False, break_long_words=True, drop_whitespace=True, break_on_hyphens=True, tabsize=8, max_lines=None, placeholder=' [...]')
Обертывает один абзац `text`, поэтому каждая строка имеет длину не более `width`. Возвращает список выходных строк без последних символов новой строки.
##### textwrap.fill(text, width=70, *, initial_indent='', subsequent_indent='', expand_tabs=True, replace_whitespace=True, fix_sentence_endings=False, break_long_words=True, drop_whitespace=True, break_on_hyphens=True, tabsize=8, max_lines=None, placeholder=' [...]')
Обертывает один абзац в `text` и возвращает одну строку, содержащую абзац.
##### textwrap.shorten(text, width, *, fix_sentence_endings=False, break_long_words=True, break_on_hyphens=True, placeholder=' [...]')
Сворачивает и обрезает `text` по `width`.
##### textwrap.dedent(text)
Удаляет все общие начальные пробелы из каждой строки `text`.
##### textwrap.indent(text, prefix, predicate=None)
Добавляет `prefix` в начало выделенных строк `text`.


## <div id="5">5. unicodedata - База данных Юникод</div>
Предоставляет доступ к БД символов Юникода, которая определяет свойства символов для всех символов Юникода.


## <div id="6">6. stringprep - Подготовка интернет-строки</div>
Предоставляет функции, которые возвращают `True`, если параметр является частью набора.


## <div id="7">7. readline - Интерфейс чтения GNU</div>
Предоставляет функции для облегчения завершения чтения/записи файлов истории из интерпретатора.


## <div id="8">8. rlcompleter - Функция завершения для строки чтения GNU</div>
Предоставляет функцию завершения, подходящую для передачи `set_completer()` в `readline` модуль. Когда модуль импортируется на Unix платформу, автоматически создается `readline` экземпляр класса.