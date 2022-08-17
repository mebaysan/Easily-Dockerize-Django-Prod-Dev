#! /bin/bash

docker container run --name baysan_database_dev -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -v postgres_dev:/var/lib/postgresql/data -d postgres