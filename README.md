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

### `sqlConnect(dbName)`
- **Description:** Connects to an SQLite database and creates an incidents table if it doesn't exist.
- **Parameters:**
  - `dbName`: Name of the SQLite database file.
- **Returns:** SQLite connection object.
- **Functionality:**
  - Connects to the SQLite database specified by `dbName`.
  - If the database doesn't exist, it creates a new one.
  - Creates an `incidents` table with columns for `incidentDate`, `address`, `incidentNumber`, `nature`, and `incidentOri`.
  - Returns the SQLite connection object.

### `insertData(con, incidents)`
- **Description:** Inserts incident data into the SQLite database.
- **Parameters:**
  - `con`: SQLite connection object.
  - `incidents`: List of tuples containing incident data.
- **Returns:** None.
- **Functionality:**
  - Takes the SQLite connection object `con` and a list of tuples `incidents` as input.
  - Uses the SQLite cursor to execute an `INSERT` statement for each incident tuple in the list.
  - Commits the transaction to save the changes to the database.
  - Does not return any value.

### `getDataFromSQLite(con)`
- **Description:** Retrieves data from the SQLite database.
- **Parameters:**
  - `con`: SQLite connection object.
- **Returns:** Result set containing incident data.
- **Functionality:**
  - Takes the SQLite connection object `con` as input.
  - Executes an SQL query to select incident data from the `incidents` table.
  - Returns the result set containing the selected data.

### `convertPdfDataToJSON(pdfData)`
- **Description:** Converts PDF data to JSON format.
- **Parameters:**
  - `pdfData`: PDF data in byte format.
- **Returns:** List of tuples containing incident data.
- **Functionality:**
  - Takes PDF data in byte format `pdfData` as input.
  - Parses the PDF content using PyPDF2 library.
  - Extracts incident data such as incident date, address, incident number, nature, and incident ORI from each page of the PDF.
  - Returns a list of tuples, with each tuple representing an incident and containing the extracted data.

### `getDataFromWeb(urlString)`
- **Description:** Fetches PDF data from the web.
- **Parameters:**
  - `urlString`: URL of the web page containing the PDF data.
- **Returns:** PDF data in byte format.
- **Functionality:**
  - Takes the URL string `urlString` as input.
  - Uses urllib to open the URL and fetches the PDF data.
  - Returns the PDF data in byte format.

Bugs and Assumptions:
Assumption: Incident data is available in PDF format on the Norman police department's website.
Assumption: Each incident PDF file contains structured data with consistent formatting.