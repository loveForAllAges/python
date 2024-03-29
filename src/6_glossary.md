# Глоссарий


## Акроним SOLID
Акроним, который представляет 5 принципов ООП и проектирования.

Инициал

### S - single responsibility principle (Принцип единственной ответственности)
Класс должен иметь только одну причину для изменения, то есть каждый класс должен быть ответственен только за выполнение одной задачи.
### O - open-closed principle (Принцип открытости/закрытости)
Класс должен быть открыт для расширения, но закрыт для модификации, то есть разрешается добавлять новую функциональность через наследование, не изменяя существующий код.
### L - Liskov substitution principle (Принцип подстановки Лисков)
Обьекты базового класса должны быть заменяемы обьектами его производного класса без изменения корректности программы. Если есть обьект базового класса, то должна быть возможность заменить его обьектом производного класса и программа все равно будет работать правильно.
### I - Interface segregation principle (Принцип разделения интерфейса)
Много интерфейсов, специально предназначенных для клиентов, лучше, чем один интерфейс общего назначения. Вместо того, чтобы иметь один общий интерфейс, лучше иметь несколько более специализированных интерфейсов.
### D - Dependency Inversion principle (Принцип инверсии зависимостей)
Высокоуровневые модули не должны зависеть от низкоуровневых модулей. Оба типа модулей должны зависеть от абстракций. Также абстракции не должны зависеть от деталей, детали должны зависеть от абстракций.


## Принцип DRY
Dont repeat yourself (не повторяйся). Каждая часть знания должна иметь единственное, непротиворечивое и авторитетное представление в рамках системы.


## Акроним KISS
Keep it simple stupid (Делай проще тупица). Система работает лучше, если она остается простой, а не усложняется.


## Набор GRASP
GRASP (General Responsibility Assignment Software Patterns) - девять шаблонов проектирования ПО, который помогает определить ответственности обьектов в системе. Предоставляет рекомендации по тому, как распределить задачи и обязанности между классами и обьектами в программе для достижения более гибкой и поддерживаемой структуры кода. Список шаблонов:
### 1. Information Expert (Информационный эксперт)
Ответственность присваивается классу, который обладает необходимой информацией для выполнения задачи.
### 2. Creator (Создатель)
Класс должен быть ответственным за создание экземпляров другого класса, если мы имеем отношение "один ко многим" или "один к одному".
### 3. Controller (Контроллер)
Класс, ответственный за координацию работы других классов или обработку внешних событий.
### 4. Low Coupling (Низкая зацепление)
Минимизация зависимостей между классами, чтобы изменения в одном классе не влияли на другие.
### 5. High Cohesion (Высокая связность)
Максимизация внутренней связанности класса, чтобы его члены работали вместе для достижения общей цели.
### 6. Polymorphism (Полиморфизм)
Ответственность присваивается классу, который обеспечивает общий интерфейс для нескольких реализаций.
### 7. Pure Fabrication (Чистая выдумка)
Создание класса, который не представляет реального объекта в предметной области, но служит для улучшения структуры системы.
### 8. Indirection (Перенаправление)
Использование посредника для уменьшения зависимостей между компонентами системы.
### 9. Protected Variations (Устойчивость к изменениям)
Шаблон защищает элементы от изменения другими элементами с помощью вынесения взаимодействия в фиксированных интерфейс, через который возможно взаимодействие между элементами.


## Принцип YAGNI
YAGNI (You arent gonna need it) (Вам это не понадобится) - принцип проектирования ПО, при котором в качестве основной цели декларируется отказ от избыточной функциональности, то есть отказ добавления фукнциональности в которой нет непосредственной надобности. Другими словами, не рекомендуется писать код, который не нужен прямо сейчас, но может понадобится в будущем.

## Спагетти-код (Индусский код)
Плохо спроектированная, слабо структурированная, запутанная и трудная для полнимания программа, содержащая много операторов GOTO, исключений и других конструкций, ухудшающих структурированность. Самый распространенный антипаттерн программирования.


## Антипаттерн
Подход к решению класса часто встречающихся проблем, являющихся неэффективным, рискованным или непродуктивным.


## GOTO
GOTO - это команда, которая переводит выполнение программы на другую часть кода. Усложняет понимание и отладку кода.


## WSGI
WSGI (Web Server Gateway Interface) (Интерфейс шлюза веб-сервера) - стандартный интерфейс между ПО веб-сервера и веб-приложениями. 


## HTTP
HTTP (HyperText Transfer Protocol) (Протокол передачи гипертекста) - протокол передачи данных (особенно гипертекстовых документов, например, веб-страницы) в сети Интернет. Является протоколом без сохранения состояния (каждый запрос от клиента к серверу считается независимым и сервер не сохраняет информацию о предыдущих запросах). Работает поверх протокола TCP и использует порт 80 для обмена данными. Основой HTTP является технология клиент-сервер (предполагается существование потребителей и поставщиков). 
Основным обьектом манипуляции в HTTP является ресурс, на который указывает URI в запросе клиента. Обычно это файлы на сервере, но могут быть логические обьекты или что-то абстрактное. 
Особенность HTTP - возможность указать в запросе и ответе способ представления одного и того же ресурса по различным параметрам: формату, кодировке, языку и т.д.
Аналогичные протоколы - FTP, SMTP. Также используется протокол HTTPS.


## HTTPS
## DNS
## TCP/IP
## FTP
## Сокет
## Интерпретатор Python
## REST API
## SOAP
## RabbitMQ
## Kaffka
## Redis
## Callback
## Coroutine (Сопрограмма)
## Декоратор
## Итератор
## Лямбда
## Магический метод
Метод, который Python неявно вызывает для выполнения определенной операции над типом, например, сложения. Такие методы имеют имена, начинающиеся и заканчивающиеся двойным подчеркиванием.
## Метакласс
Класс класса. Определения классов создают имя класса, словарь классов и список базовых классов. Метакласс отвечает за принятие этих трех аргументов и создание класса. Используются для регистрации доступа к атрибутам, добавления потокобезопасности, отслеживания создания обьектов, реализации синглтонов и других задач.

