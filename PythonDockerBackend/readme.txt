


Dockerizing application:

docker run --name starbucks-mongo -d mongo

docker build -t starbucks:latest .

docker run --name starbucks-python-mongo --link starbucks-mongo:mongo -d starbucks

Using docker compose :

place db docker file under db folder

place application files under ws folder along with dockerfile and its requirements file

place dcker compose file outside these folders

pythondockerbackend
-docker compose.yml
-db
	-dockerfile
-ws
	-dockerfile
	-requiremtns
	-app files