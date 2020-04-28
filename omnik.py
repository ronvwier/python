'''
Web interface to the OMNIK inverter

The OMNIK type inverter can be read for realtime values
'''

import urllib.request

class OMNIK:
    '''
    OMNIK class to access the OMNIK inverter
    '''    
   
    def __init__(self,ip_address):
        '''
        OMNIK instance takes the IP address of the OMNIK inverter
        '''
        self.ip_address = ip_address

    def read(self):
        '''
        Read the realtime data from the OMNIK inverter
        '''
        
        f = urllib.request.urlopen('http://' + self.ip_address + '/js/status.js')
        result = str(f.readline(),encoding="utf-8")
        x = result.split('var webData="')
        y = x[1].split('"')
        z = y[0]
        self.fields = z.split(",")

    @property
    def age(self):
        '''Age off the data in minutes at moment of read()'''
        return int(self.fields[9])
    
    @property
    def serialNumber(self):
        '''The serial number of the inverter'''
        return self.fields[0]
    
    @property
    def firmwareVersionMain(self):
        '''Main firmware version'''
        return self.fields[1]
    
    @property
    def firmwareVersionSlave(self):
        '''Slave firmware version'''
        return self.fields[2]
    
    @property
    def model(self):
        '''Model of the inverter'''
        return self.fields[3]
    
    @property
    def ratedPower(self):
        '''Rated power of the inverter in W'''
        return int(self.fields[4])
    
    @property
    def currentPower(self):
        '''CurrentPower in W'''
        return int(self.fields[5])
    
    @property
    def yieldToday(self):
        '''Todays yield in kWh'''
        return int(self.fields[6]) / 100
    
    @property
    def yieldTotal(self):
        '''Total yield kWh'''
        return int(self.fields[7]) / 10

    @property
    def alarms(self):
        '''Alarms'''
        return int(self.fields[8])
