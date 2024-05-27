from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import json
from utility import ExecuteQuery
def DataFilling():
    html_file_path = "E:\PROJRCT XOME\cBPO Ext (u)\Marketprice.html"

    # driver.get("file://" + html_file_path)
    query = """
        SELECT * 
        FROM entry_data 
        WHERE OrdID IN (
        SELECT t2.OrdID 
        FROM subject AS t1 
        JOIN entry_data AS t2 
        ON t1.OrdID = t2.OrdID 
        WHERE t1.OrdID LIKE ''
        )
"""
    
    FomValues=ExecuteQuery(query,"db2")

    print(FomValues)
DataFilling() 