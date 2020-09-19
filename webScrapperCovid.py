import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

#-------------------------------------------------------fetchPatientData Start--------------------------------------------------------------------------#
def fetchPatientData(id):
    cookieId = "ci_session=9c3eevklbn3uevp966vh7c7m67ulb50d"
    headers = {
        "Cookie": cookieId
    }
    with requests.Session() as s:
        print("\nFetching data of Patient ID: " + str(id))
        patientId = id
        dataDictionarySinglePerson = {}
        url = 'http://covid19.sindhmonitoringcell.com/dashboard/patientDetails?id=' + str(patientId)
        dataDictionarySinglePerson["patientId"] = patientId
        htmlContent = s.get(url, headers=headers).text
        soup = BeautifulSoup(htmlContent, "html.parser")

        # getting patient details
        divs = soup.find_all("div", attrs={"class": "row mgbt-xs-0"})
        commorbity = []
        for div in divs:
            if div.label != None and div.div != None:
                columnName = div.label.text
                tempColumnValue = div.div.text

                if columnName == "":
                    columnName = "comorbidities"
                columnValue = tempColumnValue[:tempColumnValue.find("Change")].strip() if tempColumnValue.find(
                    "Change") != -1 else tempColumnValue.strip()

                if columnName == "comorbidities":
                    commorbity.append(columnValue)
                    dataDictionarySinglePerson[columnName] = commorbity
                else:
                    if columnName == "Full Name:":
                        dataDictionarySinglePerson["full_name"] = columnValue
                    elif columnName == "Father Name , W/O:":
                        dataDictionarySinglePerson["father_husband"] = columnValue
                    elif columnName == 'Contact :':
                        dataDictionarySinglePerson["contact"] = columnValue
                    elif columnName == 'CNIC :':
                        dataDictionarySinglePerson["cnic"] = columnValue
                    elif columnName == 'Age:':
                        dataDictionarySinglePerson["age"] = columnValue
                    elif columnName == 'Travel:':
                        dataDictionarySinglePerson["travel"] = columnValue
                    elif columnName == 'Date Diagnosed:':
                        dataDictionarySinglePerson["diagnosed_date"] = columnValue
                    elif columnName == 'Hospital:':
                        dataDictionarySinglePerson["hospital"] = columnValue
                    elif columnName == 'District:':
                        dataDictionarySinglePerson["district"] = columnValue
                    elif columnName == 'Town:':
                        dataDictionarySinglePerson["town"] = columnValue
                    elif columnName == 'Home Address:':
                        dataDictionarySinglePerson["home_address"] = columnValue
                    elif columnName == 'Current Residence:':
                        dataDictionarySinglePerson["current_residence"] = columnValue
                    elif columnName == 'Consulting Doctor:':
                        dataDictionarySinglePerson["consulting_doctor"] = columnValue
                    
                    elif columnName == 'Doctor Contact:':
                        dataDictionarySinglePerson["doctor_contact"] = columnValue
                    elif columnName == 'Lab Name:':
                        dataDictionarySinglePerson["lab"] = columnValue
                    elif columnName == 'Reason for Test':
                        dataDictionarySinglePerson["test_reason"] = columnValue

        # getting patient status
        status = soup.find("button", attrs={"class": "btn vd_btn vd_bg-linkedin"}).text
        dataDictionarySinglePerson["status"] = status

        # getting dateNegative From test history data
        historyTable = soup.find("table", attrs={"class": "table table-condensed table-bordered"})
        historyTableRows = historyTable.tbody.find_all("tr")
        for tr in historyTableRows:
            tds = tr.find_all("td")
            if tds[2].text == "Negative":
                dateNegative = tds[1].text
                dataDictionarySinglePerson["dateNegative"] = dateNegative
                break

        # getting patient followup details circle data
        lis = soup.find_all("li", attrs={"class": "tl-item"})
        followupArray = []
        for li in lis:
            timeDiv = li.find("div", attrs={"class": "tl-date"}).text
            followupArray.append(timeDiv)
        dataDictionarySinglePerson["followUpCircleData"] = followupArray

        # getting patient followup details other data
        lis = soup.find_all("li", attrs={"class": "tl-item"})
        followupOtherArray = []
        for li in lis:
            otherDiv = li.find("div", attrs={"class": "tl-label"}).div.text
            followupOtherArray.append(otherDiv.strip())
        dataDictionarySinglePerson["followUpOtherData"] = followupOtherArray

        # getting test history data
        historyTable = soup.find("table", attrs={"class": "table table-condensed table-bordered"})
        historyTableRows = historyTable.tbody.find_all("tr")
        historyTableArrayComplete = []
        for tr in historyTableRows:
            tdsRow = tr.find_all("td")
            historyTableSingleRowData = []
            for index in range(len(tdsRow)):
                if (tdsRow[index].text).strip() == "":
                    historyTableSingleRowData.append(tdsRow[index].text)
                else:
                    historyTableSingleRowData.append(tdsRow[index].text)
            historyTableArrayComplete.append(historyTableSingleRowData)
        dataDictionarySinglePerson["testHistoryData"] = historyTableArrayComplete
        print(dataDictionarySinglePerson)
    return dataDictionarySinglePerson
#-------------------------------------------------------fetchPatientData End--------------------------------------------------------------------------#

# 1277, 1276, 102091,129441,3288
# ci_session=9c3eevklbn3uevp966vh7c7m67ulb50d
#---------------------------------------------------------------Main Start------------------------------------------------------------------------------#

#getting data
fetchPatientData(129441)



#---------------------------------------------------------------Main End------------------------------------------------------------------------------#