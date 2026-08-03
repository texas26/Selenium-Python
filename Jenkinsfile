pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    source .venv/bin/activate
                    pip install -U pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    source .venv/bin/activate
                    pytest -v --junitxml=jenkins/test-results.xml
                '''
            }
        }
    }

    post {
        always {
            junit 'jenkins/test-results.xml'
            archiveArtifacts artifacts: 'jenkins/test-results.xml', fingerprint: true
        }
    }
}
