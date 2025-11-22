
# 🚀 FastAPI + Docker + CircleCI Pipeline

(DockerHub + Pytest + Health Check + **Helm Chart** + K8s + Ingress + TLS/SSL + Probes)

A minimal FastAPI application fully containerized with Docker and integrated into a complete CircleCI CI/CD pipeline.
Now includes automated testing with **Pytest**, a Kubernetes deployment with **readiness/liveness probes**, **NGINX Ingress**, **domain-based routing**, **HTTPS using self-signed TLS certificates**, and a **production-ready Helm chart for Kubernetes deployment**.

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

### **🆕 Added: Helm Chart Deployment**

* Production-ready Helm chart (`fastapi-chart/`)
* Deploy FastAPI on K8s using:

  ```
  helm install fastapi ./fastapi-chart
  ```
* Helm values support:

  * replicaCount
  * image repository & tag
  * NodePort
  * NGINX Ingress + TLS
  * Readiness & Liveness probe config
  * Autoscaling toggle
* Fully parameterized Deployment, Service, and Ingress
* Support for upgrading:

  ```
  helm upgrade fastapi ./fastapi-chart
  ```

---

# 📦 New: Helm Chart Structure

```
fastapi-chart/
│── Chart.yaml
│── values.yaml
│── templates/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   └── NOTES.txt
```

The chart automatically deploys your app with:

✔ Deployment
✔ NodePort Service
✔ Ingress (HTTP + HTTPS/TLS)
✔ Readiness & Liveness Probes
✔ Replica scaling
✔ Custom image configuration

---

# 🛠 Deploy Using Helm

### 1️⃣ Install the Helm chart

```
helm install fastapi ./fastapi-chart
```

### 2️⃣ Upgrade after changes

```
helm upgrade fastapi ./fastapi-chart
```

### 3️⃣ Uninstall

```
helm uninstall fastapi
```

---

# 📊 Kubernetes Probes (Already Supported)

Your Deployment uses:

✔ Readiness Probe
✔ Liveness Probe
✔ `/health` endpoint for both

---

# 🔐 HTTPS + Self-Signed Certificate Setup (Minikube)

(unchanged — works with both raw YAML & Helm)

```
kubectl create secret tls fastapi-tls \
  --cert=certs/fastapi.local.crt \
  --key=certs/fastapi.local.key
```

The Helm chart automatically detects and uses this TLS secret through `values.yaml`.

---

# 🔄 CI/CD Pipeline (CircleCI)

(unchanged)

---

# 🧪 Testing (Pytest)

(unchanged)

---

# 📦 Docker Compose

(unchanged)

---

# ☸️ Kubernetes Deployment (using Helm)

Now preferred over raw YAML.

```
helm install fastapi ./fastapi-chart
```

Includes:

✔ Deployment
✔ NodePort Service
✔ NGINX Ingress
✔ HTTPS/TLS
✔ Probes
✔ Replicas

---

# 🎉 You’re All Set

Your project now supports:

✔ FastAPI
✔ Docker & Docker Compose
✔ CircleCI CI/CD
✔ DockerHub push
✔ **Helm-based Kubernetes deployment**
✔ Readiness & Liveness Probes
✔ NGINX Ingress
✔ TLS/HTTPS
✔ Clean domain routing

---
