FROM docker.io/library/alpine:latest

RUN apk add --no-cache py3-psycopg2 py3-flask

WORKDIR /app

COPY src .

EXPOSE 5000

CMD [ "/usr/bin/flask", "run", "--host=0.0.0.0"]
