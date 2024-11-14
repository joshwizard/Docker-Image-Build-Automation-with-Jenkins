pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = "joshmurih/Flask_App"
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
                    docker.build("${joshmurih/Flask_App}:${env.BUILD_ID}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry("https://docker.io", "docker-hub-credentials") {
                        docker.image("${joshmurih/Flask_App}:${env.BUILD_ID}").push()
                    }
                }
            }
        }

        stage('Clean Up') {
            steps {
                script {
                    sh "docker rmi ${joshmurih/Flask_App}:${env.BUILD_ID}"
                }
            }
        }
    }
}