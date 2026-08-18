# 🚀 GitHub Actions CI/CD Pipeline

A production-style **CI/CD pipeline for a containerized Python Flask application**, implemented using **GitHub Actions, Docker, Docker Hub, Trivy, and automated SSH-based deployment**.

The project demonstrates how source code can move automatically from **GitHub → automated testing → Docker build → security scanning → Docker Hub → deployment server → health check**.

---

## 📌 Project Overview

This project implements an end-to-end DevOps pipeline that automates the software delivery lifecycle.

### Pipeline Flow

```text
Developer
    │
    │ git push
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ├── Checkout Code
    ├── Setup Python
    ├── Install Dependencies
    ├── Flake8 Linting
    ├── Pytest Unit Tests
    │
    ▼
Docker Build
    │
    ▼
Trivy Security Scan
    │
    ▼
Docker Hub
    │
    ▼
Ubuntu Deployment Server
    │
    ├── Pull Latest Image
    ├── Restart Container
    └── Docker Compose
    │
    ▼
Application
    │
    ▼
Health Check
```

---

# 🛠️ Technologies Used

| Technology         | Purpose                          |
| ------------------ | -------------------------------- |
| **Python 3.12**    | Application development          |
| **Flask**          | Web application framework        |
| **Pytest**         | Unit testing                     |
| **Flake8**         | Python code linting              |
| **Docker**         | Application containerization     |
| **Docker Compose** | Container management             |
| **GitHub**         | Source code management           |
| **GitHub Actions** | CI/CD automation                 |
| **Docker Hub**     | Container image registry         |
| **Trivy**          | Container vulnerability scanning |
| **Ubuntu Linux**   | Deployment server                |
| **SSH**            | Secure remote deployment         |

---

# ✨ Project Features

* ✅ Automated CI/CD pipeline
* ✅ GitHub Actions workflow
* ✅ Python unit testing
* ✅ Flake8 code quality checks
* ✅ Docker image build
* ✅ Trivy vulnerability scanning
* ✅ Docker Hub image publishing
* ✅ SSH-based automated deployment
* ✅ Docker Compose deployment
* ✅ Application health check
* ✅ Git commit SHA image tagging
* ✅ `latest` Docker image tagging
* ✅ Non-root Docker container
* ✅ GitHub encrypted secrets
* ✅ Production-style deployment workflow

---

# 📁 Project Directory Structure

```text
github-actions-cicd-pipeline/
│
├── .github/
│   └── workflows/
│       └── cicd.yml
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── tests/
│   └── test_app.py
│
├── Dockerfile
├── docker-compose.yml
├── docker-compose.prod.yml
├── requirements.txt
├── requirements-dev.txt
├── .dockerignore
├── .gitignore
├── .env.example
├── run.py
└── README.md
```

---

# 🔄 CI/CD Pipeline

The GitHub Actions workflow performs the following stages:

```text
1. Checkout Source Code
        ↓
2. Setup Python
        ↓
3. Install Dependencies
        ↓
4. Run Flake8
        ↓
5. Run Pytest
        ↓
6. Build Docker Image
        ↓
7. Run Trivy Security Scan
        ↓
8. Login to Docker Hub
        ↓
9. Push Docker Image
        ↓
10. SSH to Deployment Server
        ↓
11. Pull Latest Docker Image
        ↓
12. Restart Application
        ↓
13. Health Check
```

---

# 🧪 Continuous Integration

The CI stage validates the application before it can be deployed.

### Flake8

```bash
flake8 app tests run.py
```

Checks Python code quality and identifies common coding errors.

### Pytest

```bash
pytest -v
```

Runs automated unit tests.

Example:

```text
============================= test session starts =============================

tests/test_app.py::test_home PASSED
tests/test_app.py::test_health PASSED

============================== 2 passed ======================================
```

---

# 🐳 Docker

The application is packaged as a Docker image.

### Build Docker Image

```bash
docker build -t github-actions-cicd-pipeline .
```

### Run Container

```bash
docker run -d \
  -p 5000:5000 \
  --name github-actions-cicd-app \
  github-actions-cicd-pipeline
```

### Check Running Containers

```bash
docker ps
```

### View Logs

```bash
docker logs github-actions-cicd-app
```

### Stop Container

```bash
docker stop github-actions-cicd-app
```

### Remove Container

```bash
docker rm github-actions-cicd-app
```

---

# 🐳 Docker Compose

Start the application:

```bash
docker compose up -d --build
```

Check status:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs -f
```

Stop the application:

```bash
docker compose down
```

---

# 🔐 DevSecOps Security

This project integrates **Trivy** into the CI/CD pipeline.

Trivy scans the Docker image for:

* Critical vulnerabilities
* High vulnerabilities
* OS package vulnerabilities
* Application dependency vulnerabilities

The pipeline is configured to fail when critical/high vulnerabilities are detected.

```text
Docker Build
      ↓
     Trivy
      ↓
Vulnerability Scan
      ↓
 ┌────┴────┐
 │         │
PASS      FAIL
 │         │
 ▼         ▼
Docker    Stop
Hub       Pipeline
```

---

# 📦 Docker Hub

After successful security scanning, the Docker image is pushed to Docker Hub.

Image format:

```text
DOCKERHUB_USERNAME/github-actions-cicd-pipeline:latest
```

The pipeline also creates an immutable image tag using the Git commit SHA:

```text
DOCKERHUB_USERNAME/github-actions-cicd-pipeline:<commit-sha>
```

This allows a specific application version to be identified and deployed.

---

# 🚀 Continuous Deployment

After the Docker image is successfully pushed, GitHub Actions connects to the Ubuntu server using SSH.

The deployment process is:

```text
GitHub Actions
      ↓
