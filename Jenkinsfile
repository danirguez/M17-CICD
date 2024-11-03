pipeline {
    agent any

    environment {
        registry = "danirguez/m17-cicd"
        registryCredentials = "dockerhub-user"
        project = "m17-cicd"
        projectVersion = "1.0"
        repository = "https://github.com/danirguez/M17-CICD.git"
        repositoryCredentials = "github-user"
    }

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }
        stage('Checkout code') {
            steps {
                git branch: 'main',
                    credentialsId: repositoryCredentials,
                    url: repository
            }
        }
        stage('Build') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                    dockerImage = docker.build registry
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    try {
                        sh "docker run --name $project $registry"
                    } finally {
                        sh "docker rm $project"
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    docker.withRegistry('', registryCredentials) {
                        dockerImage.push()
                    }
                }
            }
        }

    }
    post {
        failure {
            echo 'El pipeline ha fallado.'
        }
    }
}