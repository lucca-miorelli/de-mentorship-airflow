from datetime import datetime, timedelta
from airflow.decorators import dag, task
from airflow.utils.dates import days_ago

@dag(dag_id="Most_amazing_ETL_ever", schedule_interval=timedelta(seconds=30), start_date=days_ago(1), catchup=False, tags=['example_custom'])
def my_example_dag():

    @task()
    def extract():
        print("Extracting data...")
        return {"data": [1, 2, 3]}

    @task()
    def transform(data):
        print("Transforming data...")
        return {"transformed_data": [x * 2 for x in data["data"]]}

    @task()
    def load(transformed_data):
        print("Loading data...")
        print("Transformed Data: ", transformed_data)

    # Define the task dependencies
    data = extract()
    transformed_data = transform(data)
    load(transformed_data)

# Define the DAG object
example_dag = my_example_dag()