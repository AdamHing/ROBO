# sign into the leader account and accept the friend requests from the followers 
#this code sends messages not friend requests

import ROBLOSECURITY as rbs
ROBLOSECURITY = rbs.ROBLOSECURITY()

# sends a message 
import requests

cookie = ROBLOSECURITY
auth_response = requests.post("https://auth.roblox.com/v1/logout", headers = {"cookie": f".ROBLOSECURITY={cookie}"})

if auth_response.status_code == 403:
    if "x-csrf-token" in auth_response.headers:
        token = auth_response.headers["x-csrf-token"]

headers = {
    "cookie": f".ROBLOSECURITY={cookie}",
    "x-csrf-token": token
}

data = {
    "userId": 839071378, # your user id
    "subject": "testtest",
    "body": "This is a test, lol",
    "recipientId": 2494645060 # recipient's user Id
}

message_response = requests.post("https://privatemessages.roblox.com/v1/messages/send", headers = headers, data = data)
print(message_response.json())  