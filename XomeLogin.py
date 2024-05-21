from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from utility import ExecuteQuery

def PortolLogin(subclientName):

    query="select * from adjustments"
    FomValues=ExecuteQuery(query,"db1")
    chrome_options = Options()
    chrome_options.add_argument("--start-fullscreen") 
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get("https://vendor.voxturappraisal.com/Account/Login")
        username_field = driver.find_element(By.ID, "Login_Username")
        password_field = driver.find_element(By.ID, "Login_Password")
        login_button = driver.find_element(By.ID, "BtnLogin")
        username_field.send_keys("your_username")
        password_field.send_keys("your_password")
        login_button.click()
        time.sleep(30)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser
        driver.quit()


    
    