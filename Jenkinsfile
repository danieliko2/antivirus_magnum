pipeline {
    agent any
    stages {

        stage ('Build') {
            steps {
                sh 'pip install flask'
                sh 'echo "a"'
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
