# -*- coding: utf-8 -*-
# Example main.py
import argparse
import functions

def main(url):
    con = functions.sqlConnect("normanpd.db")
    webData = functions.getDataFromWeb(url)
    incidents = functions.convertPdfDataToJSON(webData)
    functions.insertData(con=con,incidents=incidents)
    data = functions.getDataFromSQLite(con)
    total = 0
    for unit in data:
        total = total + unit[1]
        print(str(unit[0])+'|'+str(unit[1]))
    # print(total)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, 
                         help="Incident summary url.")
     
    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)

