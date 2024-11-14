pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = "joshmurih/flask_app"
        DOCKER_REGISTRY = "docker.io"
        DOCKER_CREDENTIALS_ID = "docker-hub-credentials"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/joshwizard/Docker-Image-Build-Automation-with-Jenkins.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${joshmurih/flask_app}:${env.BUILD_ID}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry("https://docker.io", "docker-hub-credentials") {
                        docker.image("${joshmurih/flask_app}:${env.BUILD_ID}").push()
                    }
                }
            }
        }

        stage('Clean Up') {
            steps {
                script {
                    sh "docker rmi ${joshmurih/flask_app}:${env.BUILD_ID}"
                }
            }
        }
    }
}