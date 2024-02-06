# cis6930sp24 -- Assignment0 -- Norman Police Incident Data Extraction

## Name:
Pranil Ingle

## Assignment Description:
This assignment involves extracting incident data from the Norman, Oklahoma police department's website, reformatting it, and storing it in an SQLite database. The extracted data includes fields such as Date/Time, Incident Number, Location, Nature, and Incident ORI. The project is implemented in Python 3 and involves downloading PDF files, parsing them, creating a SQLite database, and generating incident summaries.

## How to Install:
Clone the repository:

git clone https://github.com/CodeRanger1998/dataEngineeringProject0
cd dataEngineeringProject0

Install dependencies using Pipenv:

pipenv install

## How to Run:

Execute the main script providing the incident summary URL:

pipenv run python assignment0/main.py --incidents <url>

Replace <url> with the URL of the incident summary PDF file.

## Functions:

functions.py

sqlConnect(dbName): Connects to an SQLite database and creates an incidents table.

insertData(con,incidents): Inserts data into the SQLite database.

getDataFromSQLite(con): Retrieves data from the SQLite database.

convertPdfDataToJSON(pdfData): Converts PDF data to JSON format.

getDataFromWeb(urlString): Fetches PDF data from the web.

Bugs and Assumptions:
Assumption: Incident data is available in PDF format on the Norman police department's website.
Assumption: Each incident PDF file contains structured data with consistent formatting.