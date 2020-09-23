from pony.orm import Database, Optional, PrimaryKey, set_sql_debug, db_session
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

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

db.bind(provider=os.getenv("PROVIDER"), host=os.getenv("HOST"), user=os.getenv("USERDB"), passwd=os.getenv("PASSWD"), db=os.getenv("DB"))
db.generate_mapping(create_tables=True)

@db_session
def add_patient(patientId, full_name, father_husband, contact, cnic, age, travel, diagnosed_date, district, town, home_address, current_residence, doctor_contact, lab, test_reason, status):
    Patient(patientId = patientId, full_name = full_name, father_husband = father_husband, 
    contact = contact, cnic = cnic, age = age, travel = travel, diagnosed_date = diagnosed_date, 
    district = district, town = town, home_address = home_address, current_residence = current_residence, 
    doctor_contact = doctor_contact, lab = lab, test_reason = test_reason, status = status)

