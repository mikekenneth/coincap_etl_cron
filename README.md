
# CounCAP API ETL Pipeline

A training project to implement different best practices of Data Engineering & Data Pipeline management.

## Usage
### Setup
- Create `.conf.ini` as a duplicate of `.conf_sample.ini` file with your PostgreSQL Database credentials:
```bash
cp .conf_sample.ini .conf.ini
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

- Setup database
```bash
python setup_db.py
```

## Tech Stack

Python, Dagster, Docker, PostgreSQL


## TO-DO

- [x] Make the ETL functional as a python script
- [x] Designs & Documentation 
- [ ] Add Dagster and design workflow
- [ ] Add Docker: Make the project easily deployable



## Authors

- [@mikekenneth](https://www.github.com/mikekenneth)


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Credits

See as you fit.

## Contact

If you have any questions or would like to get in touch, please open an issue on Github or send me an email: <mike.kenneth47@gmail.com>