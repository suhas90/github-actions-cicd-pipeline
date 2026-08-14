# github-actions-cicd-pipeline
Automated CI/CD Pipeline using GitHub Actions 
GitHub → GitHub Actions → Test → Docker Build → Trivy Security Scan → Docker Hub → Deploy → Health Check

1. Final project architecture
Developer
   │
   │ git push
   ▼
GitHub Repository
   │
   ▼
GitHub Actions
   │
   ├── Checkout
   ├── Python Setup
   ├── Install Dependencies
   ├── Lint
   ├── Unit Tests
   ├── Docker Build
   ├── Trivy Security Scan
   ├── Docker Login
   ├── Push Image
   │
   ▼
Docker Hub
   │
   ▼
Deployment Server
   │
   ├── Pull latest image
   ├── Stop old container
   ├── Start new container
   │
   ▼
Health Check
   │
   ▼
Application
