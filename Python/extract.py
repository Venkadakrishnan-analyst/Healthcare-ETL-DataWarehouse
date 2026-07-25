import pandas as pd
import numpy as np
from sqlalchemy import create_engine



''' --Configure the postgresql server to establish connection '''

engine=create_engine("postgresql://username:password@host:port/database_name")



''' --Load the datasets from postgresql '''

patients=pd.read_sql("SELECT * FROM staging.stg_patients",engine)
treatments=pd.read_sql("SELECT * FROM staging.stg_treatments",engine)
doctors=pd.read_sql("SELECT * FROM staging.stg_doctors",engine)
appointments=pd.read_sql("SELECT * FROM staging.stg_appointments",engine)
billing=pd.read_sql("SELECT * FROM staging.stg_billing",engine)


print(patients.columns)
print(doctors.columns)
print(appointments.columns)
print(treatments.columns)
print(billing.columns)