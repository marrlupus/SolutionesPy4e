def computepay(a, b):
    if a>40 :
        return(40*b+((a-40)*(b*1.5)))
    else :
        return(a*b)

hrs = input("Enter Hours:")
tarf= input('tarifa por hora: ')
h=float(hrs)
t=float(tarf)
p = computepay(h, t)
print("Pay", p)
