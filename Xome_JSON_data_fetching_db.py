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
def formdata_fetching_db(result_queue,order_details):
    tfsorder_id="1138537"  
    query="SELECT * FROM entry_data WHERE OrdID IN (SELECT t2.OrdID FROM subject AS t1 JOIN entry_data AS t2 ON t1.OrdID = t2.OrdID WHERE t1.TFSOrderID LIKE '"+tfsorder_id+"%')"
    # query="Select comp_data,adj_data FROM entry_data WHERE OrdID ='58985821'"
    DataFromRpad=ExecuteQuery(query,"Rpad")
    # comparables=json.loads(DataFromRpad[0][2])
    # comparablesData=comparables['values']
    # Adj=json.loads(DataFromRpad[0][3])
    # subjectData=json.loads(DataFromRpad[0][4])
    # bpoData=json.loads(DataFromRpad[0][5])

    tfsorder_id=order_details['order_id']
    tfsorder_id=str(tfsorder_id).strip()
    #tfsorder_id='1191392'
    tfs_orderid_rpad="SELECT * FROM ar_db.subject where TFSOrderID like '"+tfsorder_id+"%'"    
    tfs_order_id_rpad = ExecuteQuery(tfs_orderid_rpad,"Rpad") 
    print("tfs_order_id_rpad----",tfs_order_id_rpad) 
    if tfs_order_id_rpad:
        sub_query="SELECT Status FROM subject WHERE TFSOrderID like '"+tfsorder_id+"%'"    
        sub_status = ExecuteQuery(sub_query,"Rpad")
        print(sub_status)
        if sub_status: 
            portal_query="SELECT FormName FROM subject WHERE TFSOrderID like '"+tfsorder_id+"%'" 
            Portal_name = ExecuteQuery(portal_query,"Rpad")
            if "Redbell" in Portal_name['FormName']:
                if "Not Completed" not in sub_status or "Rental not completed" not in sub_status:
                    query="SELECT * FROM entry_data WHERE OrdID IN (SELECT t2.OrdID FROM subject AS t1 JOIN entry_data AS t2 ON t1.OrdID = t2.OrdID WHERE t1.TFSOrderID LIKE '"+tfsorder_id+"%')"
                    print(query)
                    logging.info("query........in json_data_fetching_db : {}".format(query)) 
                    try:
                        form_entry_data = ExecuteQuery(query,"Rpad")
                        logging.info("form_entry_data........in json_data_fetching_db : {}".format(form_entry_data)) 
                    except Exception as e:    
                        print("no json data in DB",e)
                        logging.info("no json data in DB : {}".format(e)) 
                    if form_entry_data is None:
                        print("form_entry_data is None")
                        logging.info("form_entry_data is None:") 
                        statuschange(order_details['order_id'],"18","3","14")
                    
                    else:
                        print("data available")
                        try:
                            cleaned_text = ' '.join(form_entry_data['comp_data'].split())
                            comp_data=json.loads(cleaned_text)
                            #print(comp_data)
                            comp_data=comp_data['values']
                        except Exception as e: 
                            comp_data=None   
                            print("no comp_data in DB",e)
                            logging.info("no comp_data in DB : {}".format(e)) 
                        #print(comp_data)
                        try:
                            cleaned_text = ' '.join(form_entry_data['adj_data'].split())
                            adj_data=json.loads(cleaned_text)
                        except Exception as e:   
                            adj_data=None 
                            print("no adj data in DB",e)
                            logging.info("no adj data in DB : {}".format(e)) 
                        try:
                            cleaned_text = ' '.join(form_entry_data['sub_data'].split())
                            sub_data=json.loads(cleaned_text)
                        except Exception as e:   
                            sub_data=None 
                            print("no sub data in DB",e)
                            logging.info("no sub data in DB : {}".format(e)) 
                        try:
                            cleaned_text = ' '.join(form_entry_data['bpo_data'].split())
                            bpo_data=json.loads(cleaned_text)
                            bpo_dataset={}
                            if bpo_data!=[] or bpo_data is not None :
                                for x in bpo_data:
                                    bpo_dataset.update(x)
                            else:
                                bpo_data=None
                                logging.info("This is bpo_data is none : {}".format(e)) 

                        except Exception as e: 
                            bpo_data=None  
                            bpo_dataset=None 
                            print("This is a Zillow Order",e)
                            logging.info("This is a Zillow Order : {}".format(e)) 

                        try:
                            cleaned_text = ' '.join(form_entry_data['rental_data'].split())
                            rental_data=json.loads(cleaned_text)    
                        except Exception as e:   
                            rental_data=None 
                            print("no Rental data in DB",e)
                            logging.info("no Rental data in DB : {}".format(e)) 

                        if form_entry_data is None or comp_data is None or adj_data is None or sub_data is None or bpo_dataset is None:
                            logging.info("One of the JSON data is Missing") 
                            statuschange(order_details['order_id'],"18","3","14")
                        else:
                            print("All present")
                            if rental_data is None:

                                merged_data = {**comp_data,**adj_data,**sub_data,**bpo_dataset}
                            else: 
                                merged_data = {**comp_data,**adj_data,**sub_data,**bpo_dataset,**rental_data}   
                            # Convert the merged dictionary to a JSON string
                            merged_jsonstr = json.dumps(merged_data)
                            merged_json=json.loads(merged_jsonstr)
                            #print("Merged JSON:", merged_json)
                            #logging.info("Merged JSON:: {}".format(merged_json))
                            result_queue.put(merged_json)
            

                else:
                    print("The subject is in Not Completed status", sub_status)
                    logging.info("Substatus None : {}".format(sub_status))
                    statuschange(order_details['order_id'],"18","3","14")    
            else: 
                print('Portal Name different',Portal_name)
                logging.info("Portal Name different : {}".format(Portal_name)) 
                statuschange(order_details['order_id'],"18","3","14")
                merged_json=[]
                result_queue.put(merged_json)
                return   
        else:
            print("Substatus None")        
            logging.info("Substatus None : {}".format(sub_status))
            statuschange(order_details['order_id'],"18","3","14")
            merged_json=[]
            result_queue.put(merged_json)
            return   

    else:
            print("Tfs client id is not present in Subject table")        
            logging.info("Tfs client id is not present in Subject table : {}".format(tfsorder_id))
            statuschange(order_details['order_id'],"65","3","14")
            merged_json=[]
            result_queue.put(merged_json)
            return
    
