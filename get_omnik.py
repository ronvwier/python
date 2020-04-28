'''
Read the values from the sunpanels OMNIK inverter

The OMNIK type inverter can be read for realtime values
'''

import omnik

x = omnik.OMNIK('192.168.0.133')
x.read()

print(x.serialNumber)
print(x.yieldToday)
print(x.yieldTotal)

