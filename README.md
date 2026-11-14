# FastAPI Kubernetes Deployment

A FastAPI application with complete Kubernetes manifests, readiness/liveness probes, resource limits, and a GitHub Actions CI/CD pipeline for automated Docker image builds and deployment.

## 🚀 Features

- **Kubernetes Ready** — Deployment and Service manifests included
- **Health Probes** — Readiness and liveness probes configured
- **Resource Management** — CPU/memory requests and limits defined
- **CI/CD Pipeline** — GitHub Actions workflow for Docker build & push
- **Horizontal Scaling** — Runs with 2 replicas by default
- **Environment Configuration** — Service name and environment via env vars

## 📁 Project Structure

```
.
├── app.py                        # FastAPI application
├── Dockerfile                    # Container build instructions
├── requirements.txt              # Python dependencies
├── deployment.yaml               # Kubernetes Deployment manifest
├── service.yaml                  # Kubernetes Service manifest
└── .github/
    └── workflows/
        └── ci-cd.yaml            # GitHub Actions pipeline
```

## 🛠️ Tech Stack

- **Python 3.9** — Runtime
- **FastAPI** — API framework
- **Kubernetes** — Container orchestration
- **Docker** — Containerization
- **GitHub Actions** — CI/CD automation

## ⚡ Quick Start

### 1. Build the Docker Image

```bash
docker build -t power-health-api:latest .
```

### 2. Deploy to Kubernetes

```bash
# Apply deployment (2 replicas)
kubectl apply -f deployment.yaml

# Apply service (NodePort)
kubectl apply -f service.yaml

# Check status
kubectl get pods -l app=power-health-api
kubectl get svc power-health-api
```

### 3. Test the API

```bash
# Get the NodePort
NODE_PORT=$(kubectl get svc power-health-api -o jsonpath='{.spec.ports[0].nodePort}')

# Test endpoints
curl http://localhost:$NODE_PORT/
curl http://localhost:$NODE_PORT/health
curl http://localhost:$NODE_PORT/readings
```

## 📖 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Service info (name + environment) |
| GET | `/health` | Health check for K8s probes |
| GET | `/readings` | Simulated equipment readings |

## ☸️ Kubernetes Configuration

### Deployment Highlights

| Setting | Value |
|---------|-------|
| Replicas | 2 |
| Image Pull Policy | IfNotPresent |
| Readiness Probe | `GET /health` every 5s (initial delay: 3s) |
| Liveness Probe | `GET /health` every 10s (initial delay: 10s) |
| CPU Request / Limit | 100m / 500m |
| Memory Request / Limit | 64Mi / 256Mi |

### Service

- **Type**: NodePort
- **Port**: 8080 → 8000 (container)

## 🔄 CI/CD Pipeline (GitHub Actions)

The included workflow runs on every push to `main`:

1. **Checkout** — Pulls the latest code
2. **Docker Login** — Authenticates to Docker Hub
3. **Buildx Setup** — Enables advanced Docker builds
4. **Build & Push** — Builds the image and pushes to registry

### Required GitHub Secrets

| Secret | Description |
|--------|-------------|
| `DOCKER_USERNAME` | Docker Hub username |
| `DOCKER_PASSWORD` | Docker Hub password/token |

> Update the image tag in the workflow (`your-dockerhub-username/your-app-name:latest`) with your actual Docker Hub repository.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
