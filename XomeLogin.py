from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from utility import ExecuteQuery
import logging
import threading
import queue
from selenium.webdriver.support import expected_conditions as EC
from Xome_form_identification_open import findorderTYPE
from StatusChange import statuschange
from Xome_JSON_data_fetching_db import formdata_fetching_db
def ClientLogin(order_details):
   #  #statuschange(order_details['order_id'],"24","5","19")
    subclientName=order_details['subclient']
    broker_name=order_details['broker_name'] 
    address=order_details['subject_address']
    print("clientname ",subclientName)
    if broker_name == "ECESIS":
     broker_name=subclientName
    else:
     broker_name=broker_name  
    print("mainclient" ,broker_name ,"subclient",subclientName)
    try:
       result_queue = queue.Queue()
       t1 = threading.Thread(target= formdata_fetching_db, args=(result_queue,order_details))
       t1.start()
       query = "SELECT username,password,status,ats_client_id FROM allclients WHERE form = 'xome' AND Mainclient = '"+broker_name+"' AND Subclient = '"+subclientName+"'"
       ClientDetails=ExecuteQuery(query,"Client")
    except Exception as e:
        print(f"An error occurred: {e}")   
    if ClientDetails:      
       logging.info("client found")
       flag=1
    else:
         print("Account Not found")   
         logging.info("Account Not found:")
         #statuschange(order_details['order_id'],"22","3","14")
         flag=0
    if ClientDetails[0][2] == "Active" and flag == 1:
         loginginto_Portal(ClientDetails)
         t1.join()
         results = []
         while not result_queue.empty():
               results.append(result_queue.get())
               # print(results)
               logging.info("Results:{}".format(results))
         merged_json=results[0]
          #print(merged_json)
         logging.info("merged_json in ss_form_processing:{}".format(merged_json))
          
         try:
               #print("merged_json['QC']   ",merged_json['QC'])
               QC=merged_json['QC']
               logging.info("QC Count:{}".format(QC))
         except Exception as ex:
               QC="0"
               print('Exception rised ..', ex)
               logging.info("Exception rised in QC..:{}".format(ex))
          #print("QC ",QC)
         if QC=="0" or QC=="null" or QC=="" or QC is None:
               findorderTYPE(orders,session,merged_json,order_details)
    else:
        print('Bad Password')
        logging.info('Bad Password')
        #statuschange(order_details['order_id'],"23","3","14")     

def loginginto_Portal(ClientDetails):
       logging.info("client Active")
       username,password,clientid=ClientDetails[0][0],ClientDetails[0][1],ClientDetails[0][3]
       chrome_options = Options()
       chrome_options.add_argument("--start-fullscreen") 
       driver = webdriver.Chrome(options=chrome_options)
       try:
            driver.get("https://vendor.voxturappraisal.com/Account/Login")
            username_field = driver.find_element(By.ID, "Login_Username")
            password_field = driver.find_element(By.ID, "Login_Password")
            login_button = driver.find_element(By.ID, "BtnLogin")
            username_field.send_keys(username)
            password_field.send_keys(password)
            login_button.click()
            WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "Login_SecurityCode"))
            )
            time.sleep(50)
            OtpQuery ="SELECT Code FROM xomeverificationcode where clientid ='"+clientid+"' ORDER BY timestamp DESC LIMIT 1"
            otp=ExecuteQuery(OtpQuery,"otp")
            otpvalue=otp[0][0]
            OTP_field = driver.find_element(By.ID, "Login_SecurityCode")
            OTP_field.send_keys(otpvalue)
            OTP_button = driver.find_element(By.ID, "BtnLogin")
            OTP_button.click()  
           
            WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "inProgressOrdersTab"))
            )
            findorderTYPE(driver,address)
       except Exception as e:
            print(f"An error occurred: {e}")
       finally:
            print("browser_closed")
            driver.quit()   


    
    