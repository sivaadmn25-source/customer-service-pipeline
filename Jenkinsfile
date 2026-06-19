pipeline {
    agent any

    stages {

        stage('Run Tests') {
            steps {
                bat 'python run_tests.py'
            }
        }

        stage('Build Application') {
            steps {
                bat 'python build_application.py'
            }
        }

        stage('Create Artifact') {
            steps {
                bat 'python create_artifact.py'
            }
        }

        stage('Deploy Application') {
            steps {
                bat 'python deploy_application.py'
            }
        }

    }
}