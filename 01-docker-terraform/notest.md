**Docker**

Docker is "stateless", so everytime that we run a Docker Image, we will get the same result. It does not matter how many changes we do while running the container, once we exit it, all the changes will be discarded. In order to this to change, we need to to modify the Docker Image.

This is not 100% true, but it is how is suposed to be. 

- Most basic docker command:
`docker run hello-world`

- Run an Ubuntu image, using -it flag to make it interactive:
`docker run -it ubuntu`

- Run a Python image, with -slim to get a smaller version: `docker run -it python:3.13.11-slim`

- Run bash inside a python container, by using the --entrypoint flag: `docker run -it --entrypoint=bash python:3.13.11-slim`

- Check exited containers: `docker ps -a`
- Get the code of the exited containers: `docker ps -aq`
- Remove those containers: `docker rm 'docker ps -aq'`

**Python**

- Version: `python -V` or `python --version`

**BASH**

- To install packages, first need to run `apt update`, and then `apt instal ...`