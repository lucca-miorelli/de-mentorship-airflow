# Data Engineering Mentorship: Orchestration with Apache Airflow

As part of the Data Engineering Mentorship program, we'll be working on a project to orchestrate a simple data pipeline using Apache Airflow. 
This readme provides an overview of the project and instructions for setting up Apache Airflow using Docker.

## What is Apache Airflow?
[Apache Airflow](https://airflow.apache.org/) is an open-source platform to programmatically author, schedule and monitor workflows. It allows you to define workflows as code, and execute them on a schedule, monitor them, and manage them.

## Installation
To get started with Apache Airflow, follow these steps:

1. Install Docker on your machine. If you don't have Docker installed, you can download it from the [official website](https://www.docker.com/products/docker-desktop).
2. Clone this repository to your local machine.
3. Navigate to the project directory.
4. Create a `.env` file in the project directory with the following content (template `.env.example`):
   ```
   AIRFLOW_UID=50000
   ```
5. Optionally, update the `AIRFLOW__CORE__LOAD_EXAMPLES` environment variable in the `docker-compose.yml` file to `false` if you don't want to load the example DAGs.
6. Run `docker-compose up -d` to start the Airflow webserver and scheduler (make sure Docker daemon is running).
7. Access the Airflow web interface by visiting `http://localhost:8080` in your browser.
8. Log in with the default credentials:
   - Username: `airflow`
   - Password: `airflow`

## Update to Latest Version of Airflow
The `docker-compose.yml` file currently uses Airflow version 2.9.0. If you want to use the latest version of Airflow, follow these steps:

1. Download the latest `docker-compose.yml` file:
   - For Windows:
     ```
     Invoke-WebRequest https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml -OutFile docker-compose.yml
     ```
   - For macOS:
     ```
     curl –Lf0 “https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml” -o docker-compose.yml
     ```

2. Replace the existing `docker-compose.yml` file with the downloaded file.

Note: The `docker-compose.yml` file is a template provided by the Apache Airflow project. You can customize it as needed.

**Note**: The `docker-compose.yml` file is a template provided by the Apache Airflow project. You can customize it as needed.

