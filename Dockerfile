FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN cp contrib/env-sample .env \
    && python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py collectstatic --no-input \
    && python manage.py test
