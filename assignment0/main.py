import argparse
import functions

"""
Calling functions from functions.py and printing to standard output.
"""
def main(url):
    webData = functions.getDataFromWeb(url)
    incidents = functions.convertPdfDataToJSON(webData)
    con = functions.sqlConnect("normanpd.db")
    functions.insertData(con=con,incidents=incidents)
    data = functions.getDataFromSQLite(con)
    for unit in data:
        print(str(unit[0])+'|'+str(unit[1]))

"""
Extracting incidents url from command line arguments
"""
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, 
                         help="Incident summary url.")
     
    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)

