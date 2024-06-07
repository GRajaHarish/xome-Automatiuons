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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import threading
import queue
from datetime import datetime, timedelta
from XomeLogin import ClientLogin
# from DataMerg import DataFilling
from stdlib.ip_checking import ip_address_checking
import logging

def x_completed():
    print("\n  Smart Entry Xome started   ......................................................................")
    url = 'http://13.200.17.36/autobpo_test/Home/GetBPO_Completed?stateId=0'
    response = requests.get(url)
    if response.status_code == 200:
       content_string = response.content
       data_dict = json.loads(content_string)
       dataset=json.loads(data_dict['Data']['Clientcnt'])    
       if dataset:
            ip_check= ip_address_checking()   
            xome_orderlist=[]
            for x in dataset:  
                ip_check=='198.98.15.235'  
                if x['soft_portal_name']=="Xome": #and x['subclient']=="Ashley": # and ip_check=='198.98.15.235' and x['subclient']=="Daniel Pacut" and x['broker_name']=="Bang":

                    if x['subclient'] in xome_orderlist:
                            pass
                    else:
                        xome_orderlist.append(x)  
                        logging.info("Xome Order list  Clients Fetched from Dashboard :{}".format(x))
            print("Total Number of xome orders =",len(xome_orderlist))
            threads=[]
            if len(xome_orderlist)>0:
                logging.info("length xome Order list :{}".format(len(xome_orderlist)))
                if len(xome_orderlist)>=15:
                    for x in range(15):   
                        t = threading.Thread(target=ClientLogin, args=(xome_orderlist[x],))
                        threads.append(t)
                elif len(xome_orderlist)==1:
                        t = threading.Thread(target=ClientLogin, args=(xome_orderlist[0],))
                        threads.append(t)
                else:
                    for x in range(len(xome_orderlist)):   
                        t = threading.Thread(target=ClientLogin, args=(xome_orderlist[x],))
                        threads.append(t)
                    # Wait for all threads to complete
                for t in threads:
                    t.start()
                for t in threads:
                    t.join()
                x_completed() 
            else:
                x_completed()  
       else:
            x_completed()
    else:
        x_completed()
#-----------------------------------------------------------------------------------------------------#
      
if __name__ == '__main__':x_completed()
           

