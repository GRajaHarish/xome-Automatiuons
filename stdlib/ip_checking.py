import requests
from bs4 import BeautifulSoup
import json
import re
import logging

# Define the URL of the webpage
def ip_address_checking():
    try:
        url = "http://ip-api.com/#"
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        #print("Response:",response.text)
        #response_string=response.text
        cleaned_string = re.sub(r'(\x1B\[\d+m)|[^\x20-\x7E]', '', response.text)
        start_index = cleaned_string.index('{')
        json_string = cleaned_string[start_index:]
        data = json.loads(json_string)
        ip_address = data["query"]
        print("IP Address:", ip_address)
        logging.info("IP Address:{}".format(ip_address))
    except Exception as e:
        print("Exception in ip checking",e)
        ip_address=''
        logging.info("Exception in ip checking:{}".format(e))
    return ip_address

