pipeline {

    agent {
        docker { image 'python:3' }
    }

    stages {
        stage ('Hello'){
            steps {
                sh 'echo "Hello!"'
            }
        }

        stage ('Build') {
            steps {
                sh 'pip3 install flask --user'
                sh 'echo "ab"'
            }
        }
        stage ('Test') {
            // when {
            //     expression{
            //     env.GIT_BRANCH ==~ "feature/(.*)"
            //     }
            //     beforeOptions true
            // }
            steps {
                sh 'cd App'
                sh 'sudo flask run'
                
            }
        }
        // stage ('Test - master') {
        //     when {
        //         branch 'master'
        //         beforeOptions true
        //     }
        //     steps {

        //     }
        // }
        // stage ('Tag Image') {
        //     when {
        //         branch 'master'
        //         beforeOptions true
        //     }
        //     steps {

        //     }
        // }
        // stage ('Deploy') {
        //     when {
        //         branch 'master'
        //         beforeOptions true
        //     }
        //     steps {

        //     }
        // }


    }
    post{
        failure{
            echo 'failed to finish'
        }
        success{
            echo 'build success'
        }
    }
}
