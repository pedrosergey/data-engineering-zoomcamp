# Module 2: Workflow Orchestration

This module focuses on workflow orchestration for data pipelines using Kestra, along with containerized supporting services for local development.

## 📂 What's in this module

### [docker-compose.yaml](docker-compose.yaml)
Multi-service local environment for orchestration and data services:
- PostgreSQL for `ny_taxi` data
- pgAdmin for database exploration
- PostgreSQL for Kestra metadata and queue
- Kestra server in standalone mode
- Persistent volumes for databases and Kestra storage

**Key concepts**: Orchestration runtime, service dependencies, Docker Compose networking, persistent storage

### [pyproject.toml](pyproject.toml)
Python project configuration for local tooling used in the module.

### [notes.md](notes.md)
Personal notes and learnings from the module.

## 🎯 Learning objectives

By completing this module, you'll be able to:
- Run an orchestration platform locally with Docker Compose
- Configure Kestra with a PostgreSQL backend
- Understand the role of scheduler, queue, and storage in workflow orchestration
- Connect orchestration workflows with data services
- Manage local environment configuration for reproducible runs

## 🚀 Getting started

1. **Start services**

```bash
docker compose up -d
```

2. **Access tools**
- Kestra UI: `http://localhost:8080`
- pgAdmin: `http://localhost:8085`
- PostgreSQL (`ny_taxi`): `localhost:5432`

3. **Stop services**

```bash
docker compose down
```

## 📚 Prerequisites

- Docker and Docker Compose installed
- Basic understanding of data pipelines and SQL
- Optional: Python 3.13+ and `uv` for local Python tooling

## 🔐 Security notes

- Do not commit secret files (`.env*`, service account credentials)
- Use local-only credentials for development
- Rotate credentials if they are exposed accidentally

---

💡 **Tip**: Keep orchestration config and credentials separated so workflows stay portable across local and cloud environments.
