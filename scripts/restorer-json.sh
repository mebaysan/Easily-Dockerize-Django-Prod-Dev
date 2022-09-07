#! /bin/bash

# to use this script, you need to pass the latest (or wanted backup file) as an argument without .json.gz name
# ./restorer.sh /opt/baysan_database_backup/2022-09-07-18-23-22

CONTAINER_NAME=baysan_database

docker container exec $CONTAINER_NAME mkdir backup

gzip -d /opt/$CONTAINER_NAME_backup/$1.json.gz

docker cp /opt/$CONTAINER_NAME_backup/$1.json $CONTAINER_NAME:/app/backup/

docker exec -it $CONTAINER_NAME python manage.py loaddata backup/$1.json