#!/bin/bash

echo "THIS SCRIPT WILL HELP YOU CLEAR THE MARIADB SETUP FOR THE APP"

# Remove the MariaDB container
read -p "Do you want to remove the MariaDB container used by the application? (Y/N): " confirm
if [[ $confirm==[yY] || $confirm==[yY][eE][sS] ]]; then
    echo "Removing the container"
    sudo docker rm --force mariadb
    echo "List of available containers after attempting to remove the MariaDB container:"
    sudo docker ps -a
else
    echo "Skipping removing the container..."
fi
echo ""

# Remove the MariaDB image
read -p "Do you want to remove the MariaDB docker image from the system? (Y/N): " confirm
if [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]]; then
    echo "Clearing the docker image for MariaDB..."
    sudo docker rmi mariadb
    echo "List of available images after attempting to remove the image for MariaDB:"
    sudo docker images
else
    echo "Skipping image removal..."
fi
echo ""