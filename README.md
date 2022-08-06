# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Makefile](#makefile)
- [Django App Dockerfile](#django-app-dockerfile)
- [Nginx Dockerfile](#nginx-dockerfile)
- [Docker Compose](#docker-compose)
- [Core Django Settings](#core-django-settings)
- [For Production](#for-production)
  - [Load Default Superuser](#load-default-superuser)
- [Default Credentials for Django Admin](#default-credentials-for-django-admin)
- [Deploy on A Real Server](#deploy-on-a-real-server)

# Introduction

I created this repo to easily dockerize Django apps. In this repo, I have my own config set-up to seperate prod and dev environments. Also, I have my pre-built `docker-compose.yml` to easily deploy my projects. You can create a Django app inside this directory to use this boilerplate.

# Makefile

In [Makefile](./Makefile) I set the commands I use often.

# Django App Dockerfile

The app's image is created by using [Dockerfile](./Dockerfile).

# Nginx Dockerfile

To set-up Nginx, we use [Dockerfile](./nginx/Dockerfile) which is located under the [nginx](./nginx/) folder. Also, [nginx.conf](./nginx/nginx.conf) file is being used for proxy.


# Docker Compose

[docker-compose.yml](.docker-compose.yml) is being used for setting up the services.

# Core Django Settings

I seperate the prod and dev environments. [config_prod.py](./settings/config_prod.py) file is being used for prod environments and [config_prod.py](./settings/config_dev.py) for dev environments. We need to implement the lines in [settings.py](./settings/settings.py) file to use these seperated environments.

# For Production

## Load Default Superuser
```
docker container exec -it baysan_web /bin/bash
>>> make loaddata
```

# Default Credentials for Django Admin

```
username: admin
password: Passw0rd!.
```


# Deploy on A Real Server

Steps:

1. Create an nginx file in `/etc/nginx/sites-available` for your web project. For example: `baysanproject`

2. Put the content below into the file you created

    ```
    server {
            # `listen` can be changed for your nginx service in docker-compose.yml
            listen 80;
            listen [::]:80;
            server_name YOUR_URL(S);
            server_name_in_redirect off;

            access_log /var/log/nginx/reverse-access.log;
            error_log /var/log/nginx/reverse-error.log;

            location / {
                proxy_set_header Client-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header Host $host;
                proxy_pass http://127.0.0.1:8080;
        }
    }
    ```

3. Create a symbolic link

    ```
        sudo ln -s /etc/nginx/sites-available/baysanproject /etc/nginx/sites-enabled
    ```