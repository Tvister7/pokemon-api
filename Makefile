launch:
	poetry run python src

run:
	docker compose up app

run-mongo:
	docker compose up mongodb

run-shell:
	docker compose exec app /bin/bash

restart:
	docker compose restart app

down:
	docker compose down

rebuild:
	docker compose up --force-recreate --build app

build:
	docker compose build

build-no-cache:
	docker compose build --no-cache

test:
	docker compose up test
