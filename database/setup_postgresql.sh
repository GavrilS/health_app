#!/bin/bash

# Install Postgresql using Docker
echo "*** Install Postgresql using Docker"
docker pull postgres
# To install a specific version of postgres, like 14.5, run:
# docker pull postgres:14.5 

# Create and run a postgresql container
echo "*** Create and run a postgresql container"
docker run -d --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgres postgres
# -d -> detached mode in the background
# --name -> assigns a name to the container
# -p maps the container's port to the host's port
# -e -> sets the password for the default postgres user
# the last bit specifies the image to be used for the container 'postgres'

# Check if the postgres container is running
echo "*** Check if the postgres container is running"
docker ps

# Connect to the PostgreSQL Database
echo "Connect to the PostgreSQL Database from the host machine with this command:"
echo "psql -h localhost -U postgres"

# Connect within docker
echo "You can also connect within docker with this command:"
echo "docker exec -it postgres psql -h localhost -U postgres"