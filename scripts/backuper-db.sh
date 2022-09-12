#! /bin/bash

CONTAINER_NAME=baysan_database

BACKUP_FOLDER=/opt/"$CONTAINER_NAME"_backup

mkdir -p $BACKUP_FOLDER

PG_USER=postgres

docker exec -it $CONTAINER_NAME pg_dumpall -c -U $PG_USER | gzip -9 > $BACKUP_FOLDER/dump_$(date +%Y-%m-%d_%H_%M_%S).sql.gz