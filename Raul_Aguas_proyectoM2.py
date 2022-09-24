#Proyecto de coordenadas
x = input("Ingrese su valor en 'x': ") #En esta seccion coloco las entradas dadas por el usuario
y = input("Ingrese su valor en 'y': ")
if x.isnumeric() and y.isnumeric(): #Si la variable 'x' y 'y' son numericos continua el programa si no me manda un mensaje de valor incorrecto
    print('Verificando en que cuadrante se encuentra su coordenada:')
    x = float(x)    #Aqui al cumplirse la condicion de que se haya entrado un valor numerico los convierto a numeros flotatantes para incluir puntos decimales
    y = float(y)
else: 
    print('Dato incorrecto, favor de introducir numeros')
    exit () #Si la condicion no se cumple manda mensa de dato incorrecto y cierra programa
if x == 0 and y == 0:  #Si las condiciones anteriores se cumple, ejecuta el programa y verifica donde se encuentra la coordenada introducida.
    print ('La coordenada se encuentra en el origen')
elif x > 0 and y > 0:
    print('La coordenada se encuentra en el cuadrante I')
elif x > 0 and y == 0: 
    print('La coordenada se encuentra en el Eje +X')
elif x == 0 and y > 0:
    print('La coordenada se encuentra en el Eje +Y')
elif x < 0 and y > 0:
    print('La coordenada se encuentra en el cuadrante II')
elif x < 0 and y == 0:
    print('La coordenada se encuentra en el eje -X')
elif x == 0 and y < 0:
    print('La coordenada se encuentra en el cuadrante -Y')
elif x < 0 and y < 0:
    print('La coordenada se encuentra en el cuadrante III')
elif x > 0 and y < 0:
    print('La coordenada se encuentra en el cuadrante IIII') 
else :
        print('Datos incorrectos favor de introducir numeros')





