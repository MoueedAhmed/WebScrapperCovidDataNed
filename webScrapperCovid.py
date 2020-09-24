from db import add_patient_basic, add_patient_comorbidities, add_patient_followup_circledata, add_patient_followup_otherdata, add_patient_test_history_data
from fetchPatientData import fetchPatientData

# 1277, 1276, 102091,129441,3288
# ci_session=9c3eevklbn3uevp966vh7c7m67ulb50d

#Scrapping data of single patient
patient = fetchPatientData(129441)
patient_comorbidities = patient["comorbidities"]
patient_followup_circledata = patient["followUpCircleData"]
patient_followup_otherdata = patient["followUpOtherData"]
patient_test_history_data = patient["testHistoryData"]

print(patient)

add_patient_basic(patient["patientId"], patient["full_name"], patient["father_husband"], 
patient["contact"], patient["cnic"], patient["age"], patient["travel"], patient["diagnosed_date"], 
patient["district"], patient["town"], patient["home_address"], patient["current_residence"], 
patient["doctor_contact"], patient["lab"], patient["test_reason"], patient["status"])

for comorbidity in patient_comorbidities:
   add_patient_comorbidities(patient["patientId"], comorbidity)

for circleData in patient_followup_circledata:
   add_patient_followup_circledata(patient["patientId"], circleData)

for other in patient_followup_otherdata:
   add_patient_followup_otherdata(patient["patientId"], other)

for rowHistory in patient_test_history_data:
   add_patient_test_history_data(patient["patientId"], rowHistory[0], rowHistory[1], rowHistory[2], rowHistory[3], rowHistory[4], rowHistory[5], rowHistory[6])










