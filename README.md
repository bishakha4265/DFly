# DFly-Project
DFly is a software development platform that enables developers to seamlessly develop and deploy their applications to public cloud.  
**************************|**************************|**************************|**************************
A website with a simple message: "Welcome to Dfly" (Containerized Flask app running behind nginx web-server container)
**************************|**************************|**************************|**************************
1. The purpose of this web application is to show the message "Welcome to Dragonfly" on the browser (It is using Nginx as web-server).
2. The web application is checked into this git repository on github and is open for other developers to submit Pull-Requests.
3. The repository is equipped with a CI-CD pipeline using Jenkins that does the continuous deployments on a Kubernetes Cluster on AWS EKS Provisioned using AWS        CloudFormation.
4. The application developed in step(1) is Dockerized and deployed to the kubernetes cluster provisioned above.
5. Anyone can Submit a Pull-Request to the git repository in and the CI-CD pipeline will push the changes to Kubernetes cluster.
