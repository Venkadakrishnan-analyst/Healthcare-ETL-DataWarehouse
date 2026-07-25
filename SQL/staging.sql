CREATE DATABASE  healthcare_dw;

CREATE SCHEMA IF NOT EXISTS staging;

CREATE SCHEMA IF NOT EXISTS warehouse;

CREATE TABLE IF NOT EXISTS staging.stg_patients(
patient_id TEXT,
first_name TEXT,
last_name TEXT,
gender TEXT,
date_of_birth DATE,
contact_number BIGINT,
address TEXT,
registration_date DATE,
insurance_provider TEXT,
insurance_number TEXT,
email TEXT
);

COPY staging.stg_patients FROM 'patients.csv' WITH (FORMAT CSV, HEADER TRUE, DELIMITER ',');


CREATE TABLE IF NOT EXISTS staging.stg_appointments(
appointments_id TEXT,
patient_id TEXT,
doctor_id TEXT,
appointment_date DATE,
appointment_time TIME,
reason_for_visit TEXT,
status TEXT
);

COPY staging.stg_appointments FROM 'appointments.csv' WITH (FORMAT CSV, HEADER TRUE, DELIMITER ',');


CREATE TABLE IF NOT EXISTS staging.stg_billing(
bill_id TEXT,
patient_id TEXT,
treatment_id TEXT,
bill_date DATE,
amount FLOAT,
payment_method TEXT,
payment_status TEXT
);

COPY staging.stg_billing FROM 'billing.csv' WITH (FORMAT CSV, HEADER TRUE, DELIMITER ',');


CREATE TABLE IF NOT EXISTS staging.stg_doctors(
doctor_id TEXT,
first_name TEXT,
last_name TEXT,
specialization TEXT,
phone_number BIGINT,
years_experience INT,
hospital_branch TEXT,
email TEXT
);

COPY staging.stg_doctors FROM 'doctors.csv' WITH (FORMAT CSV, HEADER TRUE, DELIMITER ',');


CREATE TABLE IF NOT EXISTS staging.stg_treatments(
treatment_id TEXT,
appointment_id TEXT,
treatment_type TEXT,
description TEXT,
cost FLOAT,
treatment_date DATE
);

COPY staging.stg_treatments FROM 'treatments.csv' WITH (FORMAT CSV, HEADER TRUE, DELIMITER ',');

select * from staging.stg_doctors;