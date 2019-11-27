node('docker') {
 
    stage 'Checkout'
        checkout scm

    stage 'Deploy'
        sh "docker-compose -f docker-compose.ci.yml up --force-recreate"
        // sh "docker-compose -f docker-compose.yml down -v"
}