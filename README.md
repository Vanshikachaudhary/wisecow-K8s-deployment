PROBLEM STATEMENT 1: WISECOW DEPLOYMENT USING KUBERNETES

This project sets up a CI/CD pipeline for deploying the Wisecow application using Docker and Kubernetes. The pipeline automates the build and deployment processes with GitHub Actions, deploying the application to a Kind (Kubernetes IN Docker) cluster.

Setup Requirements
- Docker: For containerization
- KIND: A local cluster setup to deploy the application
- Github: Source code Management
- Github Actions: for CI/CD
- Docker Hub: for storing docker images

Deployment Steps/Instructions

1. Clone the repository

      git clone <repository URL>
      cd <directory>

2. Build the Docker Image and push to Docker Hub

     docker build -t <docker hub username>/wisecow-application:latest .
     docker push <docker hub username>/wisecow-application:latest

3. Create KIND Cluster

       - Installation:
              curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.17.0/kind-linux-amd64
              chmod +x ./kind
              sudo mv ./kind /usr/local/bin/kind

       - Create Cluster:

            kind create cluster --name wisecow-cluster

4. Deploy to Kubernetes

       kubectl apply -f namespace.yaml
       kubectl apply -f deployment.yaml
       kubectl  apply -f service.yaml

6. Access the application

       kubectl port-forward service/wisecow-service 8080:80

   Access the application locally at https://localhost:8080


PROBLEM STATEMENT 2: PYTHON SCRIPTS 

1. System Health Monitoring Script

    Developing a script that monitors the health of a linux system.
    Install psutil

       apt install python3-psutil

   Run the script

       python3 system_health.py

2. Log Analyzer Script

   A script that analyzes web server logs for common patterns.

       python3 log_analyzer.py
     
     
