pipeline {
    agent { docker { image 'pmantini/assignment-cosc6380:latest' } }

    environment {
        PATH = "env/bin/:$PATH"
    }
    stages {
        stage('build') {
            steps {
                sh 'python dip_hw5_color.py -i cat.jpg -n 2 -t1 0 -t2 0 -t3 0'
                sh 'python dip_hw5_color.py -i Medical.PNG -n 8 -t1 30 -t2 60 -t3 90'
                sh 'python dip_hw5_color.py -i luggage.jpeg -n 10 -t1 30 -t2 60 -t3 90'
                sh 'python dip_hw5_color.py -i luggage.jpeg -n 10 -t1 60 -t2 120 -t3 180'
                sh 'python dip_hw5_color.py -i pluto.jpg -n 20 -t1 20 -t2 70 -t3 270'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'output/**/*.* ', onlyIfSuccessful: true
        }
    }
}
