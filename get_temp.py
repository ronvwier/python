import urllib.request

f = urllib.request.urlopen('http://api.thingspeak.com/apps/thinghttp/send_request?api_key=FZE8AGBTF35GT2N9')
result=f.read().decode('utf-8')
print(result)