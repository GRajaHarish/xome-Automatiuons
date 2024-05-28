import json
import mysql
import re
import mysql.connector
from StatusChange import statuschange
from utility import ExecuteQuery
import json
import logging
from FormProcessing.Xome_form_processing import FormFilling
#from webdriver_anager.chrome import ChromeDriverManager
def formdata_fetching_db():
    tfsorder_id="1138537"  
    query="SELECT * FROM entry_data WHERE OrdID IN (SELECT t2.OrdID FROM subject AS t1 JOIN entry_data AS t2 ON t1.OrdID = t2.OrdID WHERE t1.TFSOrderID LIKE '"+tfsorder_id+"%')"
    # query="Select comp_data,adj_data FROM entry_data WHERE OrdID ='58985821'"
    DataFromRpad=ExecuteQuery(query,"Rpad")
    # comparables=json.loads(DataFromRpad[0][2])
    # comparablesData=comparables['values']
    # Adj=json.loads(DataFromRpad[0][3])
    # subjectData=json.loads(DataFromRpad[0][4])
    # bpoData=json.loads(DataFromRpad[0][5])
    
    f = open('xome.json')
    jsondata = json.load(f)
    f.close()
    print(DataFromRpad)
    jsondata=json.dumps(jsondata, indent=4)
    
formdata_fetching_db()