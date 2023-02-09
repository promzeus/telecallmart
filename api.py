import hashlib
import requests
import base64 
import pandas
from datetime import datetime

method = "GET"
URI = "/did/sms/123123123"
userId = "345345345345"
timestamp = str(int(round(datetime.now().timestamp())) * 1000)
apiKey = "999999999999999999999999"
 
message = userId + apiKey + timestamp + URI + method

m = hashlib.sha256()
m.update(message.encode('utf-8'))
messageHash = m.digest()

apiHeader = base64.b64encode(messageHash)

headers = {"Accept": "application/json", "apiKey": apiHeader, "x-date-unix": timestamp, "x-user-id": userId}

r = requests.get(url = "https://www.telecallmart.com/api/did/sms/123123123", headers = headers)

print("Status Code", r.status_code)

messages = pandas.read_json(r.text).head(10)

messages.body = messages.body.apply(lambda x: base64.b64decode(x).decode('utf-8'))

display(messages)
