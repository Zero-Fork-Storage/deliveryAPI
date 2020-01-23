#!/bin/sh
docker build -t deliveryapi-server:latest .
docker run -d -p 80:80 deliveryapi-server