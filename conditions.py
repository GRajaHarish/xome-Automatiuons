from datetime import datetime as DT
#from webdriver_manager.chrome import ChromeDriverManager

from datetime import datetime, timedelta
from stdlib.utility import convert_to_int,Listing_Status,neighbour_split,property_type_PMI,Type_of_Sale_pmi,Reo_condition,age,condition,style,best_sold_address,format_data_columns,property_type_split,adres_split,Type_of_Sale,view_split,base_split,yesterday_date_conversion,date_conversion,property_type_split_citi,sixmonth_date,projected_use,compgar,Leasehold_Feesimple
import logging
# from stdlib.client_details import client_data
import json


def condition_data(merged_data,subclient):
          merged_data['isProperty_Currently_yes']= 'yes'
          if merged_data['SubPropCond'] not in ["Fair","Poor"]:
               if "Multi Family" in merged_data['Subtype']:
                    subject_property_condition="Tenant"
                    merged_data['Percentage_of_Owners']="50%"
               else :
                    subject_property_condition="Owner"
                    merged_data['Percentage_of_Owners']="85%" 
          merged_data['subject_property_condition']=subject_property_condition 
          if "Mob/manufactured" not in merged_data['Subtype']:
               merged_data['manufactured']="NA"   
          else :
               merged_data['manufactured']="" 

          if "Multi Family" in merged_data['Subtype']:
                   merged_data['Percentage_of_Owners']="50%"
          else :
               merged_data['Percentage_of_Owners']="85%" 
          if "Multi Family" in merged_data['Subtype']:
                   Predominant_Occupancy=" Tenant"
                   Predominant_Occupancy_gos="Tenant"
          else :
               Predominant_Occupancy=" Owner" 
               Predominant_Occupancy_gos="Owner"
          merged_data['Predominant_Occupancy']=Predominant_Occupancy
          merged_data['Predominant_Occupancy_gos']=Predominant_Occupancy_gos

          merged_data['Subject_property_type']=property_type_split(merged_data['Subtype'],merged_data['Substye']) 
          
          merged_data['Subject_property_type_PMI']=property_type_PMI(merged_data['Subtype'],merged_data['Substye'])

          merged_data['Subject_Feesimple']=Leasehold_Feesimple(merged_data['Subtype'])
          
          subject_projected_use=projected_use(merged_data['Subtype'])
          merged_data['Projected_Uses']=subject_projected_use
    
          merged_data['Subject_Comment']="Subject conforms to the immediate neighborhood and is located within moderate proximity to public transportation, freeway access, retail amenities and schools. There are no adverse site conditions or external factors such as easements, encroachments, environmental conditions or land uses"
          if merged_data['SubPropCond'] in ["Fair","Poor"]:
               subject_repair_Comments="Based on exterior observation, subject property is in "+merged_data['SubPropCond']+" condition."
          else:     
               subject_repair_Comments="Based on exterior observation, subject property is in "+merged_data['SubPropCond']+" condition, No immediate repair or modernization required."
          merged_data['Subject_repair_Comments']=subject_repair_Comments  

          

          subject_neighborhood_Comments="The subject is located in a suburban neighborhood with stable property values and the economy and employment conditions are stable, neighborhood market trends are stable, conditions are stable, supply and demand is stable, the prevalence of REO is stable and seller concessions are stable."
          merged_data['Subject_neighborhood_Comments']=subject_neighborhood_Comments  

          if merged_data['SubUnits']=='' or merged_data['SubUnits']=='0':
               merged_data['SubUnits']=''
          else:
               merged_data['SubUnits']=merged_data['SubUnits']

          merged_data['Subject_garage']=compgar(merged_data['SubGarType']) 
          merged_data['Act1Gar']=compgar(merged_data['Act1Gar'])
          merged_data['Act2Gar']=compgar(merged_data['Act2Gar'])
          merged_data['Act3Gar']=compgar(merged_data['Act3Gar'])
          merged_data['Sold1Gar']=compgar(merged_data['Sold1Gar'])
          merged_data['Sold2Gar']=compgar(merged_data['Sold2Gar'])
          merged_data['Sold3Gar']=compgar(merged_data['Sold3Gar'])
          try:
               merged_data['AsIs90Day']="423829"
               print(merged_data['AsIs90Day'])
               merged_data['AsIs90Day_2']=str(int(merged_data['AsIs90Day']) + 5000)
               merged_data['30daysQale']=str(int(merged_data['AsIs90Day']) - 5000)
               
               merged_data['Leased1_address'],merged_data['Leased1_city'],merged_data['Leased1_state'], merged_data['Leased1_zipcode'],merged_data['Leased1_total_rooms']=adres_split(merged_data['Leased1Add'],merged_data['Leased1Bed'])
          except Exception as e:
               print("exception in rental address please check",e)
               logging.info("exception in street address please check  :{}".format(e)) 
               Leased1_address=""
               Leased1_city=""
               Leased1_state=""
               Leased1_zipcode=""
               Leased1_total_rooms=""
          try:
               merged_data['Leased2_address'],merged_data['Leased2_city'],merged_data['Leased2_state'], merged_data['Leased2_zipcode'],merged_data['Leased2_total_rooms']=adres_split(merged_data['Leased2Add'],merged_data['Leased2Bed'])
          except Exception as e:
               print("exception in rental address please check",e)
               logging.info("exception in street address please check  :{}".format(e)) 
               Leased2_address=""
               Leased2_city=""
               Leased2_state=""
               Leased2_zipcode=""
               Leased2_total_rooms=""
          try:
               merged_data['Act1_address'],merged_data['Act1_city'],merged_data['Act1_state'], merged_data['Act1_zipcode'],merged_data['Act1_total_rooms']=adres_split(merged_data['List1Add'],merged_data['List1Bed'])
          except Exception as e:
               print("exception in rental address please check",e)
               logging.info("exception in street address please check  :{}".format(e)) 
               Act1_address=""
               Act1_city=""
               Act1_state=""
               Leased1_zipcode=""
               Leased1_total_rooms=""
          try:
               merged_data['Act2_address'],merged_data['Act2_city'],merged_data['Act2_state'], merged_data['Act2_zipcode'],merged_data['Act2_total_rooms']=adres_split(merged_data['List2Add'],merged_data['List2Bed'])
          except Exception as e:
               print("exception in rental address please check",e)
               logging.info("exception in street address please check  :{}".format(e)) 
               Act2_address=""
               Act2_city=""
               Act_state=""
               Act2_zipcode=""
               Act2_total_rooms=""
          print("merged_data['Act2Gar']    ",merged_data['Act2Gar'])
          print("merged_data['Act3Gar']-------",merged_data['Act3Gar'])

          merged_data['Subject_street_address'],merged_data['Subject_city'],merged_data['Subject_state'], merged_data['Subject_zipcode'],merged_data['Subject_total_rooms']=adres_split(merged_data['SubAdd'],merged_data['SubBed'])
          merged_data['Comp1_street_address'],merged_data['Comp1_city'],merged_data['Comp1_state'], merged_data['Comp1_zipcode'],merged_data['Comp1_total_rooms']=adres_split(merged_data['Act1Add'],merged_data['Act1Bed'])
          merged_data['Comp2_street_address'],merged_data['Comp2_city'],merged_data['Comp2_state'], merged_data['Comp2_zipcode'],merged_data['Comp2_total_rooms']=adres_split(merged_data['Act2Add'],merged_data['Act2Bed'])
          merged_data['Comp3_street_address'],merged_data['Comp3_city'],merged_data['Comp3_state'], merged_data['Comp3_zipcode'],merged_data['Comp3_total_rooms']=adres_split(merged_data['Act3Add'],merged_data['Act3Bed'])
          merged_data['Comp4_street_address'],merged_data['Comp4_city'],merged_data['Comp4_state'], merged_data['Comp4_zipcode'],merged_data['Comp4_total_rooms']=adres_split(merged_data['Sold1Add'],merged_data['Sold1Bed'])
          merged_data['Comp5_street_address'],merged_data['Comp5_city'],merged_data['Comp5_state'], merged_data['Comp5_zipcode'],merged_data['Comp5_total_rooms']=adres_split(merged_data['Sold2Add'],merged_data['Sold2Bed'])
          merged_data['Comp6_street_address'],merged_data['Comp6_city'],merged_data['Comp6_state'], merged_data['Comp6_zipcode'],merged_data['Comp6_total_rooms']=adres_split(merged_data['Sold3Add'],merged_data['Sold3Bed'])
          try:
               merged_data['Suject_basement'],merged_data['Suject_basement_finished'],merged_data['Suject_basement_percent']=base_split(merged_data['SubBase'])
          except Exception as e:
               print("exception in basement please check",e)
               logging.info("exception in basement please check  :{}".format(e)) 
               merged_data['Suject_basement']=""
               merged_data['Suject_basement_finished']=""
               merged_data['Suject_basement_percent']=""
          try:
               merged_data['Comp1_basement'],merged_data['Comp1_basement_finished'],merged_data['Comp1_basement_percent']=base_split(merged_data['Act1Base'])
          except Exception as e:
               print("exception in basement please check",e)
               logging.info("exception in basement please check  :{}".format(e)) 
               merged_data['Comp1_basement']=""
               merged_data['Comp1_basement_finished']=""
               merged_data['Comp1_basement_percent']=""
          try:
               merged_data['Comp2_basement'],merged_data['Comp2_basement_finished'],merged_data['Comp2_basement_percent']=base_split(merged_data['Act2Base'])
          except Exception as e:
               print("exception in basement please check",e)
               logging.info("exception in basement please check  :{}".format(e)) 
               merged_data['Comp2_basement']=""
               merged_data['Comp2_basement_finished']=""
               merged_data['Comp2_basement_percent']=""
          try:
               merged_data['Comp3_basement'],merged_data['Comp3_basement_finished'],merged_data['Comp3_basement_percent']=base_split(merged_data['Act3Base'])
          except Exception as e:
               print("exception in basement please check",e)
               logging.info("exception in basement please check  :{}".format(e)) 
               merged_data['Comp3_basement']=""
               merged_data['Comp3_basement_finished']=""
               merged_data['Comp3_basement_percent']=""
          try:
               merged_data['Comp4_basement'],merged_data['Comp4_basement_finished'],merged_data['Comp4_basement_percent']=base_split(merged_data['Sold1Base'])
          except Exception as e:
               print("exception in basement please check",e)
               logging.info("exception in basement please check  :{}".format(e)) 
               merged_data['Comp4_basement']=""
               merged_data['Comp4_basement_finished']=""
               merged_data['Comp4_basement_percent']=""
          try:
               merged_data['Comp5_basement'],merged_data['Comp5_basement_finished'],merged_data['Comp5_basement_percent']=base_split(merged_data['Sold2Base'])
          except Exception as e:
               print("exception in basement please check",e)
               logging.info("exception in basement please check  :{}".format(e)) 
               merged_data['Comp5_basement']=""
               merged_data['Comp5_basement_finished']=""
               merged_data['Comp5_basement_percent']=""
          try:
               merged_data['Comp6_basement'],merged_data['Comp6_basement_finished'],merged_data['Comp6_basement_percent']=base_split(merged_data['Sold3Base'])
          except Exception as e:
               print("exception in basement please check",e)
               logging.info("exception in basement please check  :{}".format(e)) 
               merged_data['Comp6_basement']=""
               merged_data['Comp6_basement_finished']=""
               merged_data['Comp6_basement_percent']=""

          
          merged_data['Substyle']=style(merged_data['Substye'])
          merged_data['Active1Style']=style(merged_data['Act1Style'])
          merged_data['Active2Style']=style(merged_data['Act2Style'])
          merged_data['Active3Style']=style(merged_data['Act3Style'])
          merged_data['Sol1Style']=style(merged_data['Sold1Style'])
          merged_data['Sol2Style']=style(merged_data['Sold2Style'])
          merged_data['Sol3Style']=style(merged_data['Sold3Style'])


          merged_data['Sub_Prop_Cond']=condition(merged_data['SubPropCond'])
          merged_data['Act1_Prop_Cond']=condition(merged_data['Act1Cond'])
          merged_data['Act2_Prop_Cond']=condition(merged_data['Act2Cond'])
          merged_data['Act3_Prop_Cond']=condition(merged_data['Act3Cond'])
          merged_data['Sold1_Prop_Cond']=condition(merged_data['Sold1Cond'])
          merged_data['Sold2_Prop_Cond']=condition(merged_data['Sold2Cond'])
          merged_data['Sold3_Prop_Cond']=condition(merged_data['Sold3Cond'])

          merged_data['Sub_Status']=Listing_Status(merged_data['SubStatus']) 


          #Client_details=json.loads(client_details.json) 
          f = open('client_details.json')
          client_details = json.load(f)
          #client_details==json.loads(client_details)
          if subclient in client_details:
          # Retrieve the "Years" information for the specified subclient
               merged_data['License'] = client_details[subclient]['License']
               merged_data['Years'] = client_details[subclient]['Years']
               merged_data['State'] = client_details[subclient]['State']
               merged_data['Expiration Date'] = client_details[subclient]['Expiration Date']
          else:
               print("Client is not available in Client_json data")
               merged_data['License']=''
               merged_data['Years']=''
               merged_data['State']=''
               merged_data['Expiration Date']=''
          if merged_data['Rent']=='0':
                    merged_data['Rent']=""
          else:
               merged_data['Rent']=merged_data['Rent']

          if merged_data['SubMLS']:               
               merged_data['SubMLS']=merged_data['SubMLS']
          else:
               merged_data['SubMLS']='0'

          try:
               if merged_data['RSugmv']=='0':
                         merged_data['RSugmv']=""
               else:
                    merged_data['RSugmv']=merged_data['RSugmv']  

          except:
               merged_data['RSugmv']=""

          if "Yes" in merged_data['SubList']:
               # merged_data['SubList_sold']="No"
               # merged_data['SubList_active']="No"
               merged_data['SubList_active']="No"
               merged_data['SubListPrice_active']=''
               merged_data['SubListDate_active']=''
               merged_data['SubListComp_active']=''
               merged_data['OwnerName_active']='' 
               merged_data['Listingcompany_active']='' 
               merged_data['SubList_sold']="No"
               merged_data['SubListPrice_sold']=''
               merged_data['SubListDate_sold']=''
               merged_data['SubListComp_sold']=''
               merged_data['OwnerName_sold']='' 
               merged_data['Listingcompany_sold']='' 
               merged_data['isProperty_Currently_yes']= 'yes'
              

               if "Active" in merged_data['SubStatus'] or "Pending" in merged_data['SubStatus']:
                    merged_data['SubList_active']="Yes"
                    merged_data['Analysis_Comments']="The subject is currently active on Market."
                    if merged_data['SubListPrice']=='':
                         merged_data['SubListPrice_active']=''
                    else:                         
                         merged_data['SubListPrice_active']= merged_data['SubListPrice']

                    if merged_data['SubListDate']=='':   
                         merged_data['SubListDate_active']=''
                    else:
                         merged_data['SubListDate_active']=merged_data['SubListDate'] 

                    if merged_data['SubListComp']=='':
                         merged_data['SubListComp_active']=''
                    else:
                         merged_data['SubListComp_active']=merged_data['SubListComp']
                    if merged_data['OwnerName']=='':
                         merged_data['OwnerName_active']=''
                    else:
                         merged_data['OwnerName_active']=merged_data['OwnerName']   
                    if merged_data['SubListComp']=='':
                         merged_data['Listingcompany_active']=''
                    else:
                         merged_data['Listingcompany_active']=merged_data['SubListComp']         

               if "Sold" in merged_data['SubStatus']:

                    merged_data['SubList_sold']="Yes"
                    merged_data['Analysis_Comments']="The subject is recently sold"
                    if merged_data['SubListPrice']=='':
                         merged_data['SubListPrice_sold']=''
                    else:                         
                         merged_data['SubListPrice_sold']= merged_data['SubListPrice']

                    if merged_data['SubListDate']=='':   
                         merged_data['SubListDate_sold']=''
                    else:
                         merged_data['SubListDate_sold']=merged_data['SubListDate'] 

                    

                    if merged_data['SubListComp']=='':
                         merged_data['SubListComp_sold']=''
                    else:
                         merged_data['SubListComp_sold']=merged_data['SubListComp']
                    if merged_data['OwnerName']=='':
                         merged_data['OwnerName_sold']=''
                    else:
                         merged_data['OwnerName_sold']=merged_data['OwnerName']   
                    if merged_data['SubListComp']=='':
                         merged_data['Listingcompany_sold']=''
                    else:
                         merged_data['Listingcompany_sold']=merged_data['SubListComp']          
          else:
               merged_data['SubList_active']="No"
               merged_data['SubListPrice_active']=''
               merged_data['SubListDate_active']=''
               merged_data['SubListComp_active']=''
               merged_data['OwnerName_active']='' 
               merged_data['Listingcompany_active']='' 
               merged_data['SubList_sold']="No"
               merged_data['SubList_Not_sold']="No"
               merged_data['SubListPrice_sold']=''
               merged_data['SubListDate_sold']=''
               merged_data['SubListComp_sold']=''
               merged_data['OwnerName_sold']='' 
               merged_data['Listingcompany_sold']='' 
               merged_data['isProperty_Currently_no']='no'
               merged_data['Analysis_Comments']='No recent sales/listing history available'

          #Hoa
          if merged_data['Subtype']=='Condo':
               merged_data['SubHoa']='Yes'  
               merged_data['FloorLocation']=merged_data['Substories']
          else:
               merged_data['SubHoa']='No'
               merged_data['FloorLocation']='' 
          try:
               #merged_data['marketingtime'] = str(float(merged_data['compdom4']) + float(merged_data['compdom5']) + float(merged_data['compdom6'])/ 3)                 
               if not merged_data['compdom4']:
                    merged_data['compdom4'] = '0'
               if not merged_data['compdom5']:
                    merged_data['compdom5'] = '0'
               if not merged_data['compdom6']:
                    merged_data['compdom6'] = '0'
               if merged_data['compdom4'].isdigit() and merged_data['compdom5'].isdigit() and merged_data['compdom6'].isdigit():
                    merged_data['marketingtime'] = str((int(merged_data['compdom4']) + int(merged_data['compdom5']) + int(merged_data['compdom6']))/ 3)
          except:
               merged_data['marketingtime']='0'

          try:
               if merged_data['SubBaseare'] == "":
                         merged_data['SubBaseare']="0"
               else :
                    merged_data['SubBaseare'] =merged_data['SubBaseare']  
          except:
                 merged_data['SubBaseare']="0"             
               
          
          try:
               if 0 < int(float(merged_data['marketingtime'])) < 90:
                    merged_data['Normal Marketing Time'] = 'Under 3 Months'
               elif 90 <= int(float(merged_data['marketingtime'])) >= 180:
                    merged_data['Normal Marketing Time'] = '3-6 Months'
               elif int(float(merged_data['marketingtime']))==0:
                    merged_data['Normal Marketing Time'] = '3-6 Months'    
               else:
                    merged_data['Normal Marketing Time'] = 'Over 6 Months'        
          except:
               merged_data['Normal Marketing Time'] = '3-6 Months' 

          price = [merged_data['Sold1Price'], merged_data['Sold2Price'], merged_data['Sold3Price'], merged_data['Act1Price'], merged_data['Act2Price'], merged_data['Act3Price']]
          low = min(price)
          high = max(price)
          merged_data['neighhigh'] = str(int(high) * 1.2)
          merged_data['neighlow'] = str(int(low) * 0.8)
          merged_data['avg'] = str((float(merged_data['neighlow']) + float(merged_data['neighhigh'])) / 2)

          saleprice = [merged_data['Sold1Price'], merged_data['Sold2Price'], merged_data['Sold3Price']]
          actvprice = [merged_data['Act1Price'], merged_data['Act2Price'], merged_data['Act3Price']]
          low = min(saleprice)
          high = max(saleprice)
          merged_data['sale_neighhigh'] = str(int(high) * 1.2)
          merged_data['sale_neighlow'] = str(int(low) * 0.8)
          merged_data['sale_avg'] = str((float(merged_data['neighlow']) + float(merged_data['neighhigh'])) / 2)

          low = min(actvprice)
          high = max(actvprice)
          merged_data['active_neighhigh'] = str(int(high) * 1.2)
          merged_data['active_neighlow'] = str(int(low) * 0.8)
          merged_data['active_avg'] = str((float(merged_data['active_neighlow']) + float(merged_data['active_neighhigh'])) / 2)


          merged_data['SubjectSaleType']=Type_of_Sale(merged_data['SubReoSSale'])
          merged_data['Act1SaleType']=Type_of_Sale(merged_data['Act1SType'])
          merged_data['Act2SaleType']=Type_of_Sale(merged_data['Act2SType'])
          merged_data['Act3SaleType']=Type_of_Sale(merged_data['Act3SType'])
          merged_data['Sold1SaleType']=Type_of_Sale(merged_data['Sold1SType'])
          merged_data['Sold2SaleType']=Type_of_Sale(merged_data['Sold2SType'])
          merged_data['Sold3SaleType']=Type_of_Sale(merged_data['Sold3SType'])



          merged_data['SubjectSaleTypepmi']=Type_of_Sale_pmi(merged_data['SubReoSSale'])
          merged_data['Act1SaleTypepmi']=Type_of_Sale_pmi(merged_data['Act1SType'])
          merged_data['Act2SaleTypepmi']=Type_of_Sale_pmi(merged_data['Act2SType'])
          merged_data['Act3SaleTypepmi']=Type_of_Sale_pmi(merged_data['Act3SType'])
          merged_data['Sold1SaleTypepmi']=Type_of_Sale_pmi(merged_data['Sold1SType'])
          merged_data['Sold2SaleTypepmi']=Type_of_Sale_pmi(merged_data['Sold2SType'])
          merged_data['Sold3SaleTypepmi']=Type_of_Sale_pmi(merged_data['Sold3SType'])

          merged_data['subage']=age(merged_data['SubYBu'])
          merged_data['Act1age']=age(merged_data['Act1Yrbuilt'])
          merged_data['Act2age']=age(merged_data['Act2Yrbuilt'])
          merged_data['Act3age']=age(merged_data['Act3Yrbuilt'])
          merged_data['Sold1age']=age(merged_data['Sold1Yrbuilt'])
          merged_data['Sold2age']=age(merged_data['Sold2Yrbuilt'])
          merged_data['Sold3age']=age(merged_data['Sold3Yrbuilt'])

          merged_data['SubView']=view_split(merged_data['SubView'])
          merged_data['Comp1_view']=view_split(merged_data['Act1View'])
          merged_data['Comp2_view']=view_split(merged_data['Act2View'])
          merged_data['Comp3_view']=view_split(merged_data['Act3View'])
          merged_data['Comp4_view']=view_split(merged_data['Sold1View'])
          merged_data['Comp5_view']=view_split(merged_data['Sold1View'])
          merged_data['Comp6_view']=view_split(merged_data['Sold1View'])

          merged_data['neighbourView']=neighbour_split(merged_data['SubLoc'])
          merged_data['neighbour1_view']=neighbour_split(merged_data['SubLoc'])
          merged_data['neighbour2_view']=neighbour_split(merged_data['SubLoc'])
          merged_data['neighbour3_view']=neighbour_split(merged_data['SubLoc'])
          merged_data['neighbour4_view']=neighbour_split(merged_data['SubLoc'])
          merged_data['neighbour5_view']=neighbour_split(merged_data['SubLoc'])
          merged_data['neighbour6_view']=neighbour_split(merged_data['SubLoc'])

          yesterday = yesterday_date_conversion()
          merged_data['Inspection_Date']=yesterday
          try: 
               merged_data['Act1sqft']= round(float(merged_data['Act1Lot'])*43560)
               merged_data['Act2sqft']= round(float(merged_data['Act2Lot'])*43560)
               merged_data['Act3sqft']= round(int(float(merged_data['Act3Lot'])*43560))
               print(merged_data['Act3sqft'])
               merged_data['Sold1sqft']= round(float(merged_data['Sold1Lot'])*43560)
               merged_data['Sold2sqft']= round(float(merged_data['Sold2Lot'])*43560)
               merged_data['Sold3sqft']= round(float(merged_data['Sold3Lot'])*43560)
               merged_data['SubLotsq']= round(float(merged_data['SubLotac'])*43560)
               merged_data['SubjectListDate']=date_conversion(merged_data['SubListDate'])    
               merged_data['Comp4_Sold_Date']=date_conversion(merged_data['compsolddate4'])    
               merged_data['Comp5_Sold_Date']=date_conversion(merged_data['compsolddate5'])    
               merged_data['Comp6_Sold_Date']=date_conversion(merged_data['compsolddate6'])    
               merged_data['Comp1_Active_Date']=date_conversion(merged_data['compactivedate1'])#orginal list date 
               merged_data['Comp2_Active_Date']=date_conversion(merged_data['compactivedate2'])    
               merged_data['Comp3_Active_Date']=date_conversion(merged_data['compactivedate3'])    
               merged_data['Comp4_Active_Date']=date_conversion(merged_data['compactivedate4'])#orginal list date
               merged_data['Comp5_Active_Date']=date_conversion(merged_data['compactivedate5'])  
               merged_data['Comp6_Active_Date']=date_conversion(merged_data['compactivedate6'])     

               six_months_ago = sixmonth_date()
               if merged_data['Comp4_Sold_Date'] < six_months_ago:
                    merged_data['Error_Comp4_Sold_Date']=merged_data['Comp4_Sold_Date']
               else:
                    merged_data['Error_Comp4_Sold_Date']=''     
               if merged_data['Comp5_Sold_Date'] < six_months_ago:
                    merged_data['Error_Comp5_Sold_Date']=merged_data['Comp5_Sold_Date']
               else: 
                    merged_data['Error_Comp5_Sold_Date']=''    
               if merged_data['Comp6_Sold_Date'] < six_months_ago:
                    merged_data['Error_Comp6_Sold_Date']=merged_data['Comp6_Sold_Date']
               else:
                    merged_data['Error_Comp6_Sold_Date']=''


          except Exception as e:
               print('exception occured in date',e)
          glamax=str(int(merged_data['SubGla'])*1.25)
          glamin=str(int(merged_data['SubGla'])*0.75)
          lotmax=str(float(merged_data['SubLotac'])*1.30)
          lotmin=str(float(merged_data['SubLotac'])*0.70)
          #ybmax=str(int(merged_data['SubYBu'])+20)
          #ybmin=str(int(merged_data['SubYBu'])-20)


          if glamax < merged_data['Act1Gla'] or glamin > merged_data['Act1Gla']:
               merged_data['Error_Act1Gla']=merged_data['Act1Gla']
          else:
              merged_data['Error_Act1Gla']=''     
          if glamax < merged_data['Act2Gla'] or glamin > merged_data['Act2Gla']:
               merged_data['Error_Act2Gla']=merged_data['Act2Gla']
          else:
                merged_data['Error_Act2Gla']=''      
          if glamax < merged_data['Act3Gla'] or glamin > merged_data['Act3Gla']:
               merged_data['Error_Act3Gla']=merged_data['Act3Gla']
          else:
                merged_data['Error_Act3Gla']=''     
          if glamax < merged_data['Sold1Gla'] or glamin > merged_data['Sold1Gla']:
               merged_data['Error_Sold1Gla']=merged_data['Sold1Gla']
          else:
              merged_data['Error_Sold1Gla']=''       
          if glamax < merged_data['Sold2Gla'] or glamin > merged_data['Sold2Gla']:
               merged_data['Error_Sold2Gla']=merged_data['Sold2Gla']
          else:
                 merged_data['Error_Sold2Gla']=''
          if glamax < merged_data['Sold3Gla'] or glamin > merged_data['Sold3Gla']:
               merged_data['Error_Sold3Gla']=merged_data['Sold3Gla']
          else:
                merged_data['Error_Sold3Gla']=''
          if lotmax < merged_data['Act1Lot'] or lotmin > merged_data['Act1Lot']:
               merged_data['Error_Act1Lot']=merged_data['Act1Lot']
          else:
               merged_data['Error_Act1Lot']=''      
          if lotmax < merged_data['Act2Lot'] or lotmin > merged_data['Act2Lot']:
               merged_data['Error_Act2Lot']=merged_data['Act2Lot']
          else:
               merged_data['Error_Act2Lot']='' 
          if lotmax < merged_data['Act3Lot'] or lotmin > merged_data['Act3Lot']:
               merged_data['Error_Act3Lot']=merged_data['Act3Lot']
          else:
               merged_data['Error_Act3Lot']=''  
          if lotmax < merged_data['Sold1Lot'] or lotmin > merged_data['Sold1Lot']:
               merged_data['Error_Sold1Lot']=merged_data['Sold1Lot']
          else:
               merged_data['Error_Sold1Lot']=''     
          if lotmax < merged_data['Sold2Lot'] or lotmin > merged_data['Sold2Lot']:
               merged_data['Error_Sold2Lot']=merged_data['Sold2Gla']
          else:
               merged_data['Error_Sold2Lot']=''
          if lotmax < merged_data['Sold3Lot'] or lotmin > merged_data['Sold3Lot']:
               merged_data['Error_Sold3Lot']=merged_data['Sold3Gla']
          else:
               merged_data['Error_Sold3Lot']='' 


          # if ybmax < merged_data['Act1Yrbuilt'] or ybmin > merged_data['Act1Yrbuilt']:
          #      merged_data['Error_Act1Yrbuilt']=merged_data['Act1Yrbuilt']
          # if ybmax < merged_data['Act2Yrbuilt'] or ybmin > merged_data['Act2Yrbuilt']:
          #      merged_data['Error_Act2Yrbuilt']=merged_data['Act2Yrbuilt']
          # if ybmax < merged_data['Act3Yrbuilt'] or ybmin > merged_data['Act3Yrbuilt']:
          #      merged_data['Error_Act3Yrbuilt']=merged_data['Act3Yrbuilt']
          # if ybmax < merged_data['Sold1Yrbuilt'] or ybmin > merged_data['Sold1Yrbuilt']:
          #      merged_data['Error_Sold1Yrbuilt']=merged_data['Sold1Yrbuilt']
          # if ybmax < merged_data['Sold2Yrbuilt'] or ybmin > merged_data['Sold2Yrbuilt']:
          #      merged_data['Error_Sold2Yrbuilt']=merged_data['Sold2Yrbuilt']
          # if ybmax < merged_data['Sold3Yrbuilt'] or ybmin > merged_data['Sold3Yrbuilt']:
          #      merged_data['Error_Sold3Yrbuilt']=merged_data['Sold3Yrbuilt']

          if merged_data['Act1Cond'] != merged_data['SubPropCond']:
               merged_data['Error_Act1Cond']=merged_data['Act1Cond']
          else:
               merged_data['Error_Act1Cond']='' 
          if merged_data['Act2Cond'] != merged_data['SubPropCond']:
               merged_data['Error_Act2Cond']=merged_data['Act2Cond']
          else:
               merged_data['Error_Act2Cond']=''     
          if merged_data['Act3Cond'] != merged_data['SubPropCond']:
               merged_data['Error_Act3Cond']=merged_data['Act2Cond']
          else:
                merged_data['Error_Act3Cond']=''
          if merged_data['Sold1Cond'] != merged_data['SubPropCond']:
               merged_data['Error_Sold1Cond']=merged_data['Sold1Cond']
          else:
               merged_data['Error_Sold1Cond']=''
          if merged_data['Sold2Cond'] != merged_data['SubPropCond']:
               merged_data['Error_Sold2Cond']=merged_data['Sold2Cond']
          else:
               merged_data['Error_Sold2Cond']=''
          if merged_data['Sold3Cond'] != merged_data['SubPropCond']:
               merged_data['Error_Sold3Cond']=merged_data['Sold3Cond']
          else:
               merged_data['Error_Sold3Cond']='' 



          data1_columns = ['adjconda1', 'bediffa1', 'fbatdiffa1', 'hbatdiffa1', 'gladiffa1', 'ybdiffa1', 'gardiffa1', 'cardiffa1', 'lotdiffa1', 'pooldiffa1', 'adjviewa1', 'totadja1', 'netadja1']
          data2_columns = ['adjconda2', 'bediffa2', 'fbatdiffa2', 'hbatdiffa2', 'gladiffa2', 'ybdiffa2', 'gardiffa2', 'cardiffa2', 'lotdiffa2', 'pooldiffa2', 'adjviewa2', 'totadja2', 'netadja2']
          data3_columns = ['adjconda3', 'bediffa3', 'fbatdiffa3', 'hbatdiffa3', 'gladiffa3', 'ybdiffa3', 'gardiffa3', 'cardiffa3', 'lotdiffa3', 'pooldiffa3', 'adjviewa3', 'totadja3', 'netadja3']
          data4_columns = ['adjconds1', 'bediffs1', 'fbatdiffs1', 'hbatdiffs1', 'gladiffs1', 'ybdiffs1', 'gardiffs1', 'cardiffs1', 'lotdiffs1', 'pooldiffs1', 'adjviews1', 'totadjs1', 'netadjs1']
          data5_columns = ['adjconds2', 'bediffs2', 'fbatdiffs2', 'hbatdiffs2', 'gladiffs2', 'ybdiffs2', 'gardiffs2', 'cardiffs2', 'lotdiffs2', 'pooldiffs2', 'adjviews2', 'totadjs2', 'netadjs2']
          data6_columns = ['adjconds3', 'bediffs3', 'fbatdiffs3', 'hbatdiffs3', 'gladiffs3', 'ybdiffs3', 'gardiffs3', 'cardiffs3', 'lotdiffs3', 'pooldiffs3', 'adjviews3', 'totadjs3', 'netadjs3']      


          merged_data['adjactiv1']=format_data_columns(merged_data, data1_columns)
          merged_data['adjactiv2']=format_data_columns(merged_data, data2_columns)
          merged_data['adjactiv3']=format_data_columns(merged_data, data3_columns)
          merged_data['adjsold1']=format_data_columns(merged_data, data4_columns)
          merged_data['adjsold2']=format_data_columns(merged_data, data5_columns)
          merged_data['adjsold3']=format_data_columns(merged_data, data6_columns)

          try:
               merged_data['compremarks1']=merged_data['compremarks1']#+" Adjustments:"+merged_data['adjactiv1']
          except Exception as e:
               merged_data['compremarks1']=''
               print(e)
          try:     
               merged_data['compremarks2']=merged_data['compremarks2']#+" Adjustments:"+merged_data['adjactiv2']
          except Exception as e:
               merged_data['compremarks2']=''
               print(e)
          try:
               merged_data['compremarks3']=merged_data['compremarks3']#+" Adjustments:"+merged_data['adjactiv3']
          except Exception as e:
               merged_data['compremarks3']=''
               print(e)
          try:
               merged_data['compremarks4']=merged_data['compremarks4']#+" Adjustments:"+merged_data['adjsold1']
          except Exception as e:
               merged_data['compremarks4']=''
               print(e)
          try:
               merged_data['compremarks5']=merged_data['compremarks5']#+" Adjustments:"+merged_data['adjsold2']
          except Exception as e:
               merged_data['compremarks5']=''
               print(e)
          try:
               merged_data['compremarks6']=merged_data['compremarks6']#+" Adjustments:"+merged_data['adjsold3']
          except Exception as e:
               merged_data['compremarks6']=''
               print(e)

          
          merged_data['Best_active_street_address']=best_sold_address(merged_data['Bestactive'])
          merged_data['Best_sold_street_address']=best_sold_address(merged_data['Bestsold'])
         
          if merged_data['Best_active_street_address']!="":
               if merged_data['Best_active_street_address'] in merged_data['Comp1_street_address']:
                    merged_data['Best_active_address']='1'
               elif merged_data['Best_active_street_address'] in merged_data['Comp2_street_address']:
                    merged_data['Best_active_address']='2'     
               elif merged_data['Best_active_street_address'] in merged_data['Comp3_street_address']:
                    merged_data['Best_active_address']='3'  
               else:
                    print("Best Active Not Found")  
                    merged_data['Best_active_address']=''
          else:
               print("Best Active is null") 
               merged_data['Best_active_address']=''
          if merged_data['Best_sold_street_address']!="":
               if merged_data['Best_sold_street_address'] in merged_data['Comp4_street_address']:
                    merged_data['Best_sold_address']='1'
               elif merged_data['Best_sold_street_address'] in merged_data['Comp5_street_address']:
                    merged_data['Best_sold_address']='2'     
               elif merged_data['Best_sold_street_address'] in merged_data['Comp6_street_address']:
                    merged_data['Best_sold_address']='3'  
               else:
                    print("Best Sold Not Found") 
                    merged_data['Best_sold_address']='' 
          else:
               print("Best Sold is null")              
               merged_data['Best_sold_address']=''

          if "Yes" in merged_data['Repairs']:
               merged_data['Repair']="Reparied"
               merged_data['Repair_value']=merged_data['Sugmv']
          else:
               merged_data['Repair']="As Is"     
               merged_data['Repair_value']=""

          if merged_data['County']!='':
               Subcounty=merged_data['County']
               merged_data['Subcounty']=Subcounty.upper()
          else:
               merged_data['Subcounty']=''     
          merged_data['reo']=Reo_condition(merged_data['SubjectSaleType'],merged_data['Act1SType'],merged_data['Act2SType'],merged_data['Act3SType'],merged_data['Sold1SType'],merged_data['Sold2SType'],merged_data['Sold3SType'])

          # if merged_data['Act1Bath']!='':
          #      merged_data['Act1Bath']=int(merged_data['Act1Bath'])
          # else:  
          #      merged_data['Act1Bath'] = 0
          # if merged_data['Act2Bath']:     
          #      merged_data['Act2Bath'] = int(merged_data['Act2Bath'])
          # else: 
          #      merged_data['Act2Bath'] = 0   
          # if merged_data['Act3Bath']:      
          #      merged_data['Act3Bath']=int(merged_data['Act3Bath'])
          # else:
          #      merged_data['Act3Bath'] = 0
          # if merged_data['Sold1Bath']!='':   
          #      merged_data['Sold1Bath'] = int(merged_data['Sold1Bath'])
          # else: 
          #      merged_data['Sold1Bath'] = 0
          # if merged_data['Sold2Bath']!= '':         
          #      merged_data['Sold2Bath']=int(merged_data['Sold2Bath'])
          # else:
          #      merged_data['Sold2Bath'] = 0
          # if merged_data['Sold3Bath']!='':         
          #      merged_data['Sold3Bath']=int(merged_data['Sold3Bath']) 
          # else:
          #      merged_data['Sold3Bath'] = 0
          # if merged_data['Act1Hbath'] !='':          
          #      merged_data['Act1Hbath']=int(merged_data['Act1Hbath'])
          # else: 
          #      merged_data['Act1Hbath'] =0
          # if merged_data['Act2Hbath']!='':        
          #      merged_data['Act2Hbath']=int(merged_data['Act2Hbath'])
          # else:
          #      merged_data['Act2Hbath']=0
          # if merged_data['Act3Hbath']!='':          
          #      merged_data['Act3Hbath'] = int(merged_data['Act3Hbath'])  
          # else:
          #      merged_data['Act3Hbath'] =0
          # if merged_data['Sold1Hbath']!='':
          #     merged_data['Sold1Hbath']=int(merged_data['Sold1Hbath'])
          # else:
          #       merged_data['Sold1Hbath'] = 0
          # if merged_data['Sold2Hbath']!='':      
          #      merged_data['Sold2Hbath']=int(merged_data['Sold2Hbath'])
          # else:
          #      merged_data['Sold2Hbath']= 0
          # if merged_data['Sold3Hbath']!='':          
          #      merged_data['Sold3Hbath']=int(merged_data['Sold3Hbath'])
          # else:
          #      merged_data['Sold3Hbath'] = 0
          # if merged_data['Act1Bed']!='':         
          #      merged_data['Act1Bed']=int(merged_data['Act1Bed'])
          # else: 
          #      merged_data['Act1Bed']=0
          # if merged_data['Act2Bed'] !='':        
          #      merged_data['Act2Bed']=int(merged_data['Act2Bed'])
          # else: 
          #      merged_data['Act2Bed']=0
          # if merged_data['Act3Bed']!='':         
          #      merged_data['Act3Bed']=int(merged_data['Act3Bed'])
          # else:
          #      merged_data['Act3Bed']=0
          # if merged_data['Sold1Bed']!='':          
          #      merged_data['Sold1Bed']=int(merged_data['Sold1Bed'])
          # else:
          #      merged_data['Sold1Bed']=0
          # if merged_data['Sold2Bed']!='':         
          #      merged_data['Sold2Bed']=int(merged_data['Sold2Bed'])
          # else: 
          #      merged_data['Sold2Bed']=0
          # if merged_data['Sold3Bed']!='':         
          #      merged_data['Sold3Bed']=int(merged_data['Sold3Bed'])
          # else:
          #      merged_data['Sold3Bed'] =0    

          # Convert values in merged_data to integers if they are not empty strings, else set them to 0
          # merged_data['Act1Bath'] = int(merged_data['Act1Bath']) if merged_data['Act1Bath'] != '' else 0
          # merged_data['Act2Bath'] = int(merged_data['Act2Bath']) if merged_data['Act2Bath'] else 0
          # merged_data['Act3Bath'] = int(merged_data['Act3Bath']) if merged_data['Act3Bath'] else 0
          # merged_data['Sold1Bath'] = int(merged_data['Sold1Bath']) if merged_data['Sold1Bath'] != '' else 0
          # merged_data['Sold2Bath'] = int(merged_data['Sold2Bath']) if merged_data['Sold2Bath'] != '' else 0
          # merged_data['Sold3Bath'] = int(merged_data['Sold3Bath']) if merged_data['Sold3Bath'] != '' else 0
          # merged_data['Act1Hbath'] = int(merged_data['Act1Hbath']) if merged_data['Act1Hbath'] != '' else 0
          # merged_data['Act2Hbath'] = int(merged_data['Act2Hbath']) if merged_data['Act2Hbath'] != '' else 0
          # merged_data['Act3Hbath'] = int(merged_data['Act3Hbath']) if merged_data['Act3Hbath'] != '' else 0
          # merged_data['Sold1Hbath'] = int(merged_data['Sold1Hbath']) if merged_data['Sold1Hbath'] != '' else 0
          # merged_data['Sold2Hbath'] = int(merged_data['Sold2Hbath']) if merged_data['Sold2Hbath'] != '' else 0
          # merged_data['Sold3Hbath'] = int(merged_data['Sold3Hbath']) if merged_data['Sold3Hbath'] != '' else 0
          # merged_data['Act1Bed'] = int(merged_data['Act1Bed']) if merged_data['Act1Bed'] != '' else 0
          # merged_data['Act2Bed'] = int(merged_data['Act2Bed']) if merged_data['Act2Bed'] != '' else 0
          # merged_data['Act3Bed'] = int(merged_data['Act3Bed']) if merged_data['Act3Bed'] != '' else 0
          # merged_data['Sold1Bed'] = int(merged_data['Sold1Bed']) if merged_data['Sold1Bed'] != '' else 0
          # merged_data['Sold2Bed'] = int(merged_data['Sold2Bed']) if merged_data['Sold2Bed'] != '' else 0
          # merged_data['Sold3Bed'] = int(merged_data['Sold3Bed']) if merged_data['Sold3Bed'] != '' else 0

          merged_data['Act1Bath'] = convert_to_int(merged_data['Act1Bath'])
          merged_data['Act2Bath'] = convert_to_int(merged_data['Act2Bath'])
          merged_data['Act3Bath'] = convert_to_int(merged_data['Act3Bath'])
          merged_data['Sold1Bath'] = convert_to_int(merged_data['Sold1Bath'])
          merged_data['Sold2Bath'] = convert_to_int(merged_data['Sold2Bath'])
          merged_data['Sold3Bath'] = convert_to_int(merged_data['Sold3Bath'])
          merged_data['Act1Hbath'] = convert_to_int(merged_data['Act1Hbath'])
          merged_data['Act2Hbath'] = convert_to_int(merged_data['Act2Hbath'])
          merged_data['Act3Hbath'] = convert_to_int(merged_data['Act3Hbath'])
          merged_data['Sold1Hbath'] = convert_to_int(merged_data['Sold1Hbath'])
          merged_data['Sold2Hbath'] = convert_to_int(merged_data['Sold2Hbath'])
          merged_data['Sold3Hbath'] = convert_to_int(merged_data['Sold3Hbath'])
          merged_data['Act1Bed'] = convert_to_int(merged_data['Act1Bed'])
          merged_data['Act2Bed'] = convert_to_int(merged_data['Act2Bed'])
          merged_data['Act3Bed'] = convert_to_int(merged_data['Act3Bed'])
          merged_data['Sold1Bed'] = convert_to_int(merged_data['Sold1Bed'])
          merged_data['Sold2Bed'] = convert_to_int(merged_data['Sold2Bed'])
          merged_data['Sold3Bed'] = convert_to_int(merged_data['Sold3Bed'])
          merged_data['AsIsSale']=merged_data['Sugmv']
          merged_data['AsIsList']=str(int(merged_data['Sugmv'])+5000)
          merged_data['AsIsQuick_Sale']=str(int(merged_data['Sugmv'])-5000)
          logging.info("Afetr Checking Conditions Merged Data:{}".format(merged_data))



          return merged_data


   