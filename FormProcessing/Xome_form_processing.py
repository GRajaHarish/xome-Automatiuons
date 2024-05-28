import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import logging

def FormFilling(DataFromDB,jsondata):
    print(DataFromDB,jsondata)
