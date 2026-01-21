#!/usr/bin/env python
# coding: utf-8

from sqlalchemy import create_engine
import pandas as pd
from tqdm.auto import tqdm
import click

@click.command()
@click.option('--year', default=2021, help='Year of the data')
@click.option('--month', default=1, help='Month of the data')
@click.option('--chunk-size', default=100000, help='Chunk size for reading CSV')
@click.option('--user', default='root', help='PostgreSQL username')
@click.option('--password', default='root', help='PostgreSQL password')
@click.option('--host', default='localhost', help='PostgreSQL host')
@click.option('--port', default=5432, help='PostgreSQL port')
@click.option('--db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--table', default='yellow_taxi_data', help='Table name for data')

def run(year, month, chunk_size, user, password, host, port, db, table):

    # use the data types to enhance the performance

    dtype = {
        "VendorID": "Int64",
        "passenger_count": "Int64",
        "trip_distance": "float64",
        "RatecodeID": "Int64",
        "store_and_fwd_flag": "string",
        "PULocationID": "Int64",
        "DOLocationID": "Int64",
        "payment_type": "Int64",
        "fare_amount": "float64",
        "extra": "float64",
        "mta_tax": "float64",
        "tip_amount": "float64",
        "tolls_amount": "float64",
        "improvement_surcharge": "float64",
        "total_amount": "float64",
        "congestion_surcharge": "float64"
    }

    parse_dates = [
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime"
]

    prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow'
    url = f'{prefix}/yellow_tripdata_{year}-{month:02d}.csv.gz'
   


    # create the conextion to the database

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')


    df = pd.read_csv(
        url,
        dtype=dtype,
        parse_dates=parse_dates,
        nrows=0
    )


    df_iterator = pd.read_csv(
        url,
        dtype=dtype,
        parse_dates=parse_dates,
        iterator=True,
        chunksize = chunk_size
    )
    
    first = True

    for iterator in tqdm(df_iterator):
        if first:
            iterator.to_sql(table, con=engine, if_exists='replace'
        )
            first = False
        else:
            iterator.to_sql(table, con=engine, if_exists='append'
        )

    print("Ingestion complete! :)")

if __name__ == '__main__':
    run()