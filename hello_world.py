from dagster import job, op


@op
def get_name():
    return "Dagster"


@op
def hello(name: str):
    print(f"Hello {name}!")


@job
def hello_dagster():
    hello(get_name())
