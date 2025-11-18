
# 🚀 FastAPI + Docker + CircleCI Pipeline

A minimal FastAPI application fully containerized with Docker and integrated with a CircleCI CI/CD pipeline.
This project demonstrates how to automate testing and Docker image builds using CircleCI.

---

## 📦 Features

* Lightweight FastAPI application
* Dockerfile for containerized deployment
* Docker Compose for local development
* CircleCI pipeline for continuous integration
* Automated Docker image build & test workflow

---

## 🏗 Project Structure

```
fastapi-circleci-demo/
│── app/
│   ├── main.py
│   └── __init__.py
│── Dockerfile
│── docker-compose.yml
│── requirements.txt
│── .circleci/
│   └── config.yml
│── README.md
```

---

## 🔄 CI/CD Pipeline (CircleCI)

The CircleCI workflow:

1. Checks out the repository
2. Sets up Python
3. Installs dependencies
4. Runs tests
5. Builds the Docker image

Just push your code → CircleCI runs automatically.

---

## ▶️ Running the App Locally

You can run the service using Docker Compose:

```
docker compose up --build
```

The app will be available on **[http://localhost:8000](http://localhost:8000)**

---
