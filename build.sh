#!/bin/bash
echo Deleting old image...
#docker rmi -f web-server

echo Building new image...
docker build -q -t web-server .

echo Running new image...
docker run -p 80:80 -p 3333:3333 -it --rm --name phish-server web-server bash