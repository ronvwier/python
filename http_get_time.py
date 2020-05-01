import json
import urllib.request

f = urllib.request.urlopen('http://worldtimeapi.org/api/ip')
result = str(f.readline(),encoding='utf-8')
print(result)
print("===========\n")
fields = json.loads(result)
print(fields["datetime"])
