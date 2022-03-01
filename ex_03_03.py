punt= input('Ingrese puntuacion: ')
try :
    p= float(punt)
    if p<=0 or p>=1.0 :
        print('Ingrese una puntuacion correcta')
    elif p>= 0.9 :
        print('A')
    elif p>= 0.8 and p<0.9 :
        print('B')
    elif p>=0.7 and p<0.8 :
        print('C')
    elif p>=0.6 and p<0.7:
        print('D')
    else :
        if p<0.6 :
            print('F')
except :
    print('Ingrese una calificacion correcta')
