# Architecture

```text
Developer
   |
   v
Git / GitHub repository
   |
   v
GitHub Actions CI
   |-- Install Python dependencies
   |-- Run Pytest
   |-- Build Docker image
   |
   v
Docker image
   |
   v
Docker Compose (local deployment)
   |
   v
Flask web app :8000
   |-- GET /       -> web page
   |-- GET /health -> JSON health status
   |
   v
Monitoring: container status + logs + health endpoint
```

Note: Cloud deployment and managed database/authentication are not included in this starter template.
