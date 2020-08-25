import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

dataComplete = []
startPatientId = 1
endPatientId = 1
cookieId = input("Cookie Id: ")


def fetchPatientData(id):
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
                columnName = "Comorbidities"
            columnValue = tempColumnValue[:tempColumnValue.find("Change")].strip() if tempColumnValue.find(
                "Change") != -1 else tempColumnValue.strip()

            if columnName == "Comorbidities":
                commorbity.append(columnValue)
                dataDictionarySinglePerson[columnName] = commorbity
            else:
                dataDictionarySinglePerson[columnName] = columnValue

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
        historyTableSingleRowData = ""
        for index in range(len(tdsRow)):
            if (tdsRow[index].text).strip() == "":
                historyTableSingleRowData += "Null" + "*"
            else:
                historyTableSingleRowData += tdsRow[index].text + "*"
        historyTableArrayComplete.append(historyTableSingleRowData)
    dataDictionarySinglePerson["testHistoryData"] = historyTableArrayComplete
    return dataDictionarySinglePerson


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": cookieId,
    "Host": "covid19.sindhmonitoringcell.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
}
# 1277, 1276, 102091,129441,3288
# ci_session=9c3eevklbn3uevp966vh7c7m67ulb50d
with requests.Session() as s:
    isNotValidInput = True
    while isNotValidInput:
        try:
            startPatientId = input("Enter starting Patient ID: ")
            endPatientId = input("Enter ending Patient ID: ")
            startPatientId = int(startPatientId)
            endPatientId = int(endPatientId)
            isNotValidInput = False
        except:
            print("\nEnter Valid Starting ID and Ending ID of patients!\n")

    for id in range(startPatientId, endPatientId + 1):
        singlePatientData = fetchPatientData(id)
        if singlePatientData.get("Full Name:") == "" and singlePatientData.get(
                "Father Name , W/O:") == "" and singlePatientData.get("Contact :") == "" and singlePatientData.get(
                "CNIC :") == "":
            print("Not Valid Patient ID!\nSkipping this ID.....")
        else:
            dataComplete.append(singlePatientData)

    print("\nComplete Data Below:\n", dataComplete)

# Write to file
f = open(f"dataFrom{startPatientId}to{endPatientId}.json", "w")
f.write(json.dumps(dataComplete))
f.close()

df = pd.read_json(f"dataFrom{startPatientId}to{endPatientId}.json")
df.to_excel(f"dataFrom{startPatientId}to{endPatientId}.xlsx")

