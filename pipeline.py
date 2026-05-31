#Load Process

import pandas as pd
import numpy as np
import sqlite3
from sqlalchemy import create_engine
from urllib.parse import quote_plus
df = pd.read_csv('sample_-_superstore.csv')
con = sqlite3.connect("1st_project.db")

#Transform Process

df.duplicated().sum()
df = df.dropna()

df.columns = (
    df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("/", "_").str.replace("-", "_")
)
df = df.drop_duplicates()

df['price'] = df['sales']/df['quantity']

sum_sales_by_customer = (
    df.groupby(["customer_id", "customer_name"])["sales"]
    .sum()
    .reset_index(name="total_sales")
)

dim_customers = (
    df[["customer_id", "customer_name"]]
    .drop_duplicates()
)

dim_region = (
    df[["country_region"]]
    .drop_duplicates()
)

fact_table=df[['row_id','order_id','customer_id', 'customer_name','product_name','country_region','sales', 'quantity', 'discount','profit', 'price']]


#load_to_postgres

from sqlalchemy import create_engine
from urllib.parse import quote_plus

user = "postgres"
password = quote_plus("YourPassword")
host = "localhost"
port = "5432"
database = "first_project_db"

engine = create_engine(
    f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
)

#checking the connection
with engine.connect() as conn:
    print("Connected successfully")
    

fact_table.to_sql("fact", engine, schema="public", if_exists="replace", index=False)
sum_sales_by_customer.to_sql("sum_sales_by_customer", engine, schema="public", if_exists="replace", index=False)
dim_customers.to_sql("dim_customers", engine, schema="public", if_exists="replace", index=False)
dim_region.to_sql("dim_region", engine, schema="public", if_exists="replace", index=False)



