pipeline {
    agent any
    stages {
        stage ('Prep') {
            steps {

                }
        }

        stage ('Build') {
            steps {

            }
        }
        stage ('Test - Feature') {
            when {
                expression{
                env.GIT_BRANCH ==~ "feature/(.*)"
                }
                beforeOptions true
            }
            steps {

            }
        }
        stage ('Test - master') {
            when {
                branch 'master'
                beforeOptions true
            }
            steps {

            }
        }
        stage ('Tag Image') {
            when {
                branch 'master'
                beforeOptions true
            }
            steps {

            }
        }
        stage ('Deploy') {
            when {
                branch 'master'
                beforeOptions true
            }
            steps {

            }
        }


    }
    post{
        failure{

        }
        success{

        }
    }
}