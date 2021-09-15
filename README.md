# yamdb_final
## Описание
Финальный проект 16 спринта. 
## Установка. 
Для установки: 
* скачайте проект к себе на компьютер 
```bash
    git clone <url repo>
```
* Установите Docker 
```https://www.docker.com/get-started```
* установите виртуальное окружение
```bash
    py -m venv venv
```
* Активируйте виртуальное окружение
```bash
    source venv/Scripts/activate
```
* создайте в корне файл ```.env``` с переменными окружения
```python
    DB_NAME=<db_name> # имя базы данных
    POSTGRES_USER=<db_login> # логин для подключения к базе данных
    POSTGRES_PASSWORD=<db_password> # пароль для подключения к БД
    DB_HOST=<db> # название сервиса
    DB_PORT=<5432> # порт для подключения к БД
    SECRET_KEY=<p&l%385148kslhtyn^##a1)ilz@4zqj=rq&agdol^##zgl9(vs>
    DJANGO_DEBUG=<True>
    ALLOWED_HOSTS=<http://84.201.179.146 localhost 127.0.0.1 web>
```
* Выполните сборку образов и запуск контейнеров
```bash
    docker-compose up -d --build
```
* Выполните миграции
```bash
    docker-compose exec web python manage.py migrate --noinput
```
* Создайте пользователя
```bash
    docker-compose exec web python manage.py createsuperuser
```
* Соберите статику
```bash
    docker-compose exec web python manage.py collectstatic
```

## Используемые технологии
Python, Django, DRF, Docker, 

## Автор
Кириленко Андрей

Развернутый на сервере проект можно посмотреть <a href='http://84.201.179.146/api/v1/'>здесь</a>
![example workflow](https://github.com/Akirosan/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)