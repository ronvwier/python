import json
import urllib.request

f = urllib.request.urlopen('http://worldtimeapi.org/api/ip')
result=json.load(f)
print(result)
print("===========\n")
print(result['datetime'])