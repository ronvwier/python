'''
Read the values from the sunpanels OMNIK inverter

The OMNIK type inverter can be read for realtime values
'''

import omnik

x = omnik.OMNIK('192.168.0.133')
x.read()

print('Serial number :', x.serialNumber)
print('Yield Today   :', x.yieldToday, ' kWh')
print('Yield Total   :', x.yieldTotal, ' kWh')

