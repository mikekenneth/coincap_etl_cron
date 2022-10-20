
# CoinCAP API ETL Pipeline

A sample ETL Pipeline project using Python script only hosted using Docker.
You can read the [article]() on this. :smile:

## Objective
Simple fetch the list of Crypto Exchanges from [CoinCap API](https://docs.coincap.io/#aff336c8-9d06-4654-bc15-a56cef06a69e), enrich & transform the data and store in PostgreSQL database for further use (eg. Analytics, Visualization, etc.)

## Usage
### Setup
- Update `.env` with your **PostgreSQL** Database credentials:

- Run with docker-compose
```bash
docker-compose up
```

## Tech Stack
- [Python3](https://www.python.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)


## TO-DO
- [x] Make the ETL functional as a python script
- [x] Add A Batch ID and Datetime
- [x] Design & Documentation
- [x] Add Docker: Make the project easily deployable


## Authors
- [@mikekenneth](https://www.github.com/mikekenneth)


## License
[MIT](https://choosealicense.com/licenses/mit/)


## Credits
See as you fit.

## Contact
If you have any questions or would like to get in touch, please open an issue on GitHub or send me an email: <mike.kenneth47@gmail.com>