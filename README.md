
# 🚀 FastAPI + Docker + CircleCI Pipeline (with DockerHub Deployment + Pytest + Health Check + Ingress)

A minimal FastAPI application fully containerized with Docker and integrated into a complete CircleCI CI/CD pipeline.
Now includes automated testing using **Pytest**, a **health check endpoint**, DockerHub deployment, Kubernetes support, and an **Ingress-based domain routing setup**.

---

## 📦 Features

* Lightweight FastAPI application
* `/health` endpoint for health checks
* Pytest-based testing
* Dockerfile for containerized deployment
* Docker Compose for local development (with `restart: "no"`)
* CircleCI pipeline for continuous integration
* Automated Docker image build, container run, and endpoint testing
* Automatic DockerHub login and image push
* Kubernetes-ready application
* Kubernetes Deployment pulling image from DockerHub
* **NGINX Ingress support for clean domain-based access (`http://fastapi.local`)**

---

## 🏗 Project Structure

```
fastapi-circleci-demo/
│── main.py
│── Dockerfile
│── docker-compose.yml
│── requirements.txt
│── tests/
│   └── test_app.py
│── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
│── .circleci/
│   └── config.yml
│── README.md
```

---

## 🔄 CI/CD Pipeline (CircleCI)

The CircleCI workflow performs:

1. Repository checkout
2. Python dependency installation
3. Running **Pytest**
4. Building Docker image
5. Running Docker container for endpoint testing
6. Testing `/` and `/health` endpoints via `curl`
7. DockerHub login
8. Pushing the image to DockerHub

Just push your code → CircleCI runs automatically.

---

## 🧪 Testing (Pytest)

Run tests locally:

```bash
pip install -r requirements.txt
pytest -v
```

---

## 🩺 Health Check Endpoint

Included `/health` endpoint is used for:

* Local health checks
* CI/CD pipeline validation
* Kubernetes readiness/liveness checks
* Ingress backend testing

---

## 📦 Updated Docker Compose (No Auto-Restart)

Run locally:

```bash
docker compose up --build
```

---

## ☸️ Kubernetes Support (DockerHub-Based Deployment)

This project includes Kubernetes manifests for:

* Deployment (pulling latest image from DockerHub)
* NodePort Service
* **NGINX Ingress for domain-based access**

  * Access the app using:

    ```
    http://fastapi.local
    http://fastapi.local/health
    ```

Apply manifests:

```bash
kubectl apply -f k8s/
```

---

## 🔐 DockerHub Deployment Setup

Add these in CircleCI:

* `DOCKERHUB_USERNAME`
* `DOCKERHUB_PASSWORD`

---

## 🎉 You're All Set

This project now includes:

✔ FastAPI
✔ Docker & Docker Compose
✔ Pytest
✔ CircleCI CI/CD
✔ DockerHub deployment
✔ Kubernetes Deployment + Service
✔ **NGINX Ingress support**
✔ Clean domain access
✔ Health check endpoint

---
