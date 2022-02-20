# Django Rest API

## Introduction

This repository showcases a simple Django REST application, with background processing for the uploaded images.

The background task is specified in tasks.py and it runs periodically via Celery.

The POST request for saving record can be done on `https://rest-api-projectt.herokuapp.com/` and the GET request to fetch all the stored records can also be done on `https://rest-api-projectt.herokuapp.com/`.

The task is ran in batches to avoid synchronous load. To facilitate that, a Boolean field `is_cropped` is added to the Records model. Once the task is run, the `is_cropped` is set to `True`, leaving that record in the next processing batch.

```python
# in tasks.py

@shared_task
def resizing():
    uncropped_records = Records.objects.filter(is_cropped=False)
    for record in uncropped_records:
        img = Image.open(record.file.path)
        output_size = (140, 140)
        img.thumbnail(output_size)
        img.save(record.file.path)
        record.is_cropped = True
        record.save()
        print(record.is_cropped)
        return img
```

Live Project : https://rest-api-projectt.herokuapp.com/

## Installation

Requirements : Python 3

In order to run this application on your machine, you will ahve to install Python, and setup this application on a virtual environment. It is done below :

```bash
pip install virtualenv
git clone https://github.com/ishikaamittal/RestAPI
virtualenv RestAPI --python=python3
cd RestAPI
pip install -r requirements.txt

python manage.py runserver
```

## Screenshots

#### GET Request (GUI)

![GET Request (GUI)](https://i.imgur.com/DRktKfL.jpg)

#### GET Request (JSON)

![GET Request (JSON)](https://i.imgur.com/zab9iTV.jpg)

#### Error 400 Bad Request on POST

![POST Error 400](https://i.imgur.com/ItJcLZN.jpeg)

## How to run the background jobs

For background jobs, we first need to setup Redis and Celery.

```shell
wget http://download.redis.io/redis-stable.tar.gz

tar zxvf redis-stable.tar.gz
cd redis-stable
make
```

Then run redis on terminal:

```bash
redis-server
```

To trigger the background jobs :

```python
celery -A Records worker --loglevel=info
In shell:
from .celery import debug_task
debug_task.delay()

```

## Deployment

The application is deployed on Heroku via Git branch, using a Gunicorn socket, which faciliates running WSGI applications like Django.
