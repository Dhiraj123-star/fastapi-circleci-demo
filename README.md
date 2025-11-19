# 🚀 FastAPI + Docker + CircleCI Pipeline (with DockerHub Deployment + Pytest + Health Check)

A minimal FastAPI application fully containerized with Docker and integrated into a complete CircleCI CI/CD pipeline.  
Now includes automated testing using **Pytest**, a **health check endpoint**, and DockerHub image deployment.

---

## 📦 Features

- Lightweight FastAPI application  
- `/health` endpoint for health checks  
- Pytest-based testing  
- Dockerfile for containerized deployment  
- Docker Compose for local development  
- CircleCI pipeline for continuous integration  
- Automated Docker image build, run, and endpoint testing  
- Automatic DockerHub login and image push after successful tests  

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
│── .circleci/
│   └── config.yml
│── README.md

````

---

## 🔄 CI/CD Pipeline (CircleCI)

The CircleCI workflow performs the following steps:

1. Checks out the repository  
2. Installs Python dependencies  
3. Runs **Pytest tests**, including:
   - Root endpoint (`/`)
   - Health check endpoint (`/health`)
4. Builds the Docker image  
5. Runs the Docker container  
6. Tests the running FastAPI endpoint using `curl`  
7. Logs into DockerHub  
8. Pushes the Docker image to DockerHub  

Just push your code → CircleCI runs automatically.

---

## 🧪 Testing (Pytest)

A simple test suite is included:

### Run locally:

```bash
pip install -r requirements.txt
pytest -v
````

### Example test file:

```
tests/test_app.py
```

---

## 🩺 Health Check Endpoint

Your FastAPI service includes:

```python
@app.get("/health")
def health():
    return {"status": "ok", "message": "Service is healthy!"}
```

CircleCI also tests this endpoint during the pipeline.

---

## 🔐 DockerHub Deployment Setup

Before the pipeline can push images:

1. Go to **Project Settings → Environment Variables → Add Variables**
2. Add:

   * `DOCKERHUB_USERNAME` → your DockerHub username
   * `DOCKERHUB_PASSWORD` → your DockerHub password / access token

After saving, re-run the workflow.

---

## ▶️ Running the App Locally (Docker Compose)

```bash
docker compose up --build
```

The app will be available at:

👉 [http://localhost:8000](http://localhost:8000)
👉 [http://localhost:8000/health](http://localhost:8000/health)

---

## 🎉 You're All Set

This project now has:

✔ FastAPI
✔ Docker
✔ Docker Compose
✔ Pytest
✔ CircleCI build pipeline
✔ DockerHub deployment
✔ Health check endpoint

---
