FROM python:latest

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /code/
COPY ./ /code/
RUN chmod +x /code/django-start
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000/tcp

CMD /code/django-start
