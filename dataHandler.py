import websocket
import json
import pandas as pd
from datetime import datetime

ws = websocket.WebSocket()
ws.connect("ws://65.2.131.93:8000")
ws.send(json.dumps({"timeperiod":"1m"}))
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if(current_time>"15:30:00"):
        break
    else:
        data=ws.recv()
        print(data)
        data=json.loads(data)
        df1 = pd.read_csv("/home/vava/Programming/Python/scrapping/nifty/Niftyprice.csv")
        count=len(df1.index)
        df2=pd.DataFrame()
        df2["time_series"]=[count]
        df2["price"]=[data["price"]]
        data=[df1,df2]
        df1=pd.concat(data, ignore_index = True)
        print(df1)
        df1.to_csv("Niftyprice.csv",index=False)


        



