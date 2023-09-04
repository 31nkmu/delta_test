___
# Установка


Для установки потребуются следующие инструменты:
| Инструмент | Описание |
|----------|---------|
| [Python](https://www.python.org/downloads/) |  Язык программирования |
| [Poetry](https://python-poetry.org/) |  Менеджер зависимостей |
| [Redis](https://redis.io/docs/getting-started/installation/install-redis-on-linux/) | Хранилище данных

* Склонируй репозиторий используя команду
```Bash
# клонировать через HTTPS:
$ git clone https://github.com/31nkmu/delta_test.git
# или клонировать через SSH:
$ git clone git@github.com:31nkmu/delta_test.git
$ cd delta_test
```
* Создай виртуальное окружение используя команду
```sh
$ poetry config virtualenvs.in-project true
$ poetry env use <your_python_version>
```

* Активируй виртуальное окружение
```sh
$ source .venv/bin/activate 
```

* Установи зависимости
```sh
$ poetry install
```
* Проведи миграции
```sh
$ make migrate
# создай суперпользователя
$ make createsuperuser
```
## Обычный запуск
* Запусти свой проект используя 3 терминала
###### 1
```sh
$ make run
``` 
###### 2

```sh
$ cd app
$ celery -A config worker -l info
```
###### 3

```sh
$ cd app
$ celery -A config beat
```
---

## Запуск через docker-compose
Тебе понадобятся следующие инструменты
| Инструмент | Описание |
|----------|---------|
| [Docker](https://docs.docker.com/engine/install/ubuntu/) | Докер |
| [docker-compose](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04) | Докер-композ

Создай .env файл (смотри .env.example)
```sh
touch .env
```
Создай docker/.env файл (смотри docker/.env.example)
```sh
$ touch docker/.env
```

Запусти свой проект через docker-compose
```sh
make compose-collect-up
# создание суперпользователя в контейнере
make compose-createsuperuser
```
Смотри в Makefile для удобной работы с проектом
