# R4C - Robots for consumers

## What does this code do?
It is a blueprint for a service that keeps track of the robots produced, as well as performs some operations related to this process.

The service is aimed at satisfying the needs of three categories of users:
- Company technicians. They will send the information to
- The company's management. They will request information
- Customers. They will be sent information
___

## What features have been implemented
1) An API-endpoint was created, which receives and processes the information in JSON format. 
As a result of a web-request to this endpoint, a record appears in the database 
that reflects the information about the robot produced in the factory. In addition the validation of the input data is provided, 
for compliance with the existing models in the system.

Example of input data:

```{"model":"R2","version":"D2","created":"2022-12-31 23:59:59"}```

```{"model":"13","version":"XS","created":"2023-01-01 00:00:00"}```

```{"model":"X5","version":"LT","created":"2023-01-01 00:00:01"}```

2) Ability to download by direct link an Excel file with a summary of the robot production totals for the last week. 
 The file should include several pages, each presents information about one model, but with details by version. 

3) Simple user form for orders receiving.

4) User order processing: if the order is in the database, the user receives a delivery notification, if the order is not in the database, a daily database check is started, when the desired order appears, a reminder email is sent to the user. 

## Что делает данный код?
Это заготовка для сервиса, который ведет учет произведенных роботов,а также 
выполняет некие операции связанные с этим процессом.

Сервис нацелен на удовлетворение потребностей трёх категорий пользователей:
- Технические специалисты компании. Они будут присылать информацию
- Менеджмент компании. Они будут запрашивать информацию
- Клиенты. Им будут отправляться информация
___

## Какие фичи реализованы
1) Создан API-endpoint, принимающий и обрабатывающий информацию в формате JSON. 
В результате web-запроса на этот endpoint, в базе данных появляется запись 
отражающая информацию о произведенном на заводе роботе. Дополнительно предусмотрена валидация входных данных, 
на соответствие существующим в системе моделям.

Пример входных данных:

```{"model":"R2","version":"D2","created":"2022-12-31 23:59:59"}```

```{"model":"13","version":"XS","created":"2023-01-01 00:00:00"}```

```{"model":"X5","version":"LT","created":"2023-01-01 00:00:01"}```

2) Возможность скачать по прямой ссылке Excel-файл со сводкой по суммарным показателям производства роботов за последнюю неделю. 
 Файл должен включает в себя несколько страниц, на каждой из которых представлена информация об одной модели, но с детализацией по версии. 

3) Создана простая форма для приема заказов пользователей.

4) Обработка заказа пользователей: если заказ есть в базе данных, пользователь получает уведомление о доставке, если заказа нет в базе данных, запускается ежедневная проверка БД, когда нужный заказ появляется, пользователю отправляется письмо-напоминание. 
