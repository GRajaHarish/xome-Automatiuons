import requests
import logging

def statuschange(order_details,bpo_statusid,tfs_status,tfs_status_reason):
    data={
                    "strSessionID":"",
                    "ProcParameters":["type","sTFStatusData","stfsOrderId"],
                    "ProcInputData":[1,f"{tfs_status}~{tfs_status_reason}~",order_details]
        }
    response2=requests.post("http://13.200.17.36/autobpo_test/home/ProcUpdateTFSstatusEntry",data=data)
    # logging.info("Status change data :{}".format(data))
    # response2=requests.post("https://bpotrackers.com/bvupcqp/home/ProcUpdateTFSstatusEntry",data=data)
    logging.info("response2 :{}".format(response2.text))
    data1={
                    "strSessionID":"",
                    "ProcInputData": [f"{bpo_statusid}~Na~Na~",order_details],
                    "ProcParameters": ["sAutoBPOdata", "sOrderId"]
        }
    response1 =requests.post("http://13.200.17.36/autobpo_test/Home/ProcUpdateAutoEntry",data=data1)
    # logging.info("Status change data1 :{}".format(data1))
    # response1 =requests.post("https://bpotrackers.com/bvupcqp/Home/ProcUpdateAutoEntry",data=data1)
    logging.info("response1 :{}".format(response1.text))
   
    print("Status changed succesfully")
    logging.info("Status changed succesfully")

    
