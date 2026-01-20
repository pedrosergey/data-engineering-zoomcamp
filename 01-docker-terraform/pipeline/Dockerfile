# always start with a FROM with the base image of the container
FROM python:3.13.11-slim

# this copy command pulls the uv binary from the uv image container and places it in /bin/uv in this image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# create a the working directory for the container
WORKDIR /code

# copy the dependency files to the working directory
COPY pyproject.toml .python-version uv.lock pipeline.py .

# run the command to install dependencies
RUN uv sync --locked

# run the pipeline using uv
ENTRYPOINT ["uv", "run", "python", "pipeline.py"]

