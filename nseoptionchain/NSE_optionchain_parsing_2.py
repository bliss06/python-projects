#Below code to parse jason data recieved from NSE INDIA website
#Later we will use this code to display a chart at runtime dynamically
import json
import math
import os.path, time
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk


#we need to parse n strikes down and n strikes up from ATM for both PE and CE
chosen_strikes_range = [1000,900,800,700,600,500,400,300,200,100,0,-100,-200,-300,-400,-500,-600,-700,-800,-900,-1000]
#chosen_strikes_range = [2000,1900,1800,1700,1600,1500,1400,1300,1200,1100,1000,900,800,700,600,500,400,300,200,100,0,-100,-200,-300,-400,-500,-600,-700,-800,-900,-1000,-1100,-1200,-1300,-1400,-1500,-1600,-1700,-1800,-1900,-2000]

counter = 0
prevtimestamp = None
oldtimestamp = None
option_chain_all = []
option_chain_all_strikes = []
today_dmy = time.strftime("%d%m%Y")
while True:
    try:
        #Sometimes this might happen when the other script is in process of creating this file, in that case try again after 5 seconds
        option_chain_file = open("BNF_OC_MAIN.txt", "r")
    except OSError as error:
        print(error)
        continue
    
    optionchain_data = json.loads(option_chain_file.read())
    if prevtimestamp == os.path.getmtime('BNF_OC_MAIN.txt'):
        option_chain_file.close()
        #This file is already processed hence skip
        continue
    prevtimestamp = os.path.getmtime('BNF_OC_MAIN.txt')

    print("last modified: %s" % time.ctime(prevtimestamp))
    option_chain_file.close()
    timestamp = optionchain_data['records']['timestamp']
    if oldtimestamp == timestamp:
        option_chain_file.close()
        #This data is already processed hence skip, sometimes NSE data update stalls repeating the same dataset
        continue
    oldtimestamp = timestamp
    spot_price = (optionchain_data['records']['underlyingValue']//100)*100 #rounding to nearest hundred
    index_data =  optionchain_data['records']['index'] #This again is a dictionary
    symbol = index_data['indexSymbol']
    advances = index_data['advances']
    declines = index_data['declines']
    put_call_data = optionchain_data['records']['data']
    current_expiry = optionchain_data['records']['expiryDates'][0]
    if counter == 0:
        chosen_strikes = [x + spot_price for x in chosen_strikes_range] #adding the spot price to above range for getting the strikes we are interested in

    counter = counter + 1
    #put_list = []
    #call_list =[]
    option_chain_summary = []
    option_chain_total = []
    for current_strike in put_call_data:

        #if current_strike['strikePrice'] in chosen_strikes and current_strike['expiryDate'] == current_expiry:
        #We need only 20 strikes above and 20 strikes below open price for the day analysis
        if current_strike['strikePrice'] in chosen_strikes and current_strike['expiryDate'] == current_expiry:
            #parse current put and call data
            #option_chain_row = {'time':timestamp, 'expiry':current_expiry,'strike':current_strike['strikePrice'], 'call_oi':current_strike['CE']['openInterest'],'call_oi_change':current_strike['CE']['changeinOpenInterest'],'call_ltp':current_strike['CE']['lastPrice'],'spot_price':current_strike['CE']['underlyingValue'],'put_oi':current_strike['PE']['openInterest'],'put_oi_change':current_strike['PE']['changeinOpenInterest'],'put_ltp':current_strike['PE']['lastPrice']}
            row_strike = current_strike['strikePrice']
            try:
                row_call_oi = current_strike['CE']['openInterest']
            except KeyError as error:
                row_call_oi = 0;
            try:
                row_call_oi_change = current_strike['CE']['changeinOpenInterest']
            except KeyError as error:
                row_call_oi_change = 0;
            try:
                row_call_ltp = current_strike['CE']['lastPrice']
            except KeyError as error:
                row_call_ltp = 0;

            try:
                row_spot_price = current_strike['CE']['underlyingValue']
            except KeyError as error:
                row_spot_price = 0;
            
            
            
            
            
            try:
                row_put_oi = current_strike['PE']['openInterest']
            except KeyError as error:
                row_put_oi = 0;
            try:
                row_put_oi_change = current_strike['PE']['changeinOpenInterest']
            except KeyError as error:
                row_put_oi_change = 0;
            try:
               row_put_ltp = current_strike['PE']['lastPrice']
            except KeyError as error:
                row_put_ltp = 0;
            
            
            option_chain_row = {'time':timestamp, 'expiry':current_expiry,'strike':row_strike, 'call_oi':row_call_oi,'call_oi_change':row_call_oi_change,'call_ltp':row_call_ltp,'spot_price':row_spot_price,'put_oi':row_put_oi,'put_oi_change':row_put_oi_change,'put_ltp':row_put_ltp}
            #option_chain_row = {'time':timestamp, 'expiry':current_expiry,'strike':current_strike['strikePrice'], 'call_oi':current_strike['CE']['openInterest'],'call_oi_change':current_strike['CE']['changeinOpenInterest'],'call_ltp':current_strike['CE']['lastPrice'],'spot_price':current_strike['CE']['underlyingValue'],'put_oi':current_strike['PE']['openInterest'],'put_oi_change':current_strike['PE']['changeinOpenInterest'],'put_ltp':current_strike['PE']['lastPrice']}
            option_chain_total.append(option_chain_row)
            #if current_strike['strikePrice'] in chosen_strikes :
                #option_chain_summary.append(option_chain_row)
            
    ##Now convert the above into a pandas dataframe and plot graph
    #option_chain_all.extend(option_chain_summary)
    option_chain_all_strikes.extend(option_chain_total)
    
    #df = pd.DataFrame(option_chain_summary)
    #df.to_csv("Option chain summary" + today_dmy + ".csv")
    #df.to_csv("Option chain summary-" + str(counter) +"-"+ time.strftime("%d%m%Y-%H%M%S") + ".csv")

    df = pd.DataFrame(option_chain_total)
    df.to_csv("Option chain latest" + today_dmy + ".csv")
    df_all = pd.DataFrame(option_chain_all_strikes)
    df_all.to_csv("Option chain " + today_dmy + " Complete.csv")

    print(df)
    time.sleep(220)

    

