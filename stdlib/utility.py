import usaddress
import json
import mysql.connector
from requests import session
import requests
from stdlib.creds import dbcred
import time
from selenium.webdriver.common.by import By
from datetime import datetime as DT
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from datetime import datetime, timedelta
from selenium.common.exceptions import NoAlertPresentException
from dateutil import parser
import re
import logging

#Functiuon for Date Conversion
def date_conversion(data):
    try:
        if data=='' or data=='00/00/0000':
            formatted_date=''
        # Parse the date using dateutil.parser
        else:
            date_obj = parser.parse(data, fuzzy=True)
            # Format the date as "%m/%d/%Y"
            formatted_date = date_obj.strftime("%m/%d/%Y")
            print(formatted_date)
        logging.info("date after Date Conversion:{}".format(formatted_date))
    except Exception as e:
        print("Exception in Date Conversion ", e)
        logging.info("Exception in Date Conversion:{}".format(e))
        formatted_date=''
    return formatted_date

#Function for Yestarday date Conversion
def yesterday_date_conversion():  
    try:
        today = datetime.now()
        # Calculate yesterday's date 
        yesterday = today - timedelta(days=1)
        # Print yesterday's date
        yesterday_date=yesterday.strftime('%m/%d/%Y')
        print(yesterday_date)
        logging.info("date after yesterday_date Conversion:{}".format((yesterday_date)))
    except Exception as e:
        print("Exception in yesterday date conversion",e)
        logging.info("Exception in yesterday date conversion :{}".format((e)))
        yesterday_date=''
    return yesterday_date

#For validating date within six months
def sixmonth_date(): 
    try: 
        today = datetime.now()
        # Calculate yesterday's date 
        six_months_ago = today - timedelta(days=30*6)
        six_months_ago=six_months_ago.strftime('%m/%d/%Y')
        # Print yesterday's date
        print(six_months_ago)
        logging.info("date after six_months_ago_date Conversion:{}".format((six_months_ago)))
    except Exception as e:
        print("Exception in six month date validation",e)
        logging.info("Exception in six month date validation:{}".format((e)))
        six_months_ago=''
    return six_months_ago

#For saving form
def save_form(driver,order_id):
    
    try:
        time.sleep(5)
        element=driver.find_element(By.XPATH,"//*[@id='msg']")
        time.sleep(5)
        value1 = element.text  
        print("Extracted Value1:", value1)
        logging.info("Extracted Value in the ok button click:{}".format((value1)))
        time.sleep(3)
        if value1:
            driver.find_element(By.XPATH,"//*[@id='msg']/button").click()
            time.sleep(15)
            driver.find_element(By.XPATH,"//*[@id='btnSave']").click()
        else:
            driver.find_element(By.XPATH,"//*[@id='btnSave']").click()
            print("There is no OK button")
            logging.info("There is no OK button to click")
    except Exception as e:
    # value = element.text
        driver.find_element(By.XPATH,"//*[@id='btnSave']").click()
        print("No need to click ok button ", e)
        #element=driver.find_element(By.XPATH,'//*[@id="SAVE_BPO"]/a')
        #element.click()
        
        
    logging.info("order saved :{}".format(order_id))

    #For msg click form
def save_form_adj(driver,order_id):
    #print("adj")
    try:
        element=driver.find_element(By.XPATH,"//*[@id='msg']")
        value1 = element.text  
        print("Extracted Value1:", value1)
        logging.info("Extracted Value in the ok button click:{}".format((value1)))
        time.sleep(3)
        if value1:
            driver.find_element(By.XPATH,"//*[@id='msg']/button").click()
        else:
            print("There is no OK button")
            logging.info("There is no OK button to click")
    except Exception as e:
    # value = element.text
        #driver.find_element(By.XPATH,"//*[@id='btnSave']").click()
        print("No need to click ok button ", e)
        #element=driver.find_element(By.XPATH,'//*[@id="SAVE_BPO"]/a')
        #element.click()
        
        
    logging.info("order saved :{}".format(order_id))

