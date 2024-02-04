import urllib.request
import io  
from PyPDF2 import PdfReader
import re
import sqlite3

def sqlConnect(dbName):
    con = sqlite3.connect("resources/"+dbName)
    cur = con.cursor()
    cur.execute("CREATE TABLE incidents(incidentDate TEXT, address TEXT, incidentNumber TEXT,nature TEXT)")
    return con

def insertData(con,incidents):
    cur = con.cursor()
    cur.executemany("INSERT INTO incidents VALUES(?, ?, ?,?)", incidents)
    con.commit()  # Remember to commit the transaction after executing INSERT.

def getDataFromSQLite(con):
    cur = con.cursor()
    data = cur.execute(""" 
        SELECT nature,COUNT(*) FROM incidents GROUP BY nature ORDER BY COUNT(*) DESC,nature;
""")
    return data

def convertPdfDataToJSON(pdfData):
    reader = PdfReader(pdfData)
    pages = reader.pages
    incidents = []
    oldAddress=None
    oldIncidentNumber = None
    oldDate = None
    start=False
    for page in pages:
        pageText = page.extract_text()
        pageLines = pageText.splitlines()
        for pageLine in pageLines:
            if start:
                # print(pageLine)
                incidentOri = re.split(" ",pageLine)[-1]
                pageLine = re.split(incidentOri,pageLine)[0].strip()
                # address = re.search("([A-Z]?[a-z]+/*\s*)+",pageLine)
                nature = re.search("(COP DDACTS)|(CIR)?(COP)?(MVA)?(911)?(EMS)?\\s*[A-Z][a-z]+.*",pageLine)
                nature = nature.group().strip()
                address = oldAddress + re.split(nature,pageLine)[0].strip()
                incidents.append((oldDate,address,oldIncidentNumber,nature))
                # print((oldDate,address,oldIncidentNumber,nature))
                oldAddress=None
                oldIncidentNumber = None
                oldDate = None
                start=False
            pageLine = pageLine.replace('NORMAN POLICE DEPARTMENT','')
            incidentDate = re.search("[0-9]+/[0-9]+/[0-9]{4} [0-9]+:[0-9]+",pageLine)
            if incidentDate != None:
                incidentDate = incidentDate.group()
                pageLine = re.split(incidentDate,pageLine)[1].strip()
                if len(pageLine)>0:
                    incidentNumber = re.search("[0-9]{4}-[0-9]+",pageLine)
                    incidentNumber = incidentNumber.group()
                    pageLine = re.split(incidentNumber,pageLine)[1].strip()
                    incidentOri = re.split(" ",pageLine)[-1]
                    pageLine = re.split(incidentOri,pageLine)[0].strip()
                    # address = re.search("([A-Z]?[a-z]+/*\s*)+",pageLine)
                    nature = re.search("(COP DDACTS)|(COP)?(MVA)?(911)?(EMS)?\\s*[A-Z][a-z]+.*",pageLine)
                    if nature==None and len(pageLine)>0:
                        # print(1,pageLine)
                        oldIncidentNumber = incidentNumber
                        oldDate = incidentDate
                        oldAddress = pageLine + incidentOri
                        start = True
                        continue
                    elif nature == None:
                        continue
                    nature = nature.group().strip()
                    address = re.split(nature,pageLine)[0].strip()
                    incidents.append((incidentDate,address,incidentNumber,nature))
    return incidents

                
def getDataFromWeb(urlString):
    url = (urlString)
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"                          
    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()  
    memoryObject = io.BytesIO(data) 
    return memoryObject                                                                          