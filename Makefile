ifeq ($(OS),Windows_NT)
	create_env := fsutil file createnew .env 0
else
	create_env := touch .env
endif

.PHONY: init
init:
	$(create_env)
	pip install -r requirements.txt

.PHONY: start
start:
	python manage.py runserver

.PHONY: run
run: start


.PHONY: migrate
migrate: 
	python manage.py makemigrations
	python manage.py migrate

.PHONY: clean
clean: 
	python utils/clean.py

.PHONY: freeze
freeze: 
	pip freeze > requirements.txt

.PHONY: superuser
superuser: 
	python manage.py createsuperuser

.PHONY: release
release: 
	python manage.py makemigrations
	python manage.py migrate