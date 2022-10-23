FROM python:3.9-slim as production

ENV PYTHONUNBUFFER = 1
WORKDIR /app/

COPY requirements/prod.txt ./requirements/prod.txt
RUN pip install -r ./requirements/prod.txt

COPY manage.py ./manage.py
COPY setup.cfg ./setup.cfg
COPY hackershack_website ./hackershack_website

EXPOSE 8000

