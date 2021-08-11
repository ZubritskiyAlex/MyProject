FROM python:3.8.3-alpine
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /MyProject
WORKDIR /MyProject
ADD requirements.txt /MyProject/
# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip3 install --upgrade pip && pip install -r requirements.txt
ADD . /MyProject/


