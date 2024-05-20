pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/sstrohmeyer/browserstack.git' // My public repo
    }

    stages {
        stage('Clone Repository') {
            steps {
                sh '''
                # Clone the repository into the workspace
                git clone ${REPO_URL} .
                '''
            }
        }
        stage('Run Tests') {
            steps {
                browserstack(credentialsId: 'browserstack_creds') {
                    sh '''

                    # Create a virtual environment
                    python3 -m venv venv

                    # Activate the virtual environment
                    . venv/bin/activate

                    # Install Selenium
                    pip install selenium

                    # Fetch and install Browserstack SDK
                    git clone -b sdk https://github.com/browserstack/python-selenium-browserstack
                    pip3 install -r ./python-selenium-browserstack/requirements.txt

                    # Run Browserstack
                    browserstack-sdk python ./tests/test.py
                    '''
                }
            }
        }
    }

    post {
        always {
            cleanWs() // Clean workspace after the build
        }
    }
}
