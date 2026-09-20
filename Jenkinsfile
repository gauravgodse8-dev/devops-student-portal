pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building DevOps Student Portal...'
                sh 'python3 --version'
                sh 'pip3 --version'
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'pytest'
            }
        }
    }
}