# Интернет-протоколы и поддержка
1. [webbrowser - Контроллер веб-браузера](#1)
2. [wsgiref - Утилиты WSGI и эталонная реализация](#2)
3. [urllib - Модули обработки URL-адресов](#3)
4. [http - HTTP-модули](#4)
5. [ftplib - клиент FTP-протокола](#5)
6. [poplib - Клиент протокола POP3](#6)
7. [imaplib - Клиент протокола IMAP4](#7)
8. [smtplib - Клиент протокола SMTP](#8)
9. [uuid - Объекты UUID согласно RFC 4122](#9)
10. [socketserver - Фреймворк для сетевых серверов](#10)
11. [xmlrpc - Серверные и клиентские модули XMLRPC](#11)
12. [ipaddress - Библиотека манипуляций IPv4/IPv6](#12)


## <div id="1">1. webbrowser - Контроллер веб-браузера</div>
> Модуль предоставляет функции для открытия веб-страниц, URL-адресов, файлов в веб-браузере.
> ### Использование
- Открытие URL через веб-браузеры.
### Примеры
Открытие новой вкладки в существующем веб-браузере:
```python
webbrowser.open_new_tab('https://www.google.com/')
```
Открытие нового экземляра веб-браузера:
```python
webbrowser.open_new('https://www.google.com/')
```
Открывает URL в веб-браузере:
```python
webbrowser.open('https://www.google.com/')
```


## <div id="2">2. wsgiref - Утилиты WSGI и эталонная реализация</div>
> Модуль предоставляет классы и функции для управления переменными среды WSGI (Web Server Gateway Interface) и заголовками ответов, реализации серверов WSGI. Предоставляет демонстрационных HTTP-сервер, обслуживающих приложения WSGI. 
### Использование
- Полезен для понимания основ работы WSGI. Для реальных проектов обычно используют более продвинутые веб-серверы и фреймворки.
### Примеры
В этом примере `simple_app` - WSGI-совместимая функция, которая принимает словарь с данными окружения сервера и функцию установки статуса и заголовков ответа. Приложение возвращает содержимое ответа в виде списка байт:
```python
def simple_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain; charset=utf-8')]
    start_response(status, headers)
    return [b'Hello world']


if __name__ == '__main__':
    with make_server('', 8000, simple_app) as httpd:
        print('Запущен на порту 8000...')
        httpd.serve_forever()
```


## <div id="3">3. urllib - Модули обработки URL-адресов</div>
> Модуль предоставляет функции, исключения и классы для доступа в Интернет, обработки интернет-протоколов, получения данных из URL-адресов. Внешний модуль `requests` является интерфейсом HTTP более высокого уровня.
### Использование
- Парсинг данных из Интернета.
- Обработка URL-адресов.
- Анализ robots.txt.
### Примеры
В этом примере получается страница и возвращается обьект bytes и отображаются первые 300 байтов:
```python
with urllib.request.urlopen('http://www.python.org/') as file:
    print(file.read(300))
```
На основе предыдущего примера выводим декодированные данные:
```python
f = urllib.request.urlopen('http://www.python.org/')
print(f.read(100).decode('utf-8'))
```
Добавление заголовков:
```python
req = urllib.request.Request('http://www.example.com/')
req.add_header('Referer', 'http://www.python.org/')
r = urllib.request.urlopen(req)
```
Разбор URL для получения схемы, хоста, пути, параметров:
```python
urllib.parse.urlparse('https://www.example.com/path/page?param=value')
```


## <div id="4">4. http - HTTP-модули</div>
>
### Использование
### Примеры
```python

```


## <div id="5">5. ftplib - клиент FTP-протокола</div>
>
### Использование
### Примеры
```python

```


## <div id="6">6. poplib - Клиент протокола POP3</div>
>
### Использование
### Примеры
```python

```


## <div id="7">7. imaplib - Клиент протокола IMAP4</div>
>
### Использование
### Примеры
```python

```


## <div id="8">8. smtplib - Клиент протокола SMTP</div>
>
### Использование
### Примеры
```python

```
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


## <div id="9">9. uuid - Объекты UUID согласно RFC 4122</div>
>
### Использование
### Примеры
```python

```


## <div id="10">10. socketserver - Фреймворк для сетевых серверов</div>
>
### Использование
### Примеры
```python

```


## <div id="11">11. xmlrpc - Серверные и клиентские модули XMLRPC</div>
>
### Использование
### Примеры
```python

```


## <div id="12">12. ipaddress - Библиотека манипуляций IPv4/IPv6</div>
>
### Использование
### Примеры
```python

```
