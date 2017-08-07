all: install run

install:
	pip install -r requirements.txt

run:
	python dice

docker_install:
	docker-compose up -d
	docker exec -it dice_python bash -c "pip install -r requirements.txt"

docker_run:
	docker-compose up -d
	docker exec -it dice_python bash -c "python dice"

docker_bash:
	docker-compose up -d
	docker exec -it dice_python bash
