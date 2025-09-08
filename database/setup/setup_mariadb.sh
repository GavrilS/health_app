#!/bin/bash

# Setting up mariadb with docker
# Pulling the image
echo "To look for a specific MariaDB image run the command:"
echo "  docker search mariadb"
echo "Pick a version and then run:"
echo "  docker pull mariadb:<version>"
echo "Or to get the latest just run:"
echo "  docker pull mariadb"
read -p "Do you want to pull the latest version? (Y/N): " confirm
if [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]]; then
    echo "Pulling the latest MariaDB image"
    sudo docker pull mariadb
else
    echo "Skipping image pull..."
fi
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
read -p "Do you want to run the container with the default arguments from the command above? (Y/N): " confirm
if [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]]; then
    echo "Running the container with the default arguments"
    sudo docker run --name mariadb -e MYSQL_ROOT_PASSWORD=mariadb -p 3306:3306 -d mariadb
else
    echo "Skipping running the container..."
fi
echo "************"
echo ""

