#!/bin/bash

echo "Setting up the HealthApp environment before running the app"

# source env/bin/activate

# Both commands below will export the env variables from db_test.env, but only in the context of the execution shell
eval "$(cat ./db_test.env)"
# source db_test.env

printenv | grep DB