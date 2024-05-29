import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from conditions import condition_data
import time
import logging

def findorderTYPE(driver,address,order_details):
    subclient = order_details['subclient']
    merged_json=condition_data(merged_json,subclient)
    global chromedriver
    chromedriver=driver
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
          subject_property_text = row.find_element(By.XPATH, ".//td[contains(@class, 'SubjectProperty')]").text
        except:
          subject_property_text = "N/A"
        subject_property_texts.append(subject_property_text)
        data[subject_property_text] = (ordertypeLink, orderlinkXpath,form_type)
    logging.info(json.dumps(data,indent=4))
    openOrderType(data,address,driver,merged_json,order_details)

def openOrderType(data,address,driver,merged_json,order_details):
    orderlist = ["cBPO Ext (u)", "cBPO Ext (n)", "cBPO Ext (a)", "cEval Ext (b)", "cBPO Ext (x) AVR"]
    if address in data:
        info = data[address]
        if info:
            for order_type in orderlist:
                if order_type in info[2]:
                    print(f"Order type '{order_type}' found")
                    order = chromedriver.find_elements(By.XPATH, info[1])
                    if order:
                        listing_address=openIdentifiedForm(order[0])
                        if listing_address:
                            print("Data has a value:", listing_address)
                            logging.info("Entry already filled")
                            # statuschange(order_details['order_id'], "25", "3", "14")
                        else:
                            print("Data is empty.")
                            with open('xome.json') as f:
                                data = json.load(f)
                            from Xome_EXT_form_filling import Formnewbpoext
                            init = Formnewbpoext()
                            # if session then send session
                            init.form(merged_json, driver, order_details['order_id'], data, order['ItemId'], order['OrderId'])
                    else:
                        print(info[1])
                        print("Order type not found, unable to do this order")
                        break
                else:
                    print(f"Order type can't be done: {order_type}")
        else:
            print("Address not found in portal")
    else:
        print("Address not found in portal")
   

def openIdentifiedForm(xpath):
     print("Order type found")
     xpath.click()
    # need code to check if data is already filled in portal
     return listing_address
