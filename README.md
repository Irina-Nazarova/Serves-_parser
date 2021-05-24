# Serves-parser
A service that allows you to track changes in the number of ads in Avito for a specific search query.

### How to deploy a project

* Clone the repository to your local machine
* Create file .env and specify parameters
   
```
DEBUG='FALSE'
SECRET_KEY=<укажите secret_key>
AVITO_AUTH_KEY=Получите ключ
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgresql
POSTGRES_USER=postgresql
POSTGRES_PASSWORD=postgresql
DB_HOST=db
DB_PORT=5432
```
* Generation SECRET_KEY - you can get by [ссылке](https://djecrety.ir/).

### Starting docker-compose
```
docker-compose up 
```
```
docker ps
```

### First Start
**For the first launch**, for project functionality, go inside to the container:

```
docker exec -it <WEB CONTAINER ID> bash
```

```
python manage.py collectstatic
```

**To create a superuser:**
```
python manage.py createsuperuser
```

### Tech Stack
* [Python 3.8.5](https://www.python.org/)
* [Django 3.1.4](https://www.djangoproject.com/)
* [Docker](https://www.docker.com/)

### Автор

[Ирина Назарова](https://github.com/Irina-Nazarova)