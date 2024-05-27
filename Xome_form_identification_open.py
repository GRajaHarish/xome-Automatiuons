import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def findorderTYPE():
    chrome_options = Options()
    chrome_options.add_argument("--start-fullscreen")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('file:///G:/Orders.html')
    address_to_search = "10914 W COTTONWOOD LN\nAVONDALE, AZ 85392"
    table = driver.find_element(By.ID, "OrdersInProgressGrid")
    rows = table.find_elements(By.XPATH, ".//tbody/tr")
    first_column_texts_and_xpaths = []
    subject_property_texts = []
    data = {}
    for row_index, row in enumerate(rows, start=2):
        # Extract text from the 0th (first) column
        first_column_element = row.find_element(By.XPATH, ".//td[1]")
        first_column_text = first_column_element.text
        first_column_xpath = f"//*[@id='OrdersInProgressGrid']/tbody/tr[{row_index}]/td[1]"
        first_column_texts_and_xpaths.append((first_column_text, first_column_xpath))
        try:
          subject_property_text = row.find_element(By.XPATH, ".//td[contains(@class, 'SubjectProperty')]").text
        except:
          subject_property_text = "N/A"
        subject_property_texts.append(subject_property_text)
        data[subject_property_text] = (first_column_text, first_column_xpath)
    openOrderType(data)

def openOrderType(data);
   
   
findorderTYPE()
