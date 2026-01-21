# **Docker**

Docker is "stateless", so everytime that we run a Docker Image, we will get the same result. It does not matter how many changes we do while running the container, once we exit it, all the changes will be discarded. In order to this to change, we need to to modify the Docker Image.

This is not 100% true, but it is how is suposed to be. 

## 1. Basic commands

- Most basic docker command:
`docker run hello-world`

- Run an Ubuntu image, using -it flag to make it interactive:
`docker run -it ubuntu`

- Run a Python image, with -slim to get a smaller version: `docker run -it python:3.13.11-slim`

- Run bash inside a python container, by using the --entrypoint flag: `docker run -it --entrypoint=bash python:3.13.11-slim`

- Check exited containers: `docker ps -a`
- Get the code of the exited containers: `docker ps -aq`
- Remove those containers: `docker rm 'docker ps -aq'`



## 2. Advanced commands:

In order to use data from the host in the container, volumes could be used. This can be done using the -v flag, and then host_directory:container_directory

`docker run -it --entrypoint=bash -v $(pwd)/test:/app/test python:3.13.11-slim`

Example to run a command and create something to a local folder: `docker run -it -v $(pwd)/external:/../external test:pandas`

If we want to preserve some data internally in the container, we also could do something like `-v internal_volume:/internal_volume`

## 3. Create containers:

- Create a docker container (with the -t flag to give it the name): `docker build -t test:pandas .`
- After the container is created, it could be runned with: `docker run test:pandas`
- In order to make the image stateless, we need to add the `--rm` flag when running the container (it is highly recommended).

## 4. POSTGRES

A basic command to run a postgres container:
```
docker run -it --rm \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v ny_taxi_postgres_data:/var/lib/postgresql \
  -p 5432:5432 \
  postgres:18
  ```

Connect to the database using pgadmin: `uv run pgcli -h localhost -p 5432 -u root -d ny_taxi`

In order to many containers interact with each other, a network should be created: `docker network create`. And then use this network to communicate the containers `--network=...`. It is important to give names to the containers, in order to set later the host.

### 4.1 PGADMIN

To connect to a proper interface, we could use another container (remember to add the newtork tag):

```
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -v pgadmin_data:/var/lib/pgadmin \
  -p 8085:80 \
  --network=pg-network \
  dpage/pgadmin4
```

# **Python**

- Version: `python -V` or `python --version`
- To pass args to the file: `import sys` & `sys.argv`

## Virtual environment (VE):

- Install the uv, to manage VE: `pip install uv`
- Create a VE: `uv init --python 3.13`
- Run commands in the VE: `uv run python -V`
- Add dependencies to the VE (the --dev flag could be use to add only dependencies to the dev part): `uv add pandas pyarrow`
- Create a jupyter notebook sesion: `uv run jupyter notebook`
- Convert jupyter notebook into a python script: `uv run jupyter nbconvert --to=script notebook.ipynb`

# **BASH**

- To install packages, first need to run `apt update`, and then `apt instal ...`

- Change the folder path: `PS1="> "`