
# 🚀 FastAPI + Docker + CircleCI + Helm + Kubernetes

A production-ready FastAPI application fully containerized with Docker and integrated into an automated **CI/CD pipeline using CircleCI**.
The project includes **Pytest testing**, **DockerHub publishing**, and a complete **Kubernetes deployment workflow** using a **Helm chart**, **NGINX Ingress**, **TLS/SSL**, and **readiness/liveness probes**.

---

# ✨ Features Overview

### 🔧 Application & Development

* Lightweight **FastAPI** application
* `/health` endpoint for health checks and probes
* **Dockerfile** + **Docker Compose** for local development

### 🧪 Testing

* Fully automated test suite using **Pytest**
* CI pipeline verifies health endpoint before deployment

### 🚀 CI/CD (CircleCI)

* Automatic:

  * Dependency installation
  * Pytest execution
  * Docker image build
  * Local container health test
  * DockerHub login and image push

### ☸️ Kubernetes Deployment

* Complete Kubernetes manifests
* NGINX Ingress for domain routing (`fastapi.local`)
* Readiness and Liveness probes enabled
* HTTPS support with self-signed TLS certificates

### 🆕 Helm Chart (Production-Ready)

A fully parameterized Helm chart for deploying the application to Kubernetes with customizable settings for:

* replicaCount
* image repo/tag
* NodePort configuration
* Ingress + TLS
* Autoscaling toggle
* Probe configuration

---

# 📦 Project Structure

```
fastapi-circleci-demo/
│── main.py
│── Dockerfile
│── docker-compose.yml
│── requirements.txt
│── tests/
│   └── test_app.py
│── fastapi-chart/     ← Helm Chart (new)
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
│       ├── deployment.yaml
│       ├── service.yaml
│       ├── ingress.yaml
│       └── NOTES.txt
│── certs/             (ignored in Git)
│── .circleci/
│   └── config.yml
│── README.md
```

---

# 🛠 Helm Chart Deployment

### 1. Install the chart

```
helm install fastapi ./fastapi-chart
```

### 2. Upgrade after updates

```
helm upgrade fastapi ./fastapi-chart
```

### 3. Uninstall

```
helm uninstall fastapi
```

### 4. View release

```
helm list
```

---

# 📊 Kubernetes Readiness & Liveness Probes

The application exposes:

```
/health
```

This endpoint is used for:

* Readiness Probe (traffic only when app is ready)
* Liveness Probe (automatic restart on app failure)
* CI/CD health verification
* Docker health testing

The probe configuration is fully customizable in `values.yaml`.

---

# 🔐 TLS/SSL Setup (Minikube + Ingress)

### Generate self-signed certificate

```
openssl req -x509 -newkey rsa:4096 -sha256 -nodes \
  -keyout certs/fastapi.local.key \
  -out certs/fastapi.local.crt \
  -days 365 \
  -subj "/CN=fastapi.local"
```

### Create Kubernetes TLS secret

```
kubectl create secret tls fastapi-tls \
  --cert=certs/fastapi.local.crt \
  --key=certs/fastapi.local.key
```

### Add host entry

```
127.0.0.1   fastapi.local
```

When Ingress is enabled, the application becomes available at:

```
https://fastapi.local
```

---

# 🔄 CircleCI Pipeline

The CircleCI workflow performs:

1. Project checkout
2. Dependency installation
3. Pytest execution
4. Docker image build
5. Containerized health check
6. DockerHub authentication
7. Docker image push

This ensures that the Kubernetes cluster always pulls the latest verified image.

---

# 🧪 Running Tests Locally

```
pip install -r requirements.txt
pytest -v
```

---

# 🐳 Local Development with Docker Compose

```
docker compose up --build
```

---

# ☸️ Kubernetes Deployment Options

### Option 1 — **Preferred**: Helm

```
helm install fastapi ./fastapi-chart
```

### Option 2 — Raw YAML (if needed)

```
kubectl apply -f k8s/
```

---

# 📌 Summary

This project provides a complete, production-ready setup including:

* FastAPI application
* Docker & Docker Compose
* Automated CI/CD via CircleCI
* DockerHub publishing
* Helm-based Kubernetes deployment
* Readiness & Liveness Probes
* NGINX Ingress
* TLS/SSL
* Domain-based routing

It is designed to be **scalable**, **automated**, and **cloud-ready**.

---
