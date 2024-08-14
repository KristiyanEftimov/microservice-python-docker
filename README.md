# microservice-python-docker

Docker based solution written in Python for extraction of data from SQL tables with microservices. The endpoint of the microservice is accessed outside the container. When the data in the database is accessed, code must do some transformations with Pandas (join tables, select columns, filter columns etc.). The output from the microservice is in json format.
