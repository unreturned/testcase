FROM docker.io/library/alpine:latest

RUN apk update; apk upgrade -a; apk add python3 py3-pip py3-psycopg2 py3-flask

WORKDIR /app

#COPY src .

EXPOSE 5000

CMD [ "/usr/bin/flask", "run", "--host=0.0.0.0"]