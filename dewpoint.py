import math

temp = 18.0
hum = 57.0
xdp = 9

temp = 18.9
hum = 51
xdp = 8.6

def alfa(T, RH):
    a = 17.27  
    b=237.7
    return ((a * T)/(b + T)) + math.log(RH/100.0)

def dp(T, RH):
    a = 17.27  
    b=237.7
    return ((b*alfa(T, RH))/(a-alfa(T, RH)))

print(temp)
print(hum)
print(dp(temp, hum),xdp)