def property_type_split(subtype, substyle): #propertyy type for Exterior and resoulte forms
    try:
        property_type =""
        if "SFR" in subtype :
            property_type ="SFD"
            #property_type="SFR Detached"
        elif "Condo" in subtype:
            property_type="Condo"
        elif "Mob/manufactured" in subtype:
            property_type="Mobile Home"
        elif "Land" in subtype:
            property_type="Land Only"
        elif "Commercial" in subtype:
            property_type="Commercial"
        elif "Multi Family" in subtype:
            if "2Family" in substyle:
                property_type="Duplex"
            elif "3Family" in substyle:
                property_type="Triplex"
            elif "4Family" in  substyle:
                property_type="4-Plex"                                             
        else:
            print("Property type not found")
            property_type=""    
        logging.info("property type for Exterior or resoulte forms :{}".format(property_type))
    except Exception as e:
        print("Exception in property type ", e)
        logging.info("Exception in property type for Exterior or resoulte forms:{}".format(e))
        property_type="" 
    return property_type



def property_type_PMI(subtype, substyle): #propertyy type for Exterior and resoulte forms
    try:
        property_type =""
        if "SFR" in subtype:
            property_type ="Single Family Detached"
        elif "SFD" in subtype:
            property_type ="Single Family Detached"    
            #property_type="SFR Detached"
        elif "Condo" in subtype:
            property_type="Condo"
        elif "Mob/manufactured" in subtype:
            property_type="Manufactured"
        elif "Land" in subtype:
            property_type="Mobile/Land Attached"
        elif "Commercial" in subtype:
            property_type="Commercial"
        elif "Multi Family" in subtype:
            if "2Family" in substyle:
                property_type="Multi-Family, 2-unit"
            elif "3Family" in substyle:
                property_type="Multi-Family, 3-unit"
            elif "4Family" in  substyle:
                property_type="Multi-Family, 4-unit"                                             
        else:
            print("Property type not found")
            property_type=""    
        logging.info("property type for Exterior or resoulte forms :{}".format(property_type))
    except Exception as e:
        print("Exception in property type ", e)
        logging.info("Exception in property type for Exterior or resoulte forms:{}".format(e))
        property_type="" 
    return property_type



def Leasehold_Feesimple(subtype): #propertyy type for Exterior and resoulte forms
    try:
        Feesimple =""
        if "SFR" in subtype or "Condo" in subtype or "Multi Family" in subtype:
            Feesimple ="Fee Simple"
        elif "Co-op" in subtype:
            Feesimple ="Leasehold"                                              
        else:
            Feesimple="--Select--"  
        logging.info("Fee simple :{}".format(Feesimple))
    except Exception as e:
        print("Exception in property type ", e)
        logging.info("Fee simple :{}".format(Feesimple))
        Feesimple="" 
    return Feesimple


def style(style):
    print(style)
    try:
            if 'Ranch' in style or '1 story' in style or 'One Story' in style or 'One' in style or '1' in style:
                    style='Ranch Rambler'
            elif 'Conventional' in style:
                    style='2 Story Conventional'
            elif '2 story' in style or '2 stories' in style or 'Two' in style or '2' in style:
                    style='2 Story Modern'  
            elif 'Town House' in style or 'Townhouse' in style or 'Town house' in style or 'Town home' in style or 'Town Home' in style:
                    style='TownHome'
            elif 'Traditional' in style or 'traditional' in style:
                    style='Traditional'
            elif 'Colonial' in style:
                    style='Colonial'  
            elif 'Split entry' in style or 'Split Level' in style or 'Split Foyer' in style or 'Split foyer' in style or 'Split' in style:
                    style='Split Entry'  
                 
            elif 'Cape Cod' in style:
                    style='Cape Cod' 
            elif 'Low Rise' in style:	
                    style='Condo'  
            elif  'Other' in style:
                    style ='--Select--'     
            elif  'Multi-Level' in style:
                    style ='Multi Level'         
            else:
                    style=style
    except Exception as e:
               print(e)
               style=''
    return style

def condition(cond):
    if 'Average' in cond:
        condition='C3-Well Maintained, limited physical depriciation due to normal wear and tear, some components may be updated.'
    elif 'Good' in cond:
        condition='C2-No deferred maintenance, little or no physical depriciation, requires no repairs.'
    elif 'Poor' in cond:
        condition='C5-Obvious deferred maintenance, need of some significant repairs.'
    elif 'Fair' in cond:
        condition='C4-Some minor deferred maintenance, normal wear and tear, required minimal repairs.'
    elif 'Excellent' in cond:
        condition='C1-New Not Previously Occupied.'
    else:
        condition=''
    return condition  
