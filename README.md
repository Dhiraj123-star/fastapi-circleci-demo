
# 🚀 FastAPI + Docker + CircleCI Pipeline (DockerHub + Pytest + Health Check + K8s + Ingress + TLS/SSL)

A minimal FastAPI application fully containerized with Docker and integrated into a complete CircleCI CI/CD pipeline.
Now includes automated testing with **Pytest**, Kubernetes deployment, **NGINX Ingress**, **domain-based access**, and **HTTPS using self-signed TLS certificates**.

---

# ⭐ Core Features (Updated)

* Lightweight FastAPI application
* `/health` endpoint for readiness/liveness checks
* Pytest-based testing
* Dockerfile + Docker Compose for local development
* CircleCI CI/CD pipeline
* Automated Docker image build, run, and endpoint testing
* DockerHub login + image push
* Kubernetes-ready deployment
* Kubernetes Deployment pulling image from DockerHub
* NGINX Ingress for domain routing (`fastapi.local`)
* **HTTPS support with self-signed TLS certificate (`https://fastapi.local`)**
* TLS secret stored securely in Kubernetes
* Easy local testing via Minikube Ingress

---

# 🏗 Project Structure

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
│── certs/ (ignored in git)
│── .circleci/
│   └── config.yml
│── README.md
```

---

# 🔐 HTTPS + Self-Signed Certificate Setup (Minikube)

### 1️⃣ Create a folder for certificates (already ignored in `.gitignore`)

```
mkdir certs
```

### 2️⃣ Generate a self-signed certificate

```
openssl req -x509 -newkey rsa:4096 -sha256 -nodes \
  -keyout certs/fastapi.local.key \
  -out certs/fastapi.local.crt \
  -days 365 \
  -subj "/CN=fastapi.local"
```

### 3️⃣ Create a Kubernetes TLS secret

```
kubectl create secret tls fastapi-tls \
  --cert=certs/fastapi.local.crt \
  --key=certs/fastapi.local.key
```

### 4️⃣ Enable NGINX Ingress (important)

```
minikube addons enable ingress
```

### 5️⃣ Apply manifests

```
kubectl apply -f k8s/
```

### 6️⃣ Add host entry

```
sudo nano /etc/hosts
```

Add:

```
127.0.0.1   fastapi.local
```

### 7️⃣ Access HTTPS

```
https://fastapi.local
https://fastapi.local/health
```

(You will accept the browser trust warning because self-signed.)

---

# 🔄 CI/CD Pipeline (CircleCI)

The CircleCI workflow:

1. Checkout repository
2. Install Python dependencies
3. Run Pytest
4. Build Docker image
5. Run container and test endpoints
6. DockerHub login
7. Push image to DockerHub

Push code → pipeline runs automatically.

---

# 🧪 Testing (Pytest)

Run tests locally:

```bash
pip install -r requirements.txt
pytest -v
```

---

# 🩺 Health Check Endpoint

Used by:

* Local Docker testing
* CI/CD pipeline `curl` checks
* Kubernetes readiness/liveness probes
* Ingress backend validation

---

# 📦 Docker Compose (No Auto-Restart)

Run locally:

```bash
docker compose up --build
```

---

# ☸️ Kubernetes (Minikube) Deployment

Manifests include:

✔ Deployment
✔ Service (NodePort)
✔ Ingress (HTTP + HTTPS/TLS)
✔ TLS secret support

Apply:

```bash
kubectl apply -f k8s/
```

---

# 🔐 DockerHub Deployment Setup

Add these in CircleCI Project Settings:

* `DOCKERHUB_USERNAME`
* `DOCKERHUB_PASSWORD`

---

# 🎉 You’re All Set

This project now supports:

✔ FastAPI
✔ Docker + Docker Compose
✔ CircleCI CI/CD
✔ DockerHub deploy
✔ Pytest
✔ Kubernetes deployment
✔ NGINX Ingress
✔ **HTTPS with self-signed TLS**
✔ Clean domain-based access

---
