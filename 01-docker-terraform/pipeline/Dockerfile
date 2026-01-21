# always start with a FROM with the base image of the container
FROM python:3.13.11-slim

# this copy command pulls the uv binary from the uv image container and places it in /bin/uv in this image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# create a the working directory for the container
WORKDIR /code

# tell the container to use the virtual environment located in .venv
ENV PATH="/code/.venv/bin:$PATH"

# copy the dependency files to the working directory
COPY pyproject.toml .python-version uv.lock ingest_data.py .

# run the command to install dependencies
RUN uv sync --locked

# run the pipeline using uv
ENTRYPOINT ["python", "ingest_data.py"]

