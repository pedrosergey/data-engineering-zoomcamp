#!/usr/bin/env python
# coding: utf-8

# In[25]:


from sqlalchemy import create_engine
import pandas as pd
from tqdm.auto import tqdm


# In[26]:


# create the url to download

prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
file = 'yellow_tripdata_2021-01.csv.gz'
url = prefix + file


# In[27]:


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


# In[33]:


# check the schema that will be created 

df = pd.read_csv(
    url,
    dtype=dtype,
    parse_dates=parse_dates,
    nrows=1
)

print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))


# In[29]:


# create the conextion to the database

engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')


# In[37]:


# add the schema to the database

df.head(0).to_sql(
    'ny_taxi_data',
    con=engine,
    if_exists='replace'
)


# In[38]:


# create the iterator

df_iterator = pd.read_csv(
    url,
    dtype=dtype,
    parse_dates=parse_dates,
    iterator=True,
    chunksize = 100000
)


# In[40]:


# add the data to the database

for iterator in tqdm(df_iterator):
    iterator.to_sql('ny_taxi_data', con=engine, if_exists='append'
)

