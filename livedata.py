import requests
import json
from pythonping import *

target = "www.google.com"

def jprint(obj):
    # Create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
response = requests.get("http://worldclockapi.com/api/json/utc/now")


print("===UTCtime========ping=======")
while 0==0 : 
    # get the ping
    response_list = ping(target,count=10)
    currentping = str(response_list.rtt_avg_ms)
    #extract the time from the JSON
    Time=response.json()["currentDateTime"][11:16]
    #create the output
    Time = "= " + Time + " = 10ping: " + currentping + " ms ="
    print(Time, end = "\r")
    #get the time
    response = requests.get("http://worldclockapi.com/api/json/utc/now")



