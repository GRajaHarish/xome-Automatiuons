from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from utility import ExecuteQuery
import logging
from selenium.webdriver.support import expected_conditions as EC
from Xome_form_identification_open import findorderTYPE
from StatusChange import statuschange

def ClientLogin(order_details,subclientName,broker_name):
    statuschange(order_details['order_id'],"24","5","19")
    try:
       query = "SELECT username,password,status,ats_client_id FROM allclients WHERE form = 'xome' AND Mainclient = '"+broker_name+"' AND Subclient = '"+subclientName+"'"
       ClientDetails=ExecuteQuery(query,"Client")
    except Exception as e:
        print(f"An error occurred: {e}")   
    if ClientDetails:      
       logging.info("client found")
    else:
         print("Account Not found")   
         logging.info("Account Not found:")
         statuschange(order_details['order_id'],"22","3","14")
    if ClientDetails[0][2] == "Active":
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
            time.sleep(90)
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
            # Close the browser
            print("browser_closed")
            time.sleep(9)
            driver.quit()
    else:
        print('Bad Password')
        logging.info('Bad Password')
        statuschange(order_details['order_id'],"23","3","14")


    
    