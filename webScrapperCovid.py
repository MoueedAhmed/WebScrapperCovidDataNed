from db import db_session, PatientBasic, PatientComorbidities, PatientFollowUpCircleData, PatientFollowUpOtherData, PatientTestHistoryData
from fetchPatientData import fetchPatientData

# 1277, 1276, 102091,129441,3288
# ci_session=9c3eevklbn3uevp966vh7c7m67ulb50d

#Scrapping data of single patient
patient = fetchPatientData(3288)
patient_comorbidities = patient["comorbidities"]
patient_followup_circledata = patient["followUpCircleData"]
patient_followup_otherdata = patient["followUpOtherData"]
patient_test_history_data = patient["testHistoryData"]

print(patient)

with db_session:
   PatientBasic(patientId=patient["patientId"], full_name=patient["full_name"], father_husband=patient["father_husband"], 
   contact=patient["contact"], cnic=patient["cnic"], age=patient["age"], travel=patient["travel"], diagnosed_date=patient["diagnosed_date"], 
   district=patient["district"], town=patient["town"], home_address=patient["home_address"], current_residence=patient["current_residence"], 
   doctor_contact=patient["doctor_contact"], lab=patient["lab"], test_reason=patient["test_reason"], status=patient["status"])

   for comorbidity in patient_comorbidities:
      PatientComorbidities(patientId=patient["patientId"], comorbidity=comorbidity)

   for circle in patient_followup_circledata:
      PatientFollowUpCircleData(patientId=patient["patientId"], circle=circle)

   for other in patient_followup_otherdata:
      PatientFollowUpOtherData(patientId=patient["patientId"], other=other)

   for rowHistory in patient_test_history_data:
      PatientTestHistoryData(patientId=patient["patientId"], sno=rowHistory[0], test_date=rowHistory[1], result=rowHistory[2], 
      lab=rowHistory[3], remarks=rowHistory[4], updated_by=rowHistory[5], option=rowHistory[6])









