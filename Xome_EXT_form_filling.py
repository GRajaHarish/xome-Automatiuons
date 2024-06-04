import json
import mysql.connector
from datetime import datetime as DT
#from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime, timedelta
from controller import radio_btn_click,select_field,data_filling_text, javascript_excecuter_datefilling,adj_click
from stdlib.utility import save_form
from conditions import condition_data
import time
import logging
import traceback
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

class Formnewbpoext:
            #  merged json = conditions completed data
    def form(self,merged_json,order_id,data):   
        # from#statuschange import#statuschange
        #merged_json=condition_data(merged_json)
        file_path = r'E:/PROJRCT XOME/Cbpo Ext(u)_1/Subject.html'
        chrome_options = Options()
        chrome_options.add_argument("--start-fullscreen") 
        driver = webdriver.Chrome(options=chrome_options)
        file_url = 'file:///' + file_path.replace('\\', '/')
        driver.get(file_url)
        time.sleep(2)
        try:
            for page_data in data["page"]:
                if "Subject_info" in page_data:
                    for control in page_data["Subject_info"]:
                        print(control["filedtype"])
                        for field in control["values"]:
                            filedtype = control["filedtype"]
                            
                            if filedtype == "Textbox":
                                print(field)
                                # if it is not present in condition data it will be in combined merged json
                                data_filling_text(driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: data_filling_text( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "select_data11":
                                select_field( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: select_field( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "radiobutton_data1":
                                radio_btn_click( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: radio_btn_click( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "Textbox_default":
                                print(field)
                                data_filling_text(driver,field[0], field[1], field[2])
                                logging.info(f"Logged: data_filling_text( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "select_default1":
                                select_field(driver,field[0], field[1], field[2])
                                logging.info(f"Logged: select_field( {field[0]}, {field[1]}, {field[2]})")
                            
                            elif filedtype == "radiobutton_default1":
                                radio_btn_click(driver,field[0], field[1], field[2])
                                logging.info(f"Logged: radio_btn_click( {field[0]}, {field[1]}, {field[2]})")
                            
                            elif filedtype == "date_fill_javascript":
                                javascript_excecuter_datefilling( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: javascript_excecuter_datefilling( driver,merged_json[{field[0]}], {field[1]}, {field[2]}")
                            elif filedtype =="save_data":
                                pass
                                             
   
                elif "Neighborhood" in page_data:
                    driver= openchrome2()
                    for control in page_data["Neighborhood"]:
                        print(control["filedtype"])
                        for field in control["values"]:
                            filedtype = control["filedtype"]
                            
                            if filedtype == "Textbox":
                                print(field)
                                data_filling_text( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: data_filling_text( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "select_data1":
                                select_field( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: select_field( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "radiobutton_data1":
                                radio_btn_click( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: radio_btn_click( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "Textbox_default":
                                print(field)
                                data_filling_text(driver,field[0], field[1], field[2])
                                logging.info(f"Logged: data_filling_text( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "select_default1":
                                select_field(driver,field[0], field[1], field[2])
                                logging.info(f"Logged: select_field( {field[0]}, {field[1]}, {field[2]})")
                            
                            elif filedtype == "radiobutton_default1":
                                radio_btn_click(driver,field[0], field[1], field[2])
                                logging.info(f"Logged: radio_btn_click( {field[0]}, {field[1]}, {field[2]})")
                            
                            elif filedtype == "date_fill_javascript":
                                javascript_excecuter_datefilling( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: javascript_excecuter_datefilling( driver,merged_json[{field[0]}], {field[1]}, {field[2]}")
                            elif filedtype =="save_data":
                                pass
                             
                                

                elif "Comparable" in page_data:
                    driver=openchrome()
                    for control in page_data["Comparable"]:
                        print(control["filedtype"])
                        for field in control["values"]:
                            filedtype = control["filedtype"]
                            
                            if filedtype == "Textbox":
                                print(field)
                                data_filling_text( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: data_filling_text( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "select_data1":
                                select_field( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: select_field( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "radiobutton_data1":
                                radio_btn_click( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: radio_btn_click( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "Textbox_default":
                                print(field)
                                data_filling_text(driver,field[0], field[1], field[2])
                                logging.info(f"Logged: data_filling_text( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "select_default1":
                                select_field(driver,field[0], field[1], field[2])
                                logging.info(f"Logged: select_field( {field[0]}, {field[1]}, {field[2]})")
                            
                            elif filedtype == "radiobutton_default1":
                                radio_btn_click(driver,field[0], field[1], field[2])
                                logging.info(f"Logged: radio_btn_click( {field[0]}, {field[1]}, {field[2]})")
                            
                            elif filedtype == "date_fill_javascript1":
                                javascript_excecuter_datefilling( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: javascript_excecuter_datefilling( driver,merged_json[{field[0]}], {field[1]}, {field[2]}")
                            elif filedtype =="save_data":
                                pass
                                

                elif "Repairs" in page_data:
                    for control in page_data["Repairs"]:
                        print(control["filedtype"])
                        for field in control["values"]:
                            filedtype = control["filedtype"]
                            
                            if filedtype == "Textbox":
                                print(field)
                                data_filling_text( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: data_filling_text( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "select_data1":
                                select_field( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: select_field( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "radiobutton_data1":
                                radio_btn_click( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: radio_btn_click( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "Textbox_default":
                                print(field)
                                data_filling_text(driver,field[0], field[1], field[2])
                                logging.info(f"Logged: data_filling_text( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "select_default1":
                                select_field(driver,field[0], field[1], field[2])
                                logging.info(f"Logged: select_field( {field[0]}, {field[1]}, {field[2]})")
                            
                            elif filedtype == "radiobutton_default1":
                                radio_btn_click(driver,field[0], field[1], field[2])
                                logging.info(f"Logged: radio_btn_click( {field[0]}, {field[1]}, {field[2]})")
                            
                            elif filedtype == "date_fill_javascript":
                                javascript_excecuter_datefilling( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: javascript_excecuter_datefilling( driver,merged_json[{field[0]}], {field[1]}, {field[2]}")
                            elif filedtype =="save_data":
                                pass
                                


                elif "Comments" in page_data:
                    for control in page_data["Comments"]:
                        print(control["filedtype"])
                        for field in control["values"]:
                            filedtype = control["filedtype"]
                            
                            if filedtype == "Textbox":
                                print(field)
                                data_filling_text( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: data_filling_text( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "select_data1":
                                select_field( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: select_field( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "radiobutton_data1":
                                radio_btn_click( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: radio_btn_click( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "Textbox_default":
                                print(field)
                                data_filling_text(driver,field[0], field[1], field[2])
                                logging.info(f"Logged: data_filling_text( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "select_default1":
                                select_field(driver,field[0], field[1], field[2])
                                logging.info(f"Logged: select_field( {field[0]}, {field[1]}, {field[2]})")
                            
                            elif filedtype == "radiobutton_default1":
                                radio_btn_click(driver,field[0], field[1], field[2])
                                logging.info(f"Logged: radio_btn_click( {field[0]}, {field[1]}, {field[2]})")
                            
                            elif filedtype == "date_fill_javascript":
                                javascript_excecuter_datefilling( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: javascript_excecuter_datefilling( driver,merged_json[{field[0]}], {field[1]}, {field[2]}")
                            elif filedtype =="save_data":
                               pass    
                               

                elif "Price" in page_data:
                    driver=openchrome3()
                    for control in page_data["Price"]:
                        print(control["filedtype"])
                        for field in control["values"]:
                            filedtype = control["filedtype"]
                            
                            if filedtype == "Textbox":
                                print(field)
                                data_filling_text( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: data_filling_text( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "select_data1":
                                select_field( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: select_field( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "radiobutton_data1":
                                radio_btn_click( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: radio_btn_click( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "Textbox_default":
                                print(field)
                                data_filling_text(driver,field[0], field[1], field[2])
                                logging.info(f"Logged: data_filling_text( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "select_default1":
                                select_field(driver,field[0], field[1], field[2])
                                logging.info(f"Logged: select_field( {field[0]}, {field[1]}, {field[2]})")
                            
                            elif filedtype == "radiobutton_default1":
                                radio_btn_click(driver,field[0], field[1], field[2])
                                logging.info(f"Logged: radio_btn_click( {field[0]}, {field[1]}, {field[2]})")
                            
                            elif filedtype == "date_fill_javascript":
                                javascript_excecuter_datefilling( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: javascript_excecuter_datefilling( driver,merged_json[{field[0]}], {field[1]}, {field[2]}")
                            elif filedtype =="save_data":
                                pass  
           #statuschange(order_id,"26","3","14")
            print("pls wait")
        except Exception as e:
            traceback.print_exc()
             # Optionally, you can also log the exception
            print("An exception occurred:", str(e))
            #statuschange(order_id,"27","3","14")
            print("Not Completed")

def openchrome():
    file_path = r'E:/PROJRCT%20XOME/Cbpo%20Ext(u)_1/Comparables.html'
    chrome_options = Options()
    chrome_options.add_argument("--start-fullscreen") 
    driver = webdriver.Chrome(options=chrome_options)
    file_url = 'file:///' + file_path.replace('\\', '/')
    driver.get(file_url)
    return driver
def openchrome2():
    file_path = r'E:/PROJRCT%20XOME/Cbpo%20Ext(u)_1/Neighborhood.html'
    chrome_options = Options()
    chrome_options.add_argument("--start-fullscreen") 
    driver = webdriver.Chrome(options=chrome_options)
    file_url = 'file:///' + file_path.replace('\\', '/')
    driver.get(file_url)
    return driver

def openchrome3():
    file_path = r'E:/PROJRCT%20XOME/Cbpo%20Ext(u)_1/Marketprice.html'
    chrome_options = Options()
    chrome_options.add_argument("--start-fullscreen") 
    driver = webdriver.Chrome(options=chrome_options)
    file_url = 'file:///' + file_path.replace('\\', '/')
    driver.get(file_url)
    return driver

        #===============================================================================================#