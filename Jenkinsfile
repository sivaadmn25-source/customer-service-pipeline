pipeline {
    agent any

    stages {

        stage('Source') {
            steps {
                echo 'D166 - Source Stage'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'D166 - Build Stage'
                bat 'python build_application.py'
            }
        }

        stage('Test') {
            steps {
                echo 'D166 - Test Stage'
                bat 'python run_tests.py'
            }
        }

        stage('Package') {
            steps {
                echo 'D166 - Package Stage'
                bat 'python create_artifact.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'D166 - Deploy Stage'
                bat 'python deploy_application.py'
            }
        }

    }
}