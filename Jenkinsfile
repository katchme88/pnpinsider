node('docker') {
 
    stage 'Checkout'
        checkout scm

    stage 'Deploy'
        sh "docker-compose -f docker-compose.yml up --force-recreate"
        // sh "docker-compose -f docker-compose.yml down -v"
}