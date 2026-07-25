from extract import *



''' --Transforming patients table and creating dimension table ( dim_patients ) '''

print(patients.to_srting())

patients['patient_name']=patients['first_name']+" "+patients['last_name']

patients['registration_date']=pd.to_datetime(patients['registration_date']).dt.strftime("%d-%m-%Y")

patients['age'] = ((pd.Timestamp.today() - pd.to_datetime(patients['date_of_birth'])).dt.days // 365.25).astype(int)

patients['gender']=patients['gender'].replace({
    'M':'Male',
    'm':'Male',
    'F':'Female',
    'f':'Female'
    })

patients['age_group'] = pd.cut(
    patients['age'],
    bins=[0, 12, 19, 60, 120],
    labels=['Child', 'Teenage', 'Adult', 'Senior'],
    include_lowest=True
)

dim_patients=patients[
    ['patient_id',
     'patient_name',
     'age',
     'age_group',
     'gender',
     'address',
     'insurance_provider',
     'registration_date']].copy()

dim_patients.insert(0,'patient_key', range(1,len(dim_patients)+1))

print(dim_patients.to_string())
print(dim_patients.columns)



''' --Transforming Doctors table and creating a dimension table ( dim_doctors ) '''

print(doctors.to_string())

doctors['doctor_name']=doctors['first_name']+" "+doctors['last_name']

doctors['experience_category']=pd.cut(
    doctors['years_experience'],
    bins=[0, 5, 10, 20, 100],
    labels=['Beginner', 'intermediate', 'Senior', 'Expert'],
    include_lowest=True
)

dim_doctors=doctors[
    ['doctor_id',
    'doctor_name',
    'specialization',
    'years_experience',
    'experience_category',
    'hospital_branch']].copy()

dim_doctors.insert(0, 'doctor_key', range(1,len(dim_doctors)+1))

print(dim_doctors.to_string())
print(dim_doctors.columns)



''' --Transforming Treatments table and creating dimension table ( dim_treatments ) '''

print(treatments.columns)

treatments['treatment_date']=pd.to_datetime(treatments['treatment_date'])

treatments['cost_category']=pd.cut(
    treatments['cost'],
    bins=[0, 1000, 3000, 5000, float('inf')],
    labels=['Low', 'Medium', 'High', 'Very high'],
    include_lowest=True
)

dim_treatments=treatments[
    ['treatment_id',
    'treatment_type',
    'description',
    'cost',
    'cost_category']].copy()

dim_treatments.insert(0,'treatment_key', range(1, len(dim_treatments)+1))

print(dim_treatments.to_string())
print(dim_treatments.columns)



''' --Creating a new dimension table ( dim_date ) '''

appointments.rename(columns={'appointments_id' : 'appointment_id'}, inplace=True)

appointments['appointment_date']=pd.to_datetime(appointments['appointment_date'])

dim_date=pd.DataFrame(appointments['appointment_date'].drop_duplicates().sort_values().copy())

dim_date.reset_index(drop=True, inplace=True)

dim_date.rename(columns={'appointment_date' : 'full_date'}, inplace=True)

dim_date.insert(0,'date_key',dim_date['full_date'].dt.strftime("%Y%m%d").astype(int))

dim_date['month']=dim_date["full_date"].dt.month_name()

dim_date['month_num']=dim_date["full_date"].dt.month

dim_date['is_weekend']=np.where(dim_date['full_date'].dt.day_of_week.isin([5,6]),'Yes','No')

dim_date['quarter']=((dim_date['month_num']-1)//3)+1

print(dim_date.to_string())
print(dim_date.columns)



'''--Creating fact table ( fact_hospital )'''

print(appointments.columns)
print(treatments.columns)
print(billing.columns)


fact_hospital=appointments.merge(
    treatments[['treatment_id', 'appointment_id', 'treatment_type',
       'cost', 'treatment_date']],
    on='appointment_id',
    how='left'
)


fact_hospital=fact_hospital.merge(
    billing[['bill_id',  'treatment_id', 'amount',
       'payment_method', 'payment_status']],
    on='treatment_id',
    how='left'
)

fact_hospital.insert(0,'fact_id',range(1,len(fact_hospital)+1))

fact_hospital=fact_hospital.merge(
    dim_doctors[['doctor_id',  'doctor_key']],
    on='doctor_id',
    how='left'
)

fact_hospital=fact_hospital.merge(
    dim_patients[['patient_id',  'patient_key']],
    on='patient_id',
    how='left'
)

fact_hospital=fact_hospital.merge(
    dim_treatments[['treatment_id',  'treatment_key']],
    on='treatment_id',
    how='left'
)

fact_hospital=fact_hospital.merge(
    dim_date[['full_date',  'date_key']],
    left_on='appointment_date',
    right_on='full_date',
    how='left'
)

fact_hospital.rename(columns={'date_key' : 'appointment_date_key'}, inplace=True)

fact_hospital.drop(columns=
                   ['appointment_id', 'patient_id', 'doctor_id',
                    'treatment_id','bill_id', 'reason_for_visit'],
                    inplace=True)

print(fact_hospital.dtypes)
print(dim_doctors.dtypes)
print(dim_patients.dtypes)
print(dim_treatments.dtypes)
print(dim_date.dtypes)

print(fact_hospital.isna().sum())
print(dim_doctors.isna().sum())
print(dim_patients.isna().sum())
print(dim_treatments.isna().sum())
print(dim_date.isna().sum())
