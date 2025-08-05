pipeline {
    agent any

    environment {
        DOCKERHUB_USERNAME = 'akaarim8'
        IMAGE_NAME = 'flask-task-manager'
        SONAR_SCANNER_HOME = '/opt/sonar-scanner'
        SONAR_PROJECT_KEY = 'flask-task-manager'
        SONAR_HOST_URL = 'http://sonarqube:9000'

    }

    stages {
        stage('Debug Workspace') {
            steps {
                sh 'ls -l ${WORKSPACE}'
            }
        }
        stage('Checkout') {
            steps {
                git branch: 'main', url:'https://github.com/akaarim8/flask-task-manager.git'
            }
        }

        stage('SonarQube Analysis'){
            steps {
                withCredentials([string(credentialsId: 'flask-task-manager-token', variable: 'SONAR_TOKEN')]) {
                    withSonarQubeEnv('SonarQube-Local') {
                        sh '''
                            ${SONAR_SCANNER_HOME}/bin/sonar-scanner \
                            -Dsonar.projectKey=${SONAR_PROJECT_KEY}\
                            -Dsonar.sources=. \
                            -Dsonar.host.url=http://sonarqube:9000 \
                            -Dsonar.login=${SONAR_TOKEN} \
                        '''
                    }
                }
            }
        }

        stage('Build') {
            steps {
                sh '''
                    docker build -t ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${BUILD_NUMBER} .
                    docker build -t ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:latest .
                '''
            }
        }

        stage('Trivy Scan') {
            steps {
                sh '''
                    echo "Running Trivy filesystem scan..."
                    trivy fs . --format table

                    echo "Running Trivy image scan..."
                    trivy image --format table \
                    ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${BUILD_NUMBER}

                    echo "Generating HTML security reports..."
                    trivy fs . --format template --template "./contrib/html.tpl" --output trivy-fs-report.html
                    trivy image --format template --template "./contrib/html.tpl" --output trivy-image-report.html \
                    ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${BUILD_NUMBER}

                    echo "Security scan completed!"
                '''
            }
        }
    }
}
