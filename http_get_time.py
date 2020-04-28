import json
import urllib.request

f = urllib.request.urlopen('http://worldtimeapi.org/api/ip')
result = f.readline()
print(result)
print("===========\n")
fields = json.loads(result)
print(fields["datetime"])