def property_type_split_citi(subtype):#property type for Citi form
    try:
        subtype=subtype.strip()
        print("subtype...",subtype)
        property_type=""
        if "SFR" in subtype:
            property_type="Single Family"
            other_property_type=""
        elif "Condo" in subtype:
            property_type="Condo"
            other_property_type=""
        elif "Mobile/manufactured" in subtype:
            property_type="Manufactured Home"
            other_property_type=""
        elif "Land" in subtype:
            property_type="Land"
            other_property_type=""
        elif "Commercial" in subtype:
            property_type="Commercial"
            other_property_type=""
        elif "Co-op" in subtype:
            property_type="Coop"
        elif "Multi Family" in subtype:
                property_type="2-4 Family"
                other_property_type=""
        else:
            if "Mobile/manufactured" in subtype:
                if "Manufactured Home" in property_type:
                   property_type="Manufactured Home"
                else:
                     property_type="Manufactured"   
            property_type=""
            other_property_type=subtype
            print("property not found")        
        logging.info("property type for Citi form :{}".format(property_type))
    except Exception as e:
        print("Exception in property type ", e)
        logging.info("Exception in property type for Citi form :{}".format(e))
        property_type=""
        other_property_type=subtype
    return property_type

def projected_use(subtype):
    try:
        subtype=subtype.strip()
        print("subtype...",subtype)
        property_type=""
        if "SFR" in subtype:
            property_type="SFR-Att"
        elif "Condo" in subtype:
            property_type="Condo"
        elif "Mobile/manufactured" in subtype:
            property_type="Mobile Home"
        elif "Commercial" in subtype:
            property_type="Commercial"
        elif "Co-op" in subtype:
            property_type="Coop"
        elif "Multi Family" in subtype:
                property_type="Multi Fam"
        else:
            property_type=""
            print("property not found")        
        logging.info("projected_use type for Citi form :{}".format(property_type))
    except Exception as e:
        print("Exception in projected_use type ", e)
        logging.info("Exception in projected_use type for Citi form :{}".format(e))
        property_type=""
    return property_type

def base_split(basement_data):
    try:
        print(basement_data)
        if basement_data in ["None","No"]:
            basement="None"
            basement_finished="0"
            basement_percent="0"
        else:
            basement="--Select--"
            basement_finished=""
            basement_percent=""
            print("basement not found")    
        logging.info("basement :{}".format(basement))  
        logging.info("basement_finished :{}".format(basement_finished))  
    except Exception as e:
        print("Exception in basement data ", e)
        logging.info("Exception in basement data :{}".format(e))  
        basement="--Select--"
        basement_finished=""
        basement_percent=""
    return basement,basement_finished,basement_percent  

def view_split(view_type):
    try:
        view=""
        if "Residential" in view_type:
            view="Neighborhood"
        elif view_type in ["Water", "Lake", "Intra Coastal", "Ocean"]:
            view="Water View"
        elif "Mountain" in view_type:
            view="Mountains"
        elif "Golf" in view_type:
            view="View of Golf Course"
        elif view_type in ["None" , "null"]:
            view="Other"    
        else:
            view=""
            print("View not found")
        logging.info("View Type:{}".format(view)) 
    except Exception as e:
        print("Exception in view type ", e)
        logging.info("Exception in view type  :{}".format(e)) 
        view=""
    return view


def neighbour_split(SubLoc):
    try:
        view=""
        if "Residential" in SubLoc:
            view="Residential"
        elif SubLoc in ["Water", "Lake", "Intra Coastal", "Ocean"]:
            view="Water Front"
        elif "Busy Street" in SubLoc:
            view="Busy Road"
        elif "Highway" in SubLoc:
            view="Highway"
        elif "Commercial" in SubLoc:
            view="Commercial"
        elif SubLoc in ["None" , "null"]:
            view="Other"    
        else:
            view=""
            print("View not found")
        logging.info("View Type:{}".format(view)) 
    except Exception as e:
        print("Exception in view type ", e)
        logging.info("Exception in view type  :{}".format(e)) 
        view=""
    return view
def validate_us_address(address):
    try:
        parsed_address, address_type = usaddress.tag(address)
        
        if address_type == 'Street Address':
            return True, parsed_address
        else:
            return False, "Invalid address type. Please provide a valid street address."
        print("Invalid address type. Please provide a valid street address.")

    except Exception as e:
        logging.error("Exception in validate_us_address: {}".format(e))
        return False, "Error validating the address. Please check the address format."
        print("Invalid address type. Please provide a valid street address.")


