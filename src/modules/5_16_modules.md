# Интернет-протоколы и поддержка
1. [webbrowser - Удобный контроллер веб-браузера](#1)
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


## <div id="1">1. webbrowser - Удобный контроллер веб-браузера</div>
>
### Использование
### Примеры
```python

```


## <div id="2">2. wsgiref - Утилиты WSGI и эталонная реализация</div>
>
### Использование
### Примеры
```python

```


## <div id="3">3. urllib - Модули обработки URL-адресов</div>
>
### Использование
### Примеры
```python

```
Простой модуль для доступа в Интернет, обработки интернет-протоколов и получения данных из URL адресов:
```python
from urllib.request import urlopen
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()
        if line.startswith('datetime'):
            print(line.rstrip())
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
