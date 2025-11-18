# 🚀 FastAPI + Docker + CircleCI Pipeline (with DockerHub Deployment)

A minimal FastAPI application fully containerized with Docker and integrated into a complete CircleCI CI/CD pipeline.
Now includes automated Docker image testing and DockerHub deployment.

---

## 📦 Features

* Lightweight FastAPI application
* Dockerfile for containerized deployment
* Docker Compose for local development
* CircleCI pipeline for continuous integration
* Automated Docker image build, run, and endpoint testing
* Automatic DockerHub login and image push after successful tests

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

The CircleCI workflow performs the following steps:

1. Checks out the repository
2. Installs dependencies and runs basic Python-level tests
3. Builds the Docker image
4. Runs the Docker container
5. Tests the FastAPI endpoint using curl
6. Logs into DockerHub
7. Pushes the image to your DockerHub registry

Once you push to GitHub, the pipeline will run automatically.

---

## 🔐 DockerHub Deployment Setup

Before the pipeline can push images to DockerHub:

1. Go to **Project Settings → Environment Variables → Add Variables**
2. Add the following:

   * `DOCKERHUB_USERNAME` → your DockerHub username
   * `DOCKERHUB_PASSWORD` → your DockerHub password or access token
3. Save and re-run the workflow

CircleCI will authenticate and push images using these credentials.

---

## ▶️ Running the App Locally

You can run the service using Docker Compose:

```
docker compose up --build
```

The app will be available at:

**[http://localhost:8000](http://localhost:8000)**

---