from pony.orm import * 
from datetime import datetime

set_sql_debug(True)
db = Database()

class Patient(db.Entity):
    patientId = PrimaryKey(int)
    full_name = Optional(str)
    father_husband = Optional(str)
    contact = Optional(str)
    cnic = Optional(str)
    age = Optional(int)
    travel = Optional(str)
    diagnosed_date = Optional(datetime)
    hospital = Optional(str)
    district = Optional(str)
    town = Optional(str)
    home_address = Optional(str)
    current_residence = Optional(str)
    consulting_doctor = Optional(str)
    doctor_contact = Optional(str)
    lab = Optional(str)
    test_reason = Optional(str)
    status = Optional(str)

db.bind(provider='mysql', host='database-free-tier.c1g6uvkv8o2l.us-east-2.rds.amazonaws.com', user='admin', passwd='Mysqlid1', db='covid19')
db.generate_mapping(create_tables=True)

@db_session
def add_patient(patientId, full_name, father_husband, contact, cnic, age, travel, diagnosed_date, district, town, home_address, current_residence, doctor_contact, lab, test_reason, status):
    Patient(patientId = patientId, full_name = full_name, father_husband = father_husband, 
    contact = contact, cnic = cnic, age = age, travel = travel, diagnosed_date = diagnosed_date, 
    district = district, town = town, home_address = home_address, current_residence = current_residence, 
    doctor_contact = doctor_contact, lab = lab, test_reason = test_reason, status = status)

