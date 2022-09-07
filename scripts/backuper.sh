#! /bin/bash

CONTAINER_NAME=baysan_database

PG_USER=postgres

docker exec -t $CONTAINER_NAME pg_dumpall -c -U $PG_USER | gzip -9 > /opt/$CONTAINER_NAME_backup/dump_$(date +%Y-%m-%d_%H_%M_%S).sql.gz

docker exec -t $CONTAINER_NAME python manage.py dumpdata | gzip -9 > /opt/$CONTAINER_NAME_backup/dump_django_$(date +%Y-%m-%d_%H_%M_%S).json.gz