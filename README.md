# Python-sql-pipeline-project-1
ETL pipeline project in Python using Pandas and SQL

This project demonstrates a simple ETL pipeline built with Python, Pandas, and PostgreSQL using the Superstore dataset.

## Project Goal
The goal of this project is to:
- load raw sales data from a CSV file
- clean and transform the dataset
- create analytical tables
- load the final tables into PostgreSQL

## Technologies Used
- Python
- Pandas
- NumPy
- PostgreSQL
- SQLAlchemy

## Transformations Performed
- removed null values
- removed duplicate rows
- standardized column names
- created a calculated `price` field
- created aggregated sales by customer
- created dimension-style tables
- created a fact-style table

## Tables Created
- `fact`
- `sum_sales_by_customer`
- `dim_customers`
- `dim_region`

## Dataset
- `sample_-_superstore.csv`

