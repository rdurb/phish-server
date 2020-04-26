FROM alpine:3.10.2
WORKDIR /phish/

ENV PS1="\u@phishing-server: \w $ "

COPY sites /phish/sites
COPY run.py /phish/

RUN apk update && apk upgrade && \
    apk add apache2 openrc python3 php bash

RUN apk add php$phpverx-apache2
RUN export phpverx=$(alpinever=$(cat /etc/alpine-release|cut -d '.' -f1);[ $alpinever -ge 9 ] && echo  7|| echo 5)

# Make python script executable
RUN chmod +x /phish/run.py

# Add apache2 to startup
RUN rc-update add apache2

# Configure httpd.conf
RUN sed -i '62s/Listen 80/Listen 3333/' /etc/apache2/httpd.conf
RUN echo "DirectoryIndex login.html" >> /etc/apache2/httpd.conf

