FROM python:3.10 AS django-static-builder
# SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app/src


COPY requirements.txt /app/src

RUN pip install -r requirements.txt
COPY . /app/src

RUN python ./manage.py collectstatic --noinput

CMD ./manage.py runserver 0.0.0.0:8080

FROM nginx:1.25.1-alpine AS front

COPY --from=django-static-builder /app/src/staticfiles /data/staticfiles






