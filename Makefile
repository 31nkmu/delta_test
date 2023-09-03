.SILENT:

# Запуск докер контейнера в разработке

.PHONY: up
up: ## Создает и запускает контейнер
	docker-compose -f docker/docker-compose.yml up -d --build

.PHONY: down
down: ## Останавливает и удаляет контейнеры
	docker-compose -f docker/docker-compose.yml down

.PHONY: stop
stop: ## Останавливает контейнеры
	docker-compose -f docker/docker-compose.yml stop

.PHONY: start
start: ## Запускает контейнеры
	docker-compose -f docker/docker-compose.yml start

.PHONY: down-v
down-v: ## Останавливает и удаляет контейнеры вместе с зависимостями
	docker-compose -f docker/docker-compose.yml down -v

.PHONY: logs
logs: ## Просмотр логов
	docker-compose -f docker/docker-compose.yml logs -f

.PHONY: ps
ps: ## Список всех контейнеров
	docker-compose -f docker/docker-compose.yml ps -a

.PHONY: createsuperuser
createsuperuser: ## Создание суперпользователя
	docker-compose -f docker/docker-compose.yml exec web python3 manage.py createsuperuser

.PHONY: exec
exec:
	docker-compose -f docker/docker-compose.yml exec web bash



# Запуск контейнера в проадкшене

.PHONY: compose-up
compose-up: ## Создает и запускает контейнер
	docker-compose -f docker/docker-compose.prod.yml up -d --build

.PHONY: compose-down
compose-down: ## Останавливает и удаляет контейнеры
	docker-compose -f docker/docker-compose.prod.yml down

.PHONY: compose-down-v
compose-down-v: ## Останавливает и удаляет контейнеры вместе с зависимостями
	docker-compose -f docker/docker-compose.prod.yml down -v

.PHONY: compose-stop
compose-stop: ## Останавливает контейнеры
	docker-compose -f docker/docker-compose.prod.yml stop

.PHONY: compose-start
compose-start: ## Запускает контейнеры
	docker-compose -f docker/docker-compose.prod.yml start

.PHONY: compose-logs
compose-logs: ## Просмотр логов
	docker-compose -f docker/docker-compose.prod.yml logs -f

.PHONY: compose-ps
compose-ps: ## Список всех контейнеров
	docker-compose -f docker/docker-compose.prod.yml ps -a

.PHONY: compose-collect-up
compose-collect-up: compose-up ## Полный запуск контейнеров
	 docker-compose -f docker/docker-compose.prod.yml exec web python3 manage.py collectstatic

.PHONY: compose-createsuperuser
compose-createsuperuser: ## Создание суперпользователя
	docker-compose -f docker/docker-compose.prod.yml exec web python3 manage.py createsuperuser

.PHONY: compose-exec
compose-exec:
	docker-compose -f docker/docker-compose.prod.yml exec web bash


.PHONY: gunicorn
gunicorn: ## Запуск проекта через gunicorn
	poetry run gunicorn --reload --bind $(HOST):$(PORT) --workers $(WORKERS) --log-level $(LEVEL) --chdir app/ config.wsgi:application

.PHONY: migrate
migrate: ## Проведение миграций
	poetry run python3 app/manage.py migrate

.PHONY: makemigrations
makemigrations: ## Создание миграций
	poetry run python3 app/manage.py makemigrations

.PHONY: run
run: ## Запуск приложения
	poetry run python3 app/manage.py runserver

.PHONY: createsuperuser-dev
createsuperuser-dev: ## Создание суперпользователя
	poetry run python3 app/manage.py createsuperuser

