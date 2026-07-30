## **Healthcare ETL pipeline and Data Warehouse**

## Technologies Used
- Python
- Pandas
- NumPy
- SqlAlchemy
- Postgresql


## Dataset
- Hospital Management Dataset
    - doctors.csv
    - patients.csv
    - treatments.csv
    - appointments.csv
    - billing.csv


## Project execution
- Create a database named **Healthcare_dw** and inside that database creating two schemas **staging** and **warehouse**.
- Load the Datasets into PostgreSQL database.
- Extract data into Python environment using SqlAlchemy.
- Transform the data by performing data cleaning, formatting the data types, calculate measures, creating dimension tables and merge them into a fact table.
- Again Load the data into PostgreSQL Warehouse for further analysis.
