export COMPOSE_FILE=local.yml

echo:
	@echo "Hi docker!"

new:
	@docker-compose run django django-admin startproject config .

status:
	@docker-compose ps

install:
	@docker-compose build

start:
	@docker-compose up -d
	@docker-compose ps
	@docker-compose rm -f -s django
	@docker-compose run --rm --service-ports django

stop:
	@docker-compose down

fix:
	@sudo chown -R ${USER}:${USER} .

purge:
	@docker-compose down --volumes

logs:
	@docker-compose logs --follow

django:
	@docker-compose run --rm django ${CMD}

makemigrations:
	@make CMD='python manage.py makemigrations' django

migrate:
	@make CMD='python manage.py migrate' django

createsuperuser:
	@make CMD='python manage.py createsuperuser' django

app:
	@make CMD='django-admin startapp template' django
