pipeline {
    agent any  // <-- Set agent globally so post block has a node context

    stages {
        stage('Run Parallel Tests') {
            parallel {
                stage('Chrome') {
                    steps {
                        checkout scm
                        sh '''
                            python3 -m venv .venv
                            source .venv/bin/activate
                            pip install -U pip
                            pip install -r requirements.txt
                            
                            BROWSER=chrome pytest -v --html=report-chrome.html --self-contained-html
                        '''
                    }
                }
                stage('Firefox') {
                    steps {
                        checkout scm
                        sh '''
                            python3 -m venv .venv
                            source .venv/bin/activate
                            pip install -U pip
                            pip install -r requirements.txt
                            
                            BROWSER=firefox pytest -v --html=report-firefox.html --self-contained-html
                        '''
                    }
                }
                stage('Headless') {
                    steps {
                        checkout scm
                        sh '''
                            python3 -m venv .venv
                            source .venv/bin/activate
                            pip install -U pip
                            pip install -r requirements.txt
                            
                            BROWSER=headless pytest -v --html=report-headless.html --self-contained-html
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'report-*.html', allowEmptyArchive: true, fingerprint: true
        }
    }
}