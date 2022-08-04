# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Makefile](#makefile)
- [Django App Dockerfile](#django-app-dockerfile)
- [Nginx Dockerfile](#nginx-dockerfile)
- [Docker Compose](#docker-compose)
- [Core Django Settings](#core-django-settings)

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

I seperate the prod and dev environments. [config_prod.py](./settings/config_prod.py) file is being used for prod environments and [config_prod.py](./settings/config_dev.py) for dev environments. We need to implement the lines in [settings.py](./settings/settings.py) file to use these seperated environments.- [Introduction](#introduction)
