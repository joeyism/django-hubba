# Hubba Recommendation Sample Website

## Pre-setup
If this is run on an EC2 instance, there's a script that helps with that.

First, select the Ubuntu 16.04 image. Once sshed inside, run

```bash
wget -O - https://raw.githubusercontent.com/joeyism/.files/master/instances/apt-python-chrome-instances.sh | bash -
```

which will install all necessary tools to run anything from this project, including the scraper.

## Installation
Clone the repository with

```bash
git clone --recursive https://github.com/joeyism/django-hubba.git
```

Install the python dependencies through pip with

```bash
pip3 install -r requirements.txt
```

## Setup
Setup the database by running

```bash
python3 manage.py migrate
python3 manage.py load_data
python3 manage.py load_recommendations
```
## Run Server

```bash
python3 manage.py runserver
```

## Scraper
The scraper can be found in `hubba_products/` folder. To run it normally (from the root of the project), run

```bash
python3 hubba_products/scraper.py [CSV FILENAME]
```

**For Example**

```bash
python3 hubba_products/scraper.py hubba_products/prods_scraped.csv
```

which will save it in `prods_scraped.csv` file.

### Headless
If you want to run it headlessly (in an EC2 instance), simply add the flag `--headless`, such that 

```bash
python3 hubba_products/scraper.py hubba_products/prods_scraped.csv --headless
```

## Database
Running migrations and load automatically adds it to a SQLite3 local database. To save it into a Postgresql database, remove the `hubba/local_settings.py` file.

