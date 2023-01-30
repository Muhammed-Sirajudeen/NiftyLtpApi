import asyncio
import websockets
import json
import requests
from bs4 import BeautifulSoup

def scrapper():
    
    url="https://economictimes.indiatimes.com/indices/nifty_50_companies"
    headers = {'User-Agent': 'Mozilla/5.0'}
    html_content = requests.get(url,headers=headers).text
    soup = BeautifulSoup(html_content, "html.parser")
    val=soup.find_all("div",{"id":"ltp"})
    return val[0].get_text()


import asyncio
 
import websockets
 
# create handler for each connection
 
async def handler(websocket, path):
 
    data = await websocket.recv()
 
    jsondata=json.loads(data)
    if(jsondata["timeperiod"]=="1m"):
        interval=55
    elif(jsondata["timeperiod"]=="5m"):
        interval=295
    while True:
        value=scrapper()
        await websocket.send(json.dumps({"timeperiod":interval,"price":value}))
        await asyncio.sleep(interval)


    
 
 
start_server = websockets.serve(handler, "0.0.0.0", 8000)
 
 
 
asyncio.get_event_loop().run_until_complete(start_server)
 
asyncio.get_event_loop().run_forever()