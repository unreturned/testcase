To run:

```
docker compose up -d
```

To post:

```
curl --data-urlencode 'data=hello_from_curl' 'http://localhost:8080'
```

To get data from postgres:

```
docker exec -ti testcase-database-1 psql -U postgres application -c 'SELECT * FROM posts;'
```
