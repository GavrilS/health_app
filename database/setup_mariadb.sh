#!/bin/bash

# Setting up mariadb with docker
# Pulling the image
echo "To look for a specific MariaDB image run the command:"
echo "  docker search mariadb"
echo "Pick a version and then run:"
echo "  docker pull mariadb:<version>"
echo "Or to get the latest just run:"
echo "  docker pull mariadb"
echo "************"
echo ""

# Running a container
echo "To run a container use the command:"
echo "  docker run --name mariadb -e MYSQL_ROOT_PASSWORD=mariadb -p 3306:3306 -d mariadb"
# - name - the name for the container
# - e - specifies the password for the root user
# - p - sets a mapping of the port of the container and the host
# - d - run in detach mode
# - at the end we specify the image to be user
