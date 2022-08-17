#! /bin/bash

docker exec -t baysan_database pg_dumpall -c -U postgres | gzip > /opt/baysan_database_backup/baysan_database_backup_$(date +"%Y-%m-%d_%H_%M_%S").sql.gz