SSH
      ↓
Ubuntu Server
      ↓
docker compose pull
      ↓
docker compose up -d
      ↓
New Container
```

The deployment server uses:

```text
docker-compose.prod.yml
```

to run the production container.

---

# 🖥️ Deployment Server Requirements

The deployment server requires:

* Ubuntu Linux
* Docker
* Docker Compose
* SSH access
* Network connectivity
* Port `5000` accessible for the application health check

Install Docker:

```bash
sudo apt update
sudo apt install -y docker.io docker-compose-plugin
```

Enable Docker:

```bash
sudo systemctl enable docker
sudo systemctl start docker
```

Verify:

```bash
docker --version
docker compose version
```

---

# 📂 Deployment Directory

The production server uses:

```text
/opt/github-actions-cicd-pipeline/
```

Structure:

```text
/opt/github-actions-cicd-pipeline/
│
└── docker-compose.prod.yml
```

---

# 🔑 GitHub Actions Secrets

The following secrets must be configured under:

```text
GitHub
→ Repository
→ Settings
→ Secrets and variables
→ Actions
```

Required secrets:

```text
DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
SERVER_HOST
SERVER_USER
SERVER_SSH_KEY
```

### DOCKERHUB_USERNAME

Your Docker Hub username.

### DOCKERHUB_TOKEN

Docker Hub access token.

A Docker Hub access token should be used instead of your Docker Hub password.

### SERVER_HOST

Public IP address or hostname of the deployment server.

Example:

```text
203.0.113.50
```

### SERVER_USER

SSH user of the Ubuntu server.

Example:

```text
ubuntu
```

### SERVER_SSH_KEY

Private SSH key used by GitHub Actions to connect to the deployment server.

**Never commit the private SSH key to GitHub.**

---

# 🧑‍💻 Running the Application Locally

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/github-actions-cicd-pipeline.git
```

```bash
cd github-actions-cicd-pipeline
```

---

## 2. Create Virtual Environment

### Windows

```powershell
python -m venv .venv
```

Activate:

```powershell
.venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements-dev.txt
```

---

## 4. Run Tests

```bash
pytest -v
```

---

## 5. Run Linting

```bash
flake8 app tests run.py
```

---

## 6. Start Application

```bash
python run.py
```

Application:

```text
http://localhost:5000
```

---

# ❤️ Health Check

The application provides a health endpoint:

```text
GET /health
```

Open:

```text
http://localhost:5000/health
```

Expected response:

```json
{
  "status": "healthy"
}
```

This endpoint is also used by the CI/CD pipeline to verify that the deployed application is responding.

---

# 🏗️ Application Endpoint

The main application endpoint is:

```text
GET /
```

Example response:

```json
{
  "application": "GitHub Actions CI/CD Demo",
  "status": "running",
  "version": "1.0.0"
}
```

---

# 📊 Docker Image Lifecycle

```text
Source Code
     ↓
Docker Build
     ↓
Security Scan
     ↓
Docker Hub
     ↓
Deployment Server
     ↓
Docker Container
```

Image tags:

```text
latest
```

and:

```text
<git-commit-sha>
```

Using the Git commit SHA provides traceability between the deployed container and the exact source-code version.

---

# 🔒 Security Practices

The project follows several DevSecOps practices:

* Docker container runs as a non-root user
* Docker Hub access token instead of password
* GitHub encrypted secrets
* SSH key-based authentication
* Trivy vulnerability scanning
* `.gitignore` prevents accidental environment files
* `.dockerignore` reduces Docker build context
* Immutable Git commit SHA image tags
* Security scan runs before Docker image publishing
* Tests must pass before deployment

---

# 📈 Future Enhancements

The project can be extended with:

```text
GitHub Actions
      ↓
SonarQube
      ↓
OWASP Dependency Check
      ↓
Trivy
      ↓
Docker
      ↓
Docker Hub
      ↓
AWS EC2
      ↓
Nginx
      ↓
HTTPS
      ↓
Prometheus
      ↓
Grafana
      ↓
Alertmanager
```

Planned improvements:

* [ ] Add SonarQube
* [ ] Add OWASP Dependency-Check
* [ ] Add Nginx reverse proxy
* [ ] Add HTTPS/SSL
* [ ] Deploy to AWS EC2
* [ ] Add Terraform infrastructure
* [ ] Add Prometheus monitoring
* [ ] Add Grafana dashboards
* [ ] Add Alertmanager
* [ ] Add Slack/Teams notifications
* [ ] Add Kubernetes deployment
* [ ] Add Helm charts
* [ ] Add Argo CD GitOps
* [ ] Add blue-green deployment
* [ ] Add automatic rollback
* [ ] Add AI-powered CI/CD troubleshooting

---

# 🎯 Learning Objectives

This project demonstrates practical knowledge of:

* Git and GitHub
* GitHub Actions
* CI/CD
* Python application testing
* Docker
* Docker Compose
* Container registries
* DevSecOps
* Vulnerability scanning
* Linux
* SSH
* Automated deployment
* Infrastructure concepts
* Application health monitoring

---

# 👨‍💻 Author

**Suhas Bhalerao**

DevOps Engineer | Cloud | CI/CD | Docker | AWS | DevSecOps

---

# ⭐ Project Status

**Status:** 🚧 Active Development

This project is being continuously improved by adding cloud infrastructure, monitoring, security, Kubernetes, GitOps and AI-powered DevOps automation.
