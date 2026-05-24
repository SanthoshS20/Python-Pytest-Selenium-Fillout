pipeline {
    
    agent any

    triggers {
        githubPush()
    }
    
    stages {
        
        // stage('clean up') {
        //     steps {
        //         cleanWs()
        //     }
        // }
        
        stage('clone repo') {
            
            steps {
                checkout scm
            }
        }
        
        stage('install requirements') {
            
            steps {
               bat """
                    python -m venv hackerrank
                    mkdir logs
                    call hackerrank\\Scripts\\activate

                    pip install -r requirements.txt

                    pip list
                """
            }
        }
        
        stage('run the test') {
            
            steps {
               bat """
                    call hackerrank\\Scripts\\activate

                    pytest -vv --browser_name chrome --html=hackerrank.html tests\\test_login_page\\test_login_page.py -m login
                """
            }
        }
    }
}
