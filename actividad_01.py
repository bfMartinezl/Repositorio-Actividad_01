# -*- coding: utf-8 -*-
"""
Created on Thursday Jun  2 7:27:28 2022

@author: HP EliteBook 2470p
"""
#iniciamos al acceso de las funciones matematicas con import math
import math
#Se toma la decision de quiere pasar de decimal a grados o de grados a decimal 
print("Seleccione un número para hacer la conversion: ")
print("1. Grados, Minutos, Segundos -> Grados Decimales")
print("2. Grados Decimales -> Grados, Minutos, Segundos")
#Colocamos esta funcion para que el usuario escoga un numero entero, 1 o 2
seleccion = int(input("> "))
#Se coloca una condicionante si el usuario escoge la opcion 1.
if seleccion == 1:
    print("Selecconaste Grados, Minutos, Segundos a Grados Decimales")
    Gdos = int(input("Por favor ingresar grados: "))
    MINUTOS = int(input("Por favor ingresar minutos: "))
    SEGUNDOS = float(input("Por favor ingresar segundos: "))
#Se realizan los calculos respectivos para que se haga la conversion.    
    min_x = SEGUNDOS/60 + MINUTOS
#Se pone la funcion round para redondear a tres cifras.
    grados_valor_x = round(((min_x)/60 + Gdos), 3)
#Se define una funcion referente al resultado final y dentro iran los mismos calculos por si hay cualquier error
    def gmd(grados_valor_x):    
        min_x = SEGUNDOS/60 + MINUTOS
        grados_valor_x = round(((min_x)/60 + Gdos), 3)
#Devuelve el resultado
        return (grados_valor_x) 
#Se imprime el resultado   
    print ("El resultados es: ", grados_valor_x,"°")
#A traves de esta condicionante, si el usario escogio la opcion 2
elif seleccion == 2:
    print("Has seleccionado convertir Grados Decimales a Grados, Minutos, Segundos")
#Se pone la funcion float, ya que el usuario tendra que trabajar con decimales y no enteros.
    lat = float(input("Ingrese el valor de la latitud en decimales: "))
    lon = float(input("Ingrese el valor de la longitud en decimales: "))
#Se realizan los calculos para hacer las distintas conversiones, para latitud como longitud
    grados_lat = abs(int(lat))
    z = abs(float((lat)))-abs(int(lat))
    MINUTOS = int(z * 60)
    MIN2 = float(z *60)
    a = abs(float((MIN2)))-abs(int(MIN2))
    SEGUNDOS = float(a*60)

    grados_lon = abs(int(lon))
    deci_grados = abs(float((lon)))-abs(int(lon))
    MINUTOS = int(deci_grados * 60)
    MIN2 = float(deci_grados *60)
    deci_grados_min2 = abs(float((MIN2)))-abs(int(MIN2))
    SEGUNDOS = float(deci_grados_min2*60)
#Se define una funcion referente al resultado final y dentro iran los mismos calculos

    def dms(lon,lat):
        grados_lon = abs(int(lon))
        deci_grados = abs(float((lon)))-abs(int(lon))
        MINUTOS = int(deci_grados * 60)
        MIN2 = float(deci_grados *60)
        deci_grados_min2 = abs(float((MIN2)))-abs(int(MIN2))
       
#Se colocan condicionantes en donde si el usuario escoge una cordenada mayor a 0    
    if lon >= 0:
        numero_lon = "E"
    else:
        numero_lon = "W"

        Gdos_lat = abs(int(lat))
        z = abs(float((lat)))-abs(int(lat))
        MINUTOS = int(z * 60)
        MIN2 = float(z *60)
        a = abs(float((MIN2)))-abs(int(MIN2))
        SEGUNDOS = float(a*60)
#Se vuelve a colocar condicionantes en donde si el usuario escoge una cordenada mayor a 0, se le otorgara la direccion al norte y en el caso contrario,
# la direccion sur
    if lat >= 0:
        numero_lat = "N"
    else:
        numero_lat = "S"
#Se imprimiran los resultados  de longitud y latitud 
    print('Su valor de latitud es:')
    y = f"{Gdos_lat}° {MINUTOS}' {SEGUNDOS:.2f}''{numero_lat}"
    print(y)
    
    print('Su valor de longitud es:')
    x = f"{grados_lon}° {MINUTOS}' {SEGUNDOS:.2f}'' {numero_lon}"
    print(x)
#Se pone esta condicionante por si el usuario no coloca la opcion 1 o 2  
else:
    seleccion < 1 and seleccion > 2
    print("La opcion escogida no es valida :(. Escoger entre 1 y 2")