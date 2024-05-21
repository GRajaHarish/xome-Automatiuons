import ctypes
import json
import logging
import time
import webbrowser
import imaplib
import email
#from bs4 import BeautifulSoup
import mysql
import mysql.connector
import requests
import re
import sys
from datetime import datetime as DT
#from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import threading
import queue
from datetime import datetime, timedelta
from XomeLogin import PortolLogin
# from XomeForm import FormData

from stdlib.ip_checking import ip_address_checking
import logging

def x_completed():
    url = 'http://13.200.17.36/autobpo_test/Home/GetBPO_Completed?stateId=0'
    response = requests.get(url)
    if response.status_code == 200:
       content_string = response.content
       data_dict = json.loads(content_string)
       dataset=json.loads(data_dict['Data']['Clientcnt'])    
 
       if dataset:
            ip_check= ip_address_checking()
            subclientName=dataset[0]['subclient']   
            xome_orderlist=[]
            for x in dataset:  
                ip_check=='198.98.15.235'  
                if x['soft_portal_name']=="Xome": #and x['subclient']=="Ashley": # and ip_check=='198.98.15.235' and x['subclient']=="Daniel Pacut" and x['broker_name']=="Bang":
                    if x['subclient'] in xome_orderlist:
                            pass
                    else:
                        xome_orderlist.append(x)  
                        logging.info("Xome Order list Bang Clients Fetched from Dashboard :{}".format(xome_orderlist.append(x)))
            if len(xome_orderlist)>0:
                print("length ",len(xome_orderlist))
                logging.info("length xome Order list :{}".format(len(xome_orderlist)))
                print("threading starting")
                t = threading.Thread(target=PortolLogin, args=(subclientName,))
                t.start()
                t.join()
                
x_completed()