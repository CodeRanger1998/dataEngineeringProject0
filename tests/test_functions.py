import sys
from assignment0 import functions
import random

"""
Testing functions sqlConnect, insertData and getDataFromSQLite
"""
def test_database():
    try:
        con = functions.sqlConnect("fortest"+str(random.randint(0,1000)))
        if con != None:
            try:
                functions.insertData(con,[("1","2","3","4","5")])
            except Exception as e2:
                print("Error while inserting " +  str(e2),file=sys.stderr)
                assert False
            try:
                dataFromDb = functions.getDataFromSQLite(con)
                if dataFromDb.rowcount > 0:
                    assert True
            except Exception as e3:
                print("Error while inserting " +  str(e3),file=sys.stderr)
                assert False
            assert True
        else:
            print("Error while connecting ")
            assert False
    except Exception as e:
        print("Error while connecting "+ str(e),file=sys.stderr)
        assert False

"""
Testing function getDataFromWeb
"""
def test_getDataFromWeb():
    try:
        webData = functions.getDataFromWeb('https://www.google.com')
        assert True
    except Exception as e:
        print("Error while getting data "+ str(e),file=sys.stderr)
        assert False

"""
Testing function convertPdfDataToJSON
"""
def test_convertPdfDataToJSON():
    try:
        data = functions.convertPdfDataToJSON('resources/test.pdf')
        if len(data) == 328:
            assert True
        else:
            print("Error while getting data "+str(len(data)),file=sys.stderr)
            assert False
    except Exception as e:
        print("Error while converting data "+ str(e),file=sys.stderr)
        assert False