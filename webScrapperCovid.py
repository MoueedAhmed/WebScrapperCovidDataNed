from db import add_patient
from fetchPatientData import fetchPatientData


# 1277, 1276, 102091,129441,3288
# ci_session=9c3eevklbn3uevp966vh7c7m67ulb50d

#Scrapping data of single patient
patient = fetchPatientData(102091)

# add_patient(patient["patientId"], patient["full_name"], patient["father_husband"], 
# patient["contact"], patient["cnic"], patient["age"], patient["travel"], patient["diagnosed_date"], 
# patient["district"], patient["town"], patient["home_address"], patient["current_residence"], 
# patient["doctor_contact"], patient["lab"], patient["test_reason"], patient["status"])











