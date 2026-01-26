# Docker: Containerized Data Pipelines

This folder contains Docker-based data engineering pipelines for ingesting and processing NYC taxi data using PostgreSQL.

## 📁 Contents

- **`docker-compose.yaml`** - Multi-container orchestration for PostgreSQL database and pgAdmin
- **`Dockerfile`** - Custom image definition for the data ingestion pipeline
- **`ingest_data.py`** - Python script that downloads and ingests NYC taxi trip data into PostgreSQL
- **`notebook.ipynb`** - Jupyter notebook for data exploration and SQL queries
- **`pyproject.toml`** - Python dependencies management (using uv)

## 🚀 Quick start

### 1. Start the database and pgAdmin

```bash
docker-compose up -d
```

This will spin up:
- **PostgreSQL** database on port 5432
- **pgAdmin** web interface on http://localhost:8080

Default credentials:
- PostgreSQL: `root` / `root`
- pgAdmin: `admin@admin.com` / `root`

### 2. Run the data ingestion pipeline

Build and run the ingestion container:

```bash
# Build the image
docker build -t taxi_ingest:v001 .

# Run the ingestion script
docker run --rm --network=01-docker-terraform_default \
  taxi_ingest:v001 \
    --user=root \
    --password=root \
    --host=pgdatabase \
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_taxi_trips \
    --url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"
```

### 3. Query the data

Connect to PostgreSQL using pgAdmin (http://localhost:8080) or using `psql`:

```bash
docker exec -it postgres psql -U root -d ny_taxi
```

Example query:
```sql
SELECT COUNT(*) FROM yellow_taxi_trips;
```

## 🔑 Key concepts

### Docker fundamentals
- **Images**: Pre-built templates for containers (e.g., `postgres:17-alpine`)
- **Containers**: Running instances of images (stateless by default)
- **Volumes**: Persist data between container restarts
- **Networks**: Allow containers to communicate with each other

### Useful commands

```bash
# List running containers
docker ps

# Check logs
docker logs postgres

# Stop all containers
docker-compose down

# Remove volumes (⚠️ deletes data)
docker-compose down -v

# Run bash in a container
docker exec -it postgres bash
```

## 📊 What this pipeline does

1. Downloads NYC taxi trip CSV data from a URL
2. Processes the data in chunks (for memory efficiency)
3. Creates a PostgreSQL table with proper schema
4. Inserts the data into the database
5. Allows querying via SQL (pgAdmin or psql)

## 🛠️ Customization

To ingest different months or datasets, change the `--url` parameter when running the ingestion script. The NYC taxi data is available at:
- [NYC TLC Trip Data](https://github.com/DataTalksClub/nyc-tlc-data/releases)

## 💡 Tips

- Use `--rm` flag when running containers to automatically clean up after exit
- Mount volumes with `-v` to share data between host and container
- Use `--network` to connect containers within the same Docker network
- Check the `docker-compose.yaml` for service names when connecting containers

---

**Next steps**: After mastering Docker, move on to the [terraform/](../terraform/) folder to learn about infrastructure as code!
