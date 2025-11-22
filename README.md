
# 🚀 FastAPI + Docker + CircleCI Pipeline (DockerHub + Pytest + Health Check + K8s + Ingress + TLS/SSL + Probes)

A minimal FastAPI application fully containerized with Docker and integrated into a complete CircleCI CI/CD pipeline.
Now includes automated testing with **Pytest**, a Kubernetes deployment with **readiness/liveness probes**, **NGINX Ingress**, **domain-based routing**, and **HTTPS using self-signed TLS certificates**.

---

# ⭐ Core Features (Updated)

* Lightweight FastAPI application
* `/health` endpoint for all health checks
* Pytest-based testing
* Dockerfile + Docker Compose for local development
* CircleCI CI/CD pipeline
* Automated Docker image build, run, and endpoint testing
* DockerHub login + image push
* Kubernetes-ready deployment
* Kubernetes Deployment pulling image from DockerHub
* **Kubernetes Readiness & Liveness Probes**

  * *Readiness Probe:* Pod receives traffic only when FastAPI is ready
  * *Liveness Probe:* Automatically restarts app if unresponsive
* NGINX Ingress for domain routing (`fastapi.local`)
* **HTTPS support using self-signed TLS certificates (`https://fastapi.local`)**
* TLS secret stored securely in Kubernetes
* Minikube local Ingress support

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
│── certs/   (ignored in git)
│── .circleci/
│   └── config.yml
│── README.md
```

---

# 📊 Kubernetes Probes (New Feature)

Your `deployment.yaml` now includes:

### ✔ **Readiness Probe**

Ensures the pod only starts receiving traffic *after FastAPI is fully ready*.

### ✔ **Liveness Probe**

Automatically restarts the container if the app becomes unresponsive or stuck.

### Probe Endpoint:

```
/health
```

This endpoint is lightweight and optimized for fast probe checks.

---

# 🔐 HTTPS + Self-Signed Certificate Setup (Minikube)

### 1️⃣ Create a folder for certificates

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

### 4️⃣ Enable Ingress

```
minikube addons enable ingress
```

### 5️⃣ Apply Kubernetes manifests

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

### 7️⃣ Access the service (TLS)

```
https://fastapi.local
https://fastapi.local/health
```

(You will see a browser warning — because it's self-signed.)

---

# 🔄 CI/CD Pipeline (CircleCI)

The CircleCI pipeline performs:

1. Repository checkout
2. Install Python dependencies
3. Run Pytest
4. Build Docker image
5. Run Docker container
6. Test endpoints
7. Login to DockerHub
8. Push image

Push → automatically deployed to DockerHub.

---

# 🧪 Testing (Pytest)

```
pip install -r requirements.txt
pytest -v
```

---

# 🩺 Health Check Endpoint

Used by:

* CI/CD pipeline
* Docker local tests
* Kubernetes probes
* Ingress service validation

```
/health
```

---

# 📦 Docker Compose

```
docker compose up --build
```

---

# ☸️ Kubernetes Deployment (Minikube)

Apply:

```
kubectl apply -f k8s/
```

Includes:

✔ Deployment
✔ NodePort Service
✔ Ingress (HTTP + HTTPS/TLS)
✔ Readiness Probe
✔ Liveness Probe

---

# 🎉 You’re All Set

This project now delivers:

✔ FastAPI
✔ Docker & Docker Compose
✔ CircleCI CI/CD
✔ DockerHub image push
✔ Kubernetes Deployment
✔ **Readiness & Liveness Probes**
✔ NGINX Ingress
✔ HTTPS with self-signed TLS
✔ Clean domain routing

---
