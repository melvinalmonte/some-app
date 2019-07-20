#!/bin/bash

mysql_user=$1
mysql_password=$2
mysql_host=$3
mysql_port=$4
database=$5

export MYSQL_USER=${mysql_user}
export MYSQL_PASSWORD=${mysql_password}
export MYSQL_HOST=${mysql_host}
export MYSQL_PORT=${mysql_port}
export DATABASE=${database}