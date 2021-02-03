FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD motdepasse
ENV MYSQL_DATABASE classicmodels
ENV MYSQL_USER elisa
ENV MYSQL_PASSWORD pass123

EXPOSE 3306

COPY bdd.sql /docker-entrypoint-initdb.d