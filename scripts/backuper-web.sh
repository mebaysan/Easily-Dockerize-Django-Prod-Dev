#! /bin/bash

CONTAINER_NAME=baysan_web

BACKUP_FOLDER=/opt/"$CONTAINER_NAME"_backup

mkdir -p $BACKUP_FOLDER

docker exec -it $CONTAINER_NAME python manage.py dumpdata | gzip -9 > $BACKUP_FOLDER/dump_django_$(date +%Y-%m-%d_%H_%M_%S).json.gz