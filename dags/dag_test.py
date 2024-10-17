import datetime

from src import DAG
from src.operators.empty import EmptyOperator

with DAG(
        dag_id="my_dag_name",
        start_date=datetime.datetime(2021, 1, 1),
        schedule="@daily",
):
    EmptyOperator(task_id="task")