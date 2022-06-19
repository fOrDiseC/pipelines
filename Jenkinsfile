

pipeline {
    
    
    agent any
    
    
    stages {
        stage('start script') {
            
            steps {
                script{
                
                echo "${WORKSPACE}"
               
                
                //def test_path1 ='D:\\Dev\\rezult'
                //def fullpath = test_path1+'\\'+params.Test_date+'\\'+params.Distr
                //env.mypath = fullpath
                
                bat'''
                echo %Path_to_file%
                python --version
                
                echo start activation
                
                call C:\\Users\\disho\\miniconda3\\Scripts\\activate.bat
                
                echo after activation
                
                python --version
                
                python Test_diff\\titanic.py
                
                
                
                
                
                '''
                
                
                
                }
                
            }
        }
    }
}
