#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username postgres --dbname application <<-EOSQL
    CREATE TABLE posts (id serial PRIMARY KEY, postdata varchar (150) NOT NULL, date_added date DEFAULT CURRENT_TIMESTAMP);
EOSQL