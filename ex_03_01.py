hrs = input('enter hours: ')
tarf= input('tarifa por hora: ')
h = float(hrs)
t= float(tarf)
if h>40 :
    print(40*t+((h-40)*(t*1.5)))
else :
    print(h*t)
