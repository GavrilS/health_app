#!/bin/bash

echo "Setting up the HealthApp environment before running the app"

source env/bin/activate

# Both commands below will export the env variables from db_test.env, but only in the context of the execution shell
eval "$(cat ./db_test.env)"
# source db_test.env

# Get the DB hostname and export it
if [[ "$1" == "container" ]]; then
    echo "DB running within a container"
    docker start mariadb
    mariadbIP="$(sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mariadb)"
    export DB_HOST="$mariadbIP"
fi

printenv | grep DB

echo "Environment configuration completed. Running the Health App"

python3 app.py