def adres_split(address, bed):
    try:
        is_valid, parsed_address = validate_us_address(address)

        if is_valid:
            St_add = parsed_address.get('AddressNumber', '') if parsed_address.get('AddressNumber', '') is not None else ''
            St_name = parsed_address.get('StreetName', '') if parsed_address.get('StreetName', '') is not None else ''
            St_suffix = parsed_address.get('StreetNamePostType', '') if parsed_address.get('StreetNamePostType', '') is not None else ''
            
            Street_Address = St_add + ' ' + St_name + ' ' + St_suffix
            Address_city = parsed_address.get('PlaceName', '')
            Addr_state = parsed_address.get('StateName', '').upper()
            Addr_zip = parsed_address.get('ZipCode', '').strip()

            print("Street_Address: {}".format(Street_Address))
            print("Address_city: {}".format(Address_city))
            print("Addr_state: {}".format(Addr_state))
            print("Addr_zip: {}".format(Addr_zip))

            logging.info("Street_Address: {}".format(Street_Address))
            logging.info("Address_city: {}".format(Address_city))
            logging.info("Addr_state: {}".format(Addr_state))
            logging.info("Addr_zip: {}".format(Addr_zip))

            try:
                Total_Rooms = int(bed) + 3
            except Exception as e:
                Total_Rooms = 0
                print("Exception in Total_Rooms. Please check:", e)
                logging.info("Exception in Total_Rooms. Please check: {}".format(e))

            logging.info("Total_Rooms: {}".format(Total_Rooms))
            print("Total_Rooms: {}".format(Total_Rooms))
            return Street_Address, Address_city, Addr_state, Addr_zip, Total_Rooms

        else:
            Street_Address = Address_city = Addr_state = Addr_zip = ""
            logging.info(parsed_address)
            try:
                Total_Rooms = int(bed) + 3
            except Exception as e:
                Total_Rooms = 0
                print("Exception in Total_Rooms. Please check:", e)
                logging.info("Exception in Total_Rooms. Please check: {}".format(e))
            return Street_Address, Address_city, Addr_state, Addr_zip, Total_Rooms

    except Exception as e:
        Street_Address = Address_city = Addr_state = Addr_zip = ""
        logging.error("Exception in adres_split: {}".format(e))
        try:
                Total_Rooms = int(bed) + 3
        except Exception as e:
            Total_Rooms = 0
            print("Exception in Total_Rooms. Please check:", e)
            logging.info("Exception in Total_Rooms. Please check: {}".format(e))
        logging.info("Total_Rooms: {}".format(Total_Rooms))
        print("Total_Rooms: {}".format(Total_Rooms))
        return Street_Address, Address_city, Addr_state, Addr_zip, Total_Rooms

def Type_of_Sale(saletype):
    try:
        type=""
        if saletype=="FMV":
            type="FMV"
        elif saletype=="Short Sale" or saletype=="SS":
            type="Short Sale"
        elif saletype=="REO":
            type="REO"
        else:
            type="FMV"
        logging.info("Type_of_Sale :{}".format(type))    
    except Exception as e:    
        print("exception in Type_of_Sale please check",e)
        logging.info("exception in Type_of_Sale please check :{}".format(e))
        type=""
    return type


def Listing_Status(SubStatus):
    try:
        type=""
        if SubStatus=="Pending":
            type="Contract"
        elif SubStatus=="Active":
            type="Active"
        elif SubStatus=="Sold":
            type="Sold"
        else:
            type="No activity within past 24 months"
        logging.info("Type_of_Sale :{}".format(type))    
    except Exception as e:    
        print("exception in Type_of_Sale please check",e)
        logging.info("exception in Type_of_Sale please check :{}".format(e))
        type=""
    return type    

def Type_of_Sale_pmi(saletype):
    try:
        type=""
        if saletype=="FMV":
            type="Arms length sale"
        elif saletype=="Short Sale" or saletype=="SS":
            type="Short Sale"
        elif saletype=="REO":
            type="REO sale"
        else:
            type="Arms length sale"
        logging.info("Type_of_Sale in Citi:{}".format(type))
    except Exception as e:    
        print("exception in Type_of_Sale in Citi please check",e)
        logging.info("exception in Type_of_Sale please check:{}".format(e))
        type=""
    return type

