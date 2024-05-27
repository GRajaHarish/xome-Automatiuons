import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def findorderTYPE():
    global driver
    chrome_options = Options()
    chrome_options.add_argument("--start-fullscreen")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('file:///G:/Orders.html')
    address_to_search = "10914 W COTTONWOOD LN\nAVONDALE, AZ 85392"
    table = driver.find_element(By.ID, "OrdersInProgressGrid")
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
    print(json.dumps(data,indent=4))
    openOrderType(data,rows)

def openOrderType(data,rows):
    address="1241 N 48TH ST Unit #111\nPHOENIX, AZ 85008"
    orderlist=["cBPO","cBPO Ext (x)","cBPO Ext (x) 24hr"]
    
    if address in data:
        info = data[address]
        for order_type in orderlist:
            if order_type in info[2]:
                print(f"Order type '{order_type}' found in info[2]")
                order = driver.find_elements(By.XPATH,info[1] )
                if order:
                   openIdentifiedForm(order[0])
                else:
                    print(info[1])
                    print("Order type not found")
                break
            else:
                print("None of the order types found in info[2]")
               
  
def openIdentifiedForm(xpath):
     print("Order type found")
     xpath.click()
     time.sleep(8)
     driver.quit()
   
findorderTYPE()
