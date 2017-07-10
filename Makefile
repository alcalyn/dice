all: install run

install:
	docker-compose up -d
	docker exec -it dice_python /bin/sh -c "pip install -r requirements.txt"

run:
	docker-compose up -d
	docker exec -it dice_python /bin/sh -c "python dice"

bash:
	docker-compose up -d
	docker exec -it dice_python /bin/sh
