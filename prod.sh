#!/bin/bash

rm hubba/local_settings.py

cd hubba_products
wget https://s3.amazonaws.com/hubba-data-engineer-datasets/prods.csv 
wget https://s3.amazonaws.com/hubba-data-engineer-datasets/actions.csv
wget https://s3.amazonaws.com/hubba-data-engineer-datasets/buyers.csv
cd ..
python3 manage.py load_data
python3 manage.py load_recommendations