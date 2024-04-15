# Minikube Cluster with Dockerized Services: Predictive Analytics Example

Welcome to the Minikube Cluster with Dockerized Services project! This project demonstrates the implementation of a predictive analytics pipeline using a Minikube Kubernetes cluster. We've dockerized three services: a PostgreSQL database, a linear regression model with FastAPI for prediction, and a connector service that orchestrates communication between the database and the model.

## Overview

In this setup, we've created a miniature Kubernetes cluster using Minikube, allowing us to manage and deploy our containerized services efficiently. Here's a breakdown of the components:

1. PostgreSQL Database Service: This service stores the data required for model training and prediction. It serves as our persistent storage solution, housing the datasets and any necessary metadata.

2. Linear Regression Model with FastAPI: Implemented as a separate service, this container hosts a machine learning model trained to perform linear regression. FastAPI is employed to provide a RESTful API for making predictions based on input data.

3. Connector Service: Acting as the bridge between the database and the model, this service handles the retrieval of data from PostgreSQL, forwards it to the prediction model via FastAPI, and returns the predictions back to the client.

Additionally, we've integrated a Cron Job Scheduler into the cluster. This scheduler is responsible for periodically generating new data for prediction, which is then fed into the pipeline through the connector service. By automating this process, we ensure that our model remains up-to-date and relevant.

## Getting started

### Prerequisites

Before getting started, ensure you have the following prerequisites installed:

1. Docker 24.0.7: Minikube may not be compatible with higher versions of Docker, so we recommend installing version 24.0.7

2. Minikube: Minikube provides a local Kubernetes cluster for development and testing purposes. Install Minikube by following the instructions appropriate for your operating system [here](https://minikube.sigs.k8s.io/docs/start/).

3. kubectl: kubectl is the Kubernetes command-line tool used to interact with the cluster. You can install it using the instructions [here](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/).

4. Start Minikube: Once Minikube and kubectl are installed, start Minikube by running the following command:
```bash
minikube start
```
5. (Optional) Start minikube dashboard with command:
```bash
minikube dashboard
```

## Building services

### Postgres image

1. Position Yourself in the yaml_files Folder.

2. To create service for postgres in minikube run command:

```bash
kubectl apply -f postgres.yaml
```

### Model image

1. Position Yourself in the "model" Folder.

2. Build the Docker Image:

Once you're in the model folder, run the following command to build the Docker image for the model service:

```bash
docker build -t model .
```

3. Load docker image to minikube with command:
```bash
minikube image load model
```

4. Position Yourself in the yaml_files Folder.

5. To create deployment for model in minikube run command:

```bash
kubectl apply -f model-deployment.yaml
```

6. To create service for model in minikube run following command:

```bash
kubectl apply -f model-svc.yaml
```

### Connect image

1. Position Yourself in the "connect" Folder.

2. To get cluster_ip and port from postgres and model in minikube run:

```bash
kubectl get services
```

3. In database.py set ip_address to postgres cluster_ip and set port to postgres port.

4. In main.py  ip_address to model cluster_ip and set port to model port.

5. Build the Docker Image:

Once you're in the connect folder, run the following command to build the Docker image for the connect service:

```bash
docker build -t connect .
```

6. Load docker image to minikube with command:
```bash
minikube image load connect
```

7. Position Yourself in the yaml_files Folder.

8. To create deployment for connect in minikube run command:

```bash
kubectl apply -f connect-deployment.yaml
```

9. To create service for connect in minikube run following command:

```bash
kubectl apply -f connect-svc.yaml
```

### Scheduler image

1. Position Yourself in the "scheduler" Folder.

2. To get cluster_ip and port from connect in minikube run:

```bash
kubectl get services
```

3. In main.py set ip_address to connect cluster_ip and set port to connect port.

4. Build the Docker Image:

Once you're in the scheduler folder, run the following command to build the Docker image for the scheduler cronjob.

```bash
docker build -t scheduler .
```

5. Load docker image to minikube with command:

```bash
minikube image load scheduler
```

6. Position Yourself in the yaml_files Folder.

7. To create cronjob for scheduler in minikube run command:

```bash
kubectl apply -f scheduler.yaml
```

## Stop and delete

* To stop minikube run:
```bash
minikube stop
```

* To delete everything run:
```bash
minikube delete --all
```