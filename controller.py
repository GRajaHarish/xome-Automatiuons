
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from datetime import datetime

def javascript_excecuter_datefilling(driver,data,elementlocator,selector):    
   
        if data=='':
            pass

        else:
            # date=datetime.strptime(data,"%Y-%m-%d")
            # date=date.strftime("%d/%m/%Y")
            script = f"""document.evaluate("{elementlocator}", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.value = '{data}'"""
            driver.execute_script(script)
    
def adj_click(driver,data,element_identifier,element_type):
    selector_map=selector_mapping(element_type)
    element=driver.find_elements(selector_map,element_identifier)
    for x in element:
        x.click()

def radio_btn_click(driver,btn_value,element_identifier,element_type):#This function is for clicking radio button
    selector_map=selector_mapping(element_type)
    element=driver.find_elements(selector_map,element_identifier)
    for x in element:
        if x.get_attribute("value")==btn_value:
            x.click()

def data_filling_text(driver,data,elementlocator,selector):
    selector_map=selector_mapping(selector)
    element=find_elem(driver,selector_map,elementlocator)
    element.send_keys(data)

def select_field(driver,data,elementlocator,selector):
    try:
        Select(find_elem(driver,selector,elementlocator)).select_by_visible_text(data)
    except Exception as e:   
            data='' 
            print("no data",e)
def find_elem(driver,selector,elementlocator):
    
    element=driver.find_element(selector,elementlocator)
    return element

def selector_mapping(selector_type):
    
    selector = None
    
    if selector_type == "xpath":
        selector = By.XPATH
    elif selector_type == "id":
        selector = By.ID
    elif selector_type == "name":
        selector = By.NAME
    elif selector_type == "class_name":
        selector = By.CLASS_NAME
    elif selector_type == "tag_name":
        selector = By.TAG_NAME
    elif selector_type == "link_text":
        selector = By.LINK_TEXT
    elif selector_type == "partial_link_text":
        selector = By.PARTIAL_LINK_TEXT
    elif selector_type == "css_selector":
        selector = By.CSS_SELECTOR
    else:
        raise ValueError("Invalid selector type")
    return selector