def Reo_condition(SubjectSaleType,Act1SType,Act2SType,Act3SType,Sold1SType,Sold2SType,Sold3SType):

          sale_type=["REO sale","REO"]
          try:
              if SubjectSaleType in sale_type or Act1SType in sale_type or Act2SType in sale_type or Act3SType in sale_type or Sold1SType in sale_type or Sold2SType in sale_type  or Sold3SType in sale_type:
                   reo=''
              else:
                   reo='1'
          except Exception as e:
                      reo='1'
                      print("Exception in Reo")
          return reo       


def format_data_columns(merged_data, columns):

    condition_to_json_mapping = {
        "adjcond": "Condition",
        "bediff": "Bed",
        "fbatdiff": "Full Bath",
        "hbatdiff": "Half Bath",
        "gladiff": "GLA",
        "ybdiff": "YearBuilt",
        "gardiff": "Garage",
        "cardiff": "Carport",
        "lotdiff": "Lot",
        "pooldiff": "Pool",
        "adjview": "View",
        "totadj": "Total Adjustment",
        "netadj": "Net Adjustment Value"
    }

    adj='' 
    for col in columns:
        if merged_data[col] != 0:
            adj_name = condition_to_json_mapping.get(str(col)[:-2], None)
            print("adj_name ",adj_name)
            if adj_name is not None:
                adj=adj+adj_name+":$"+str(merged_data[col])+","
        #else:
        #    pass
    adj=str(adj)[:-1]
    logging.info("Adjustment:{}".format(adj))
    return adj  
def age(yearblt): 
    try: 
        current_year = datetime.now().year
        age = int(current_year) - int(yearblt )
        print(age)
        logging.info("age:{}".format((age)))
    except Exception as e:
        print("Exception in age",e)
        logging.info("Exception in age:{}".format((e)))
        age=''
    return age    

def compgar(garage):
# Use regular expression to find the first digit in the valueif subGarType in ['None','Driveway','Undefined']
    try:
        # if (garage in ['0','None']):
        #    gar='None'  
        # elif (garage in ['1']):
        #     gar='Garage - 1 Car' 
        # elif (garage in ['2']):
        #     gar='Garage - 2 Car' 
        # else:
        #      gar='Garage - 3 Car'
        # if (['0','None'] in garage):
        #    gar='None'  
        # elif (['1'] in garage):
        #     gar='Garage - 1 Car' 
        # elif (['2'] in garage ):
        #     gar='Garage - 2 Car' 
        # else:
        #      gar='Garage - 3 Car'
        if '0' in garage or 'None' in garage:
            gar = 'None'
        elif '1' in garage:
            gar = 'Garage - 1 Car'
        elif '2' in garage:
            gar = 'Garage - 2 Car'
        else:
            gar = 'Garage - 3 Car'
        logging.info("Comparable Garage:{}".format(gar))    
    except Exception as e:    
        print("exception in comp garage",e)
        logging.info("exception in Comparable Garage:{}".format(e))
        gar='None'
    return gar



# def subject_garage(subGarType):
#     try:
#                if (subGarType in ['0','None']):
#                          Subject_garage='None'
#                elif (subGarType.upper() in ['1CARATTACH','1 CAR ATTACH', '1 CAR ATTACHED']):
#                          Subject_garage='Attached 1 Car Garage'  
#                elif (subGarType.upper() in ['1CARDETACH','1 CAR DETACH', '1 CAR DETACH']):
#                          Subject_garage='Detached 1 Car Garage'
#                elif (subGarType.upper() in ['2CARDETACH','2 CAR DETACH', '2 CAR DETACH']):
#                          Subject_garage='Detached 2 Car Garage'
#                elif (subGarType.upper() in ['3CARDETACH','3 CAR DETACH', '3 CAR DETACH']):
#                          Subject_garage='Attached 3 Car Garage'
#                elif (subGarType.upper() in ['3CARDETACH','3 CAR DETACH', '3 CAR DETACH']):
#                          Subject_garage='Detached 3 Car Garage'
                         
#                else :
#                          Subject_garage='Detached 3 Car Garage'
               
#     except Exception as e:    
#         print("exception in Address_state please check",e)
#         Subject_garage='None'
#     return Subject_garage



def get_state_abbreviation(state_name):
        states = {
            "ALABAMA": "AL",
            "ALASKA": "AK",
            "ARIZONA": "AZ",
            "ARKANSAS": "AR",
            "CALIFORNIA": "CA",
            "COLORADO": "CO",
            "CONNECTICUT": "CT",
            "DELAWARE": "DE",
            "FLORIDA": "FL",
            "GEORGIA": "GA",
            "HAWAII": "HI",
            "IDAHO": "ID",
            "ILLINOIS": "IL",
            "INDIANA": "IN",
            "IOWA": "IA",
            "KANSAS": "KS",
            "KENTUCKY": "KY",
            "LOUISIANA": "LA",
            "MAINE": "ME",
            "MARYLAND": "MD",
            "MASSACHUSETTS": "MA",
            "MICHIGAN": "MI",
            "MINNESOTA": "MN",
            "MISSISSIPPI": "MS",
            "MISSOURI": "MO",
            "MONTANA": "MT",
            "NEBRASKA": "NE",
            "NEVADA": "NV",
            "NEW HAMPSHIRE": "NH",
            "NEW JERSEY": "NJ",
            "NEW MEXICO": "NM",
            "NEW YORK": "NY",
            "NORTH CAROLINA": "NC",
            "NORTH DAKOTA": "ND",
            "OHIO": "OH",
            "OKLAHOMA": "OK",
            "OREGON": "OR",
            "PENNSYLVANIA": "PA",
            "RHODE ISLAND": "RI",
            "SOUTH CAROLINA": "SC",
            "SOUTH DAKOTA": "SD",
            "TENNESSEE": "TN",
            "TEXAS": "TX",
            "UTAH": "UT",
            "VERMONT": "VT",
            "VIRGINIA": "VA",
            "WASHINGTON": "WA",
            "WEST VIRGINIA": "WV",
            "WISCONSIN": "WI",
            "WYOMING": "WY",
            "AL": "ALABAMA",
            "AK": "ALASKA",
            "AZ": "ARIZONA",
            "AR": "ARKANSAS",
            "CA": "CALIFORNIA",
            "CO": "COLORADO",
            "CT": "CONNECTICUT",
            "DE": "DELAWARE",
            "FL": "FLORIDA",
            "GA": "GEORGIA",
            "HI": "HAWAII",
            "ID": "IDAHO",
            "IL": "ILLINOIS",
            "IN": "INDIANA",
            "IA": "IOWA",
            "KS": "KANSAS",
            "KY": "KENTUCKY",
            "LA": "LOUISIANA",
            "ME": "MAINE",
            "MD": "MARYLAND",
            "MA": "MASSACHUSETTS",
            "MI": "MICHIGAN",
            "MN": "MINNESOTA",
            "MS": "MISSISSIPPI",
            "MO": "MISSOURI",
            "MT": "MONTANA",
            "NE": "NEBRASKA",
            "NV": "NEVADA",
            "NH": "NEW HAMPSHIRE",
            "NJ": "NEW JERSEY",
            "NM": "NEW MEXICO",
            "NY": "NEW YORK",
            "NC": "NORTH CAROLINA",
            "ND": "NORTH DAKOTA",
            "OH": "OHIO",
            "OK": "OKLAHOMA",
            "OR": "OREGON",
            "PA": "PENNSYLVANIA",
            "RI": "RHODE ISLAND",
            "SC": "SOUTH CAROLINA",
            "SD": "SOUTH DAKOTA",
            "TN": "TENNESSEE",
            "TX": "TEXAS",
            "UT": "UTAH",
            "VT": "VERMONT",
            "VA": "VIRGINIA",
            "WA": "WASHINGTON",
            "WV": "WEST VIRGINIA",
            "WI": "WISCONSIN",
            "WY": "WYOMING",
            "SOUTH": "S",
            "WEST": "W",
            "EAST": "E",
            "NORTH": "N",
            "S": "SOUTH",
            "W": "WEST",
            "E": "EAST",
            "N": "NORTH",
            "NORTHWEST": "NW",
            "NORTHEAST": "NE",
            "SOUTHWEST": "SW",
            "SOUTHEAST": "SE",
            "NW": "NORTHWEST",
            "NE": "NORTHEAST",
            "SW": "SOUTHWEST",
            "SE": "SOUTHEAST"

        }
        logging.info("state_name after abbrevation:{}".format(state_name)) 
        return states.get(state_name)    

def best_sold_address(address):
    try:
        Street_Address=address.split(",")[0].strip()
    except Exception as e:
        print("exception in street address please check",e)
        logging.info("exception in street address please check  :{}".format(e)) 
        Street_Address=""
    return Street_Address

def get_cursor(db):
    """This function Connects to the database"""
    cred=dbcred(db)
    cnx = mysql.connector.connect(user=cred['DB_user'], password=cred['DB_password'], host=cred['DB_host'], database=cred['DB_database'],
                                  autocommit=True)
    cursor = cnx.cursor(buffered=True, dictionary=True)
    return cnx, cursor
def close_cursor_connection(cursor, cnx):
    """This Fucntion is used to Close SQL Connection"""
    cursor.close()
    cnx.close()
def cursorexec(db,query):
    """This Fucntion is used to Execute SQL query"""
    cnx, cursor = get_cursor(db)
    cursor.execute(query)
    data = cursor.fetchone()
    close_cursor_connection(cursor, cnx)
    return data 

def convert_to_int(value):
    try:
        # Try converting to float first
        float_value = float(value)
        # If conversion to float succeeds, convert to integer
        return int(float_value)
    except (ValueError, TypeError):
        return 0

def get_headers(additonal_headers):        #Function used to fetch the common headers used for acceptance
    try:
        headers={
                    'authority': 'valuationops.homegenius.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                    'accept-language': 'en-US,en;q=0.5',
                    'referer': 'https://valuationops.homegenius.com/VendorPortal',
                    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Brave";v="110"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/1.0.0.0 Safari/537.36',
                }
        if len(additonal_headers)> 0 :
            for a_head in additonal_headers: headers[a_head] = additonal_headers[a_head]
        return headers
    except Exception as ex:
        print(ex)

def session_check(session,session_cookie):
            resp=''
            url = "https://valuationops.homegenius.com/VendorPortalProfileV1"
            if session_cookie != '':
                data = session_cookie
                cook ='.ASPXAUTH={};'.format(data)
                print(cook)
                cookie ={'.ASPXAUTH': session_cookie }
                headers = get_headers({})
                resp = session.get(url, headers=headers ,cookies=cookie)
                if 'Profile Information' in resp.text:
                    print("Session Cookie Active!!!")
                    session.cookies.set('.ASPXAUTH', data)									  
                    session.headers.update(cookie) #session cookie not getting updated after 'get' request
                    return session,True
                else:
                    print("Session Cookie Not Active!!!")
                    return session,False
            else:
                return session,False

def login_to_portal(client_data,session):          #Function used to login into the portal
    try:
        url = "https://us-central1-crack-mariner-131508.cloudfunctions.net/Ecesis-Authpp"
        payload = json.dumps({
        "username": client_data['userid']
        })
        headers = {
        'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        resp=json.loads(response.text)
        if response.status_code==200:
            print("Success session fetch")
            cookies=resp['cookies']
            session.cookies.update(cookies)

            return True,session
        else:
            print("Server Error with API")
        if response['status']=='failed' and response['cookies']=={}:
            print("LOGIN ERROR")
            return False,session
    except Exception as ex:
        print(ex)

def fetch_data(session):
    response=session.get("https://valuationops.homegenius.com/VendorPortal/InprogressOrder")
    cookies=session.cookies.get_dict()
    headers = {
    'authority': 'valuationops.homegenius.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://valuationops.homegenius.com',
    'referer': 'https://valuationops.homegenius.com/VendorPortal/InprogressOrder',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }
    data = {
        '__aweconid': 'Grid',
        'v': '',
        'orderGenID': '',
        'loanId': '',
        'borrowerName': '',
        'propertyAddress': '',
        'stateAbbr': '',
        'productId': '',
        'orderFromDate': '',
        'orderThruDate': '',
        'orderStatus': '',
        'globalSearch': '',
        'pageSize': [
            '1000',
            '50',
        ],
        'page': '1',
        'tzo': '-330',
    }

    response = requests.post(
        'https://valuationops.homegenius.com/VendorPortal/GetMyOrderItem',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    #print(response.content)
    data=json.loads(response.content)
    orders=data['dt']['it']
    return orders,session
