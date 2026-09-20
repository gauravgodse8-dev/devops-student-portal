pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building DevOps Student Portal...'

                sh 'python3 --version'
                sh 'python3 -m venv venv'
                sh 'venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'venv/bin/pytest'
            }
        }
    }
}