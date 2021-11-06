pipeline{
  agent any;
  stages {
    stage('Code Quality'){
      steps {
        sh 'echo checking code quality'
      }
    }
    stage('Unit Tests'){
      steps {
        sh 'echo testing the applications'
      }
    }
    stage('Build'){
      steps {
        sh 'echo creating application package'
      }
    }
    stage('Delivery'){
      steps {
        sh 'echo uploading the artifact to a repository'
      }
    }
    stage('Deploy'){
      steps {
        sh 'echo deploying the applications'
      }
    }
  }
}
