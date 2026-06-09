pipeline {
    agent any

    environment {
        APP_NAME = "flask-redis-app"
        VERSION = "1.0.${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out ${APP_NAME} version ${VERSION}"
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image for ${APP_NAME}..."
                sh "docker-compose build"
                echo "Docker image built successfully!"
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying ${APP_NAME} version ${VERSION}..."
                sh "docker-compose down || true"
                sh "BUILD_NUMBER=${BUILD_NUMBER} docker-compose up -d"
                echo "Deployment complete!"
            }
        }

        stage('Verify') {
            steps {
                echo "Verifying deployment..."
                sh "sleep 5"
                sh "curl -f http://localhost:5001/health"
                echo "App is live and healthy!"
            }
        }
    }

    post {
        success {
            echo "${APP_NAME} version ${VERSION} deployed successfully!"
            echo "App is running at http://localhost:5001"
        }
        failure {
            echo "Deployment failed — rolling back..."
            sh "docker-compose down || true"
        }
        always {
            echo "Pipeline finished."
        }
    }
}
