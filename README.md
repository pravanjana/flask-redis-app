# Flask Redis App

A multi-container web application deployed via Jenkins CI/CD pipeline using Docker Compose.

## What it does
- Tracks page visits using a Redis counter
- Displays visit count in real time on the web page
- Shows the Jenkins build number that deployed the app
- Health check endpoint at /health verifies Redis connectivity

## Tech Stack
- Python 3.11 + Flask (web framework)
- Redis 7 (visit counter storage)
- Docker Compose (multi-container orchestration)
- Jenkins (CI/CD pipeline)
- GitHub (Pipeline as Code via Jenkinsfile)

## Architecture
Browser → Flask container (port 5001)
↓
Redis container (port 6379)

## Pipeline Stages
1. Checkout SCM - pulls latest code from GitHub
2. Build Docker Image - builds Flask image via docker-compose build
3. Deploy - runs docker-compose up -d (Flask + Redis containers)
4. Verify - health check confirms app and Redis are live
5. Post Actions - success/failure notification + rollback on failure

## Key Concepts Demonstrated
- Multi-container Docker networking
- Stateful deployment with Redis volume persistence
- Automated health verification in pipeline
- Auto rollback on deployment failure
- Build number traceability end to end
