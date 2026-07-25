from transform import *



''' --Load the warehouse tables into PostgreSQL '''

dim_doctors.to_sql('dim_doctors', 
                   engine, 
                   schema='warehouse', 
                   if_exists='replace', index=False)

dim_patients.to_sql('dim_patients', 
                    engine, 
                    schema='warehouse', 
                    if_exists='replace', index=False)

dim_treatments.to_sql('dim_treatments', 
                      engine, 
                      schema='warehouse', 
                      if_exists='replace', index=False)

dim_date.to_sql('dim_date', 
                engine, 
                schema='warehouse', 
                if_exists='replace', index=False)

fact_hospital.to_sql('fact_hospital', 
                     engine, 
                     schema='warehouse', 
                     if_exists='replace', index=False)