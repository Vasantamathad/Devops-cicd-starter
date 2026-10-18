# DevOps CI/CD Starter Web Application

A small Flask web application for practising Git/GitHub, automated tests with Pytest, Docker, Docker Compose, GitHub Actions, and basic health/log monitoring.

## Requirements
- Docker Desktop with its engine running
- Git (optional, for uploading to GitHub)

## Run with Docker Compose
Open a terminal in this folder and run:

```bash
docker compose up --build -d
```

Open:
- App: http://localhost:8000
- Health check: http://localhost:8000/health

Useful commands:

```bash
docker compose ps
docker compose logs -f web
docker compose down
```

## Run tests locally
Install Python 3.12 or compatible, then run:

```bash
pip install -r requirements-dev.txt
pytest -q
```

## CI workflow
The workflow at `.github/workflows/ci.yml` runs on pushes and pull requests to `main` or `master`. It installs dependencies, runs tests, and builds a Docker image. It does not publish the image or deploy to a cloud provider.

## Upload to GitHub
Create an empty repository on GitHub, then from this folder run:

```bash
git init
git add .
git commit -m "Initial DevOps CI/CD starter project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with the URL of your own repository.

## Monitoring
- `docker compose ps` shows container status.
- `docker compose logs -f web` shows application logs.
- `/health` returns JSON with the current health status.

## Scope note
This starter includes local Docker deployment and a CI workflow that tests and builds the image. Cloud deployment, image publishing, managed database, and authentication are not configured; add these if required by your internship's final rubric.
