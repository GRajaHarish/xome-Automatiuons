import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from conditions import condition_data
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

def findorderTYPE(driver,address,order_details,merged_json):
    subclient = order_details['subclient']
    print('Finding Order type for Client --------------------------------------------------',subclient)
    merged_json=condition_data(merged_json,subclient)
    global chromedriver
    chromedriver=driver
    OrderProgressTab=chromedriver.find_element(By.XPATH,"/html/body/div/div[3]/div[2]/div/div[2]/div[3]/ul/li[2]/a")
    OrderProgressTab.click()
    table = chromedriver.find_element(By.ID, "OrdersInProgressGrid")
    rows = table.find_elements(By.XPATH, ".//tbody/tr")
    merge_text_path = []
    subject_property_texts = []
    data = {}
    for row_index, row in enumerate(rows, start=1):
        
        ordertypeXpath = row.find_element(By.XPATH, ".//td[1]")
        ordertypeLink = ordertypeXpath.text
        orderlinkXpath = f"//*[@id='OrdersInProgressGrid']/tbody/tr[{row_index}]/td[1]/div/a[@id='oip-cBPO-link']"
        form_type = row.find_element(By.XPATH, f"//*[@id='OrdersInProgressGrid']/tbody/tr[{row_index}]/td[4]").text
        merge_text_path.append((ordertypeLink, orderlinkXpath,form_type))
        try:
          subject_property_text = row.find_element(By.XPATH, ".//td[contains(@class, 'SubjectProperty')]").text.split()[0]
        except:
          subject_property_text = "N/A"
        subject_property_texts.append(subject_property_text)
        data[subject_property_text] = (ordertypeLink, orderlinkXpath,form_type)
    logging.info(json.dumps(data,indent=4))
    openOrderType(data,address,merged_json,order_details)

def openOrderType(data,address,merged_json,order_details):
    print(data,address)
    address=address.split()[0]
    orderlist=["cBPO Ext (u)", "cBPO Ext (n)", "cBPO Ext (a)","cBPO Ext (x) 72hr", "cEval Ext (b)", "cBPO Ext (x) AVR","Exterior PCR Only"]
    if address in data:
        info = data[address]
        if info:
            for order_type in orderlist:
                if order_type in info[2]:
                        clickFormType=BtnClick(info[1],chromedriver)
                        if clickFormType == "done":
                            print("form type identified", clickFormType)
                            logging.info("Entry already filled")
                            # statuschange(order_details['order_id'], "25", "3", "14")
                            ChangeTonewTab(chromedriver)
                            viewFormBtnXpath="/html/body/div[1]/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/a[6]"
                            time.sleep(10)
                            viewFormbtnClick=BtnClick(viewFormBtnXpath,chromedriver)
                            if viewFormbtnClick == "done":
                                print("started form filling////////////////////////////////////////")
                                with open('connectors/cbpo x.json') as f:
                                  data = json.load(f)
                                orderid=order_details['order_id']
                                from Xome_EXT_form_filling import Formnewbpoext
                                init = Formnewbpoext()
                                init.form(merged_json,chromedriver,orderid, data) 
                            else:
                                time.sleep(20)
                                viewFormXpath="/html/body/div[1]/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div/div/div/div/div/a"
                                viewFormClick=BtnClick(viewFormXpath,chromedriver)
                                if viewFormClick=="done":
                                    print("view btn  found")
                                else:
                                    print("view form button not fount")
                        else:
                            print("Fresh Form Identified ................................................................................")
                               
        else:
            print("address not found in portal")
    else:
            print("address not match in portal")
   

def BtnClick(xpath,driver):
    btn=driver.find_elements(By.XPATH,xpath)
    if btn:
       btn[0].click()
       return "done"
    else:
       return "element not fount"

def ChangeTonewTab(driver):
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[-1])  # Switch to the latest opened tab
    return driver
    

     
