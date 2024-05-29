import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import logging

def findorderTYPE(driver,address,cookies):
    global chromedriver
    chromedriver=driver
    OrderProgressTab=chromedriver.find_element(By.ID,"inProgressOrdersTab")
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
    openOrderType(data,address)

def openOrderType(data,address):
    print(data,address)
    address=address.split()[0]
    orderlist=["cBPO Ext (u)", "cBPO Ext (n)", "cBPO Ext (a)", "cEval Ext (b)", "cBPO Ext (x) AVR","Exterior PCR Only"]
    if address in data:
        info = data[address]
        if info:
            for order_type in orderlist:
                if order_type in info[2]:
                    order = chromedriver.find_elements(By.XPATH,info[1] )
                    if order:
                        openIdentifiedForm(order[0])
                    else:
                        print(info[1])
                        print("Order type not found unable to do this order ")
                    break  
        else:
            print("address not found in portal")
    else:
            print("address not match in portal")
   

def openIdentifiedForm(xpath):
     print("Order type found")
     xpath.click()
     viewFormBTN = chromedriver.find_element(By.ID, "button-1048-btnEl")
     viewFormBTN.click()
     print("Openingform")
     
     
