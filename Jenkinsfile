pipeline {
  agent any
  stages {
    stage('Jenkins Build Stage') {
      parallel {
        stage('Backend image') {
          steps {
            sh 'echo "Backend"'
          }
        }
        stage('Database image') {
          steps {
            sh 'echo "Front end"'
          }
        }
        stage('Frontend image') {
          steps {
            sh 'echo "Database"'
          }
        }
      }
    }
    stage('Test Stage') {
      parallel {
        stage('Integration Tests') {
          steps {
            sh 'echo "Shreyak"'
          }
        }
        stage('Unit Tests') {
          steps {
            sh 'echo "Unit Tests"'
          }
        }
      }
    }
    stage('Deploy Stage') {
      parallel {
        stage('Deploy Stage') {
          steps {
            sh 'echo "Deploy"'
          }
        }
        stage('Trigger Rundeck Job') {
          steps {
            sh 'echo "Well Played"'
          }
        }
      }
    }
  }
}