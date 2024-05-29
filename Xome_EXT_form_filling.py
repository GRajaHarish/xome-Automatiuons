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



class Formnewbpoext:

    def form(self,merged_json,order_id,data):
        # from StatusChange import statuschange
        #merged_json=condition_data(merged_json)
        file_path = r'C:\Users\mdm460\Downloads\Subject.html'
        chrome_options = Options()
        chrome_options.add_argument("--start-fullscreen") 
        driver = webdriver.Chrome(options=chrome_options)
        
        # Convert the file path to a URL format
        file_url = 'file:///' + file_path.replace('\\', '/')
        
        # Open the HTML file in Chrome
        driver.get(file_url)
        
        # Wait for the page to load
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
                            
                            elif filedtype == "select_data":
                                select_field( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: select_field( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "radiobutton_data":
                                radio_btn_click( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: radio_btn_click( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "Textbox_default":
                                print(field)
                                data_filling_text( field[0], field[1], field[2])
                                logging.info(f"Logged: data_filling_text( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "select_default":
                                select_field( field[0], field[1], field[2])
                                logging.info(f"Logged: select_field( {field[0]}, {field[1]}, {field[2]})")
                            
                            elif filedtype == "radiobutton_default":
                                radio_btn_click( field[0], field[1], field[2])
                                logging.info(f"Logged: radio_btn_click( {field[0]}, {field[1]}, {field[2]})")
                            
                            elif filedtype == "date_fill_javascript":
                                javascript_excecuter_datefilling( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: javascript_excecuter_datefilling( driver,merged_json[{field[0]}], {field[1]}, {field[2]}")
                            elif filedtype =="save_data":
                                for cookie in driver.get_cookies():
                                    c = {cookie['name']: cookie['value']}
                                    session.cookies.update(c)  
                                save_form(order_id)
                                Neighborhood = json.dumps(Neighborhood_url)
                                Neighborhood_Information=json.loads(Neighborhood)
                                driver.get(Neighborhood_Information['Neighborhood']) 
                                             
                #     #for control in
                #     save_form(order_id)   
                # if "save_data" in page_data:
                #     #for control in
                #     save_form(order_id)
                #     #data=page_data['save_data']['nextpage']
                #     #link=type.get(data)
                #     driver.get(type)
                #     #driver.get(f"{type}")

                elif "Neighborhood Information" in page_data:
                    for control in page_data["Neighborhood Information"]:
                        print(control["filedtype"])
                        for field in control["values"]:
                            filedtype = control["filedtype"]
                            
                            if filedtype == "Textbox":
                                print(field)
                                data_filling_text( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: data_filling_text( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "select_data":
                                select_field( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: select_field( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "radiobutton_data":
                                radio_btn_click( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: radio_btn_click( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "Textbox_default":
                                print(field)
                                data_filling_text( field[0], field[1], field[2])
                                logging.info(f"Logged: data_filling_text( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "select_default":
                                select_field( field[0], field[1], field[2])
                                logging.info(f"Logged: select_field( {field[0]}, {field[1]}, {field[2]})")
                            
                            elif filedtype == "radiobutton_default":
                                radio_btn_click( field[0], field[1], field[2])
                                logging.info(f"Logged: radio_btn_click( {field[0]}, {field[1]}, {field[2]})")
                            
                            elif filedtype == "date_fill_javascript":
                                javascript_excecuter_datefilling( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: javascript_excecuter_datefilling( driver,merged_json[{field[0]}], {field[1]}, {field[2]}")
                            elif filedtype =="save_data":
                                save_form(order_id)
                                for cookie in driver.get_cookies():
                                    c = {cookie['name']: cookie['value']}
                                    session.cookies.update(c)  
                                Comparable = json.dumps(Comparable_url)
                                Comparable_data=json.loads(Comparable)
                                driver.get(Comparable_data['Comparable'])
                                

                elif "Comparable" in page_data:
                    for control in page_data["Comparable"]:
                        print(control["filedtype"])
                        for field in control["values"]:
                            filedtype = control["filedtype"]
                            
                            if filedtype == "Textbox":
                                print(field)
                                data_filling_text( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: data_filling_text( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "select_data":
                                select_field( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: select_field( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "radiobutton_data":
                                radio_btn_click( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: radio_btn_click( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "Textbox_default":
                                print(field)
                                data_filling_text( field[0], field[1], field[2])
                                logging.info(f"Logged: data_filling_text( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "select_default":
                                select_field( field[0], field[1], field[2])
                                logging.info(f"Logged: select_field( {field[0]}, {field[1]}, {field[2]})")
                            
                            elif filedtype == "radiobutton_default":
                                radio_btn_click( field[0], field[1], field[2])
                                logging.info(f"Logged: radio_btn_click( {field[0]}, {field[1]}, {field[2]})")
                            
                            elif filedtype == "date_fill_javascript":
                                javascript_excecuter_datefilling( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: javascript_excecuter_datefilling( driver,merged_json[{field[0]}], {field[1]}, {field[2]}")
                            elif filedtype =="save_data":
                                for cookie in driver.get_cookies():
                                    c = {cookie['name']: cookie['value']}
                                    session.cookies.update(c)
                                save_form(order_id)
                                Repairs = json.dumps(Repairs_url)
                                Repairs_data=json.loads(Repairs)
                                driver.get(Repairs_data['Repairs'])
                                

                elif "Repairs" in page_data:
                    for control in page_data["Repairs"]:
                        print(control["filedtype"])
                        for field in control["values"]:
                            filedtype = control["filedtype"]
                            
                            if filedtype == "Textbox":
                                print(field)
                                data_filling_text( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: data_filling_text( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "select_data":
                                select_field( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: select_field( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "radiobutton_data":
                                radio_btn_click( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: radio_btn_click( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "Textbox_default":
                                print(field)
                                data_filling_text( field[0], field[1], field[2])
                                logging.info(f"Logged: data_filling_text( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "select_default":
                                select_field( field[0], field[1], field[2])
                                logging.info(f"Logged: select_field( {field[0]}, {field[1]}, {field[2]})")
                            
                            elif filedtype == "radiobutton_default":
                                radio_btn_click( field[0], field[1], field[2])
                                logging.info(f"Logged: radio_btn_click( {field[0]}, {field[1]}, {field[2]})")
                            
                            elif filedtype == "date_fill_javascript":
                                javascript_excecuter_datefilling( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: javascript_excecuter_datefilling( driver,merged_json[{field[0]}], {field[1]}, {field[2]}")
                            elif filedtype =="save_data":
                                for cookie in driver.get_cookies():
                                    c = {cookie['name']: cookie['value']}
                                    session.cookies.update(c)
                                save_form(order_id)
                                Comments = json.dumps(Comments_url)
                                Comments_data=json.loads(Comments)
                                driver.get(Comments_data['Comments'])
                                


                elif "Comments" in page_data:
                    for control in page_data["Comments"]:
                        print(control["filedtype"])
                        for field in control["values"]:
                            filedtype = control["filedtype"]
                            
                            if filedtype == "Textbox":
                                print(field)
                                data_filling_text( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: data_filling_text( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "select_data":
                                select_field( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: select_field( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "radiobutton_data":
                                radio_btn_click( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: radio_btn_click( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "Textbox_default":
                                print(field)
                                data_filling_text( field[0], field[1], field[2])
                                logging.info(f"Logged: data_filling_text( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "select_default":
                                select_field( field[0], field[1], field[2])
                                logging.info(f"Logged: select_field( {field[0]}, {field[1]}, {field[2]})")
                            
                            elif filedtype == "radiobutton_default":
                                radio_btn_click( field[0], field[1], field[2])
                                logging.info(f"Logged: radio_btn_click( {field[0]}, {field[1]}, {field[2]})")
                            
                            elif filedtype == "date_fill_javascript":
                                javascript_excecuter_datefilling( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: javascript_excecuter_datefilling( driver,merged_json[{field[0]}], {field[1]}, {field[2]}")
                            elif filedtype =="save_data":
                                for cookie in driver.get_cookies():
                                    c = {cookie['name']: cookie['value']}
                                    session.cookies.update(c)
                                save_form(order_id)  
                                Price = json.dumps(Price_url)
                                Price_data=json.loads(Price)
                                driver.get(Price_data['Price'])      
                               

                elif "Price" in page_data:
                    for control in page_data["Price"]:
                        print(control["filedtype"])
                        for field in control["values"]:
                            filedtype = control["filedtype"]
                            
                            if filedtype == "Textbox":
                                print(field)
                                data_filling_text( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: data_filling_text( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "select_data":
                                select_field( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: select_field( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "radiobutton_data":
                                radio_btn_click( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: radio_btn_click( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "Textbox_default":
                                print(field)
                                data_filling_text( field[0], field[1], field[2])
                                logging.info(f"Logged: data_filling_text( driver,merged_json[{field[0]}], {field[1]}, {field[2]})")
                            
                            elif filedtype == "select_default":
                                select_field( field[0], field[1], field[2])
                                logging.info(f"Logged: select_field( {field[0]}, {field[1]}, {field[2]})")
                            
                            elif filedtype == "radiobutton_default":
                                radio_btn_click( field[0], field[1], field[2])
                                logging.info(f"Logged: radio_btn_click( {field[0]}, {field[1]}, {field[2]})")
                            
                            elif filedtype == "date_fill_javascript":
                                javascript_excecuter_datefilling( driver,merged_json[field[0]], field[1], field[2])
                                logging.info(f"Logged: javascript_excecuter_datefilling( driver,merged_json[{field[0]}], {field[1]}, {field[2]}")
                            elif filedtype =="save_data":
                                for cookie in driver.get_cookies():
                                    c = {cookie['name']: cookie['value']}
                                    session.cookies.update(c)

                                save_form(order_id)         
                                
                # Comparable = json.dumps(Comparable_url)
                # Comparable_data=json.loads(Comparable)
                # driver.get(Comparable_data['Comparable'])   
            print("Complete")  
            time.sleep(10)          
            save_form(order_id)
            
            ###************************************************ 
            
                                
            time.sleep(2)
            
            statuschange(order_id,"26","3","14")
            print("pls wait")
        except Exception as e:
            traceback.print_exc()
             # Optionally, you can also log the exception
            print("An exception occurred:", str(e))
            statuschange(order_id,"27","3","14")
            print("Not Completed")
        #===============================================================================================#