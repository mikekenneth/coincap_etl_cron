
# CounCAP API ETL Pipeline

A training project to implement different best practices of Data Engineering & Data Pipeline management.
You can read the [article]() on this. :sweat_smile:

## Objective
Simple fetch the list of Brypto Exchanges from [CoinCap API](https://docs.coincap.io/#aff336c8-9d06-4654-bc15-a56cef06a69e), enrich & transform the data and store in PostgreSQL database for further use (eg. Analytics, Visualization, etc.)

## Usage
### Setup
- Create `.conf.ini` as a duplicate of `.conf_sample.ini` & update with your PostgreSQL Database credentials:
```bash
cp .conf_sample.ini .conf.ini
```

- Install Python Dependencies (It's preferrable to use a virtual environment):
```bash
pip3 install -r requirements.txt
```

- Setup database. (This drops then recreate the schema & tables):
```bash
python3 setup.py
```
### Run ETL
- Run the command below to run the ETL pipeline:
```bash
python3 run_etl.py
```

## Tech Stack
- [Python3](https://www.python.org/)
- [PostgreSQL](https://www.postgresql.org/)


## TO-DO
- [x] Make the ETL functional as a python script
- [x] Add A Batch ID and Datetime
- [x] Design & Documentation
- [ ] Add Functional Data Engineering Principles (Idempotence, Atomicity, Reusability, Performance-Measurement)
- [ ] Add Dagster as Workflow Orchestrator
- [ ] Add Apache Airflow as Workflow Orchestrator
- [ ] Add Apache Beam as Workflow Orchestrator
- [ ] Add Apache Nifi as workflow Orchestrator
- [ ] Add Docker: Make the project easily deployable


## Authors
- [@mikekenneth](https://www.github.com/mikekenneth)


## License
[MIT](https://choosealicense.com/licenses/mit/)


## Credits
See as you fit.

## Contact
If you have any questions or would like to get in touch, please open an issue on Github or send me an email: <mike.kenneth47@gmail.com>