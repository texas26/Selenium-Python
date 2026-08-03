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
                    . .venv/bin/activate
                    pip install -U pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            parallel {
                stage('chrome') {
                    steps {
                        sh '''
                            . .venv/bin/activate
                            BROWSER=chrome pytest -v --junitxml=jenkins/test-results-chrome.xml
                        '''
                    }
                }
                stage('firefox') {
                    steps {
                        sh '''
                            . .venv/bin/activate
                            BROWSER=firefox pytest -v --junitxml=jenkins/test-results-firefox.xml
                        '''
                    }
                }
                stage('headless') {
                    steps {
                        sh '''
                            . .venv/bin/activate
                            BROWSER=headless pytest -v --junitxml=jenkins/test-results-headless.xml
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            junit 'jenkins/test-results-*.xml'
            archiveArtifacts artifacts: 'jenkins/test-results-*.xml', fingerprint: true
        }
    }
}
