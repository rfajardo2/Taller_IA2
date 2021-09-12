# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 09:39:39 2021

@author: Desarrollo RUBEN Fajardo 
"""
# 1.Hacer un algoritmo que calcule el total a pagar por la compra de
# camisas. Si se compran tres camisas o mas se aplica un descuento
# del 30% sobre el total de la compra y si son menos de tres camisas
# un descuento del 10%.

precio_camisa1 = float(input("Digite el precio de la camisa: $"))
cantidad_camisa1 = int(input("Digite cantidad de la camisa a comprar: "))
total_camisas_pagar = precio_camisa1 * cantidad_camisa1
descuento = 0.0
if(precio_camisa1 < 0 or cantidad_camisa1 < 0):
    print("Por favor verificar datos digitados, los datos no pueden ser menor a 0")
    print(f" precio de la camisa digitado: ${precio_camisa1:,}")
    print(f" cantidad de la camisa digitado:{cantidad_camisa1}")
else:
    if(cantidad_camisa1 >= 3):
        descuento = total_camisas_pagar * 0.3
    else:
        descuento = total_camisas_pagar * 0.1
    total_camisas_pagar_descuento = total_camisas_pagar - descuento
    print(f"El total a pagar es: ${total_camisas_pagar_descuento:,}")
    print(f"El descuento aplicado es: ${descuento:,}")
    print(f"El valor unitario es: ${precio_camisa1:,}")
    print(f"La cantidad comprade es: {cantidad_camisa1}")


# 2. En un supermercado se hace una promoción, mediante la cual el
# cliente obtiene un descuento dependiendo de un número que se
# escoge al azar. Si el número escogido es menor que 74 el descuento
# es del 15% sobre el total de la compra, si es mayor o igual a 74 el
# descuento es del 20%. Obtener cuanto dinero se le descuenta.

precio_compra2 = float(input("Digite el total de la compra: $"))
nuemo_azar2 = int(input("Digite un nuemro al azar mayor o igual a 0: "))
descuento = 0.0
if(precio_compra2 < 0 or nuemo_azar2 < 0):
    print("Por favor verificar datos digitados, los datos no pueden ser menor a 0")
    print(f" precio de la compra ${precio_compra2:,}")
    print(f" nuemro al azar digitado:{nuemo_azar2}")
else:
    if(nuemo_azar2 < 74):
        descuento = precio_compra2 * 0.15
    else:
        descuento = precio_compra2 * 0.2
    total_a_pagar_descuento = precio_compra2 - descuento
    print(f"El total a pagar es: ${total_a_pagar_descuento:,}")
    print(f"El descuento aplicado es: ${descuento:,}")
    print(f"El valor dela compra era de: ${precio_compra2:,}")
    print(f"El nuemro al azar digitado es: {nuemo_azar2}")


# 3.Una compañía de seguros está abriendo un departamento de
# finanzas y estableció un programa para captar clientes, que conssite
# en lo siguiente: Si el monto por el que se efectúa la fianza es menor
# que $50.000 la cuota a pagar será por el 3% del monto, y si el monto
# es mayor que $50.000 la cuota a pagar será el 2% del monto. La
# afianzadora desea determinar cual será la cuota que debe pagar al
# cliente.


monto3 = float(input("Digite el total del monto a financiar: $"))
if(monto3 < 0):
    print("verificar datos digitados, los datos no pueden ser menor a 0")
    print(f" monto a financiar: ${monto3:,}")
else:
    porcentaje_cuota = 0.0
    if(monto3 < 50000):
        porcentaje_cuota = 0.03
    else:
        porcentaje_cuota = 0.02
    cuota = monto3 * porcentaje_cuota
    print(f"El total del monto a financiar es: ${monto3:,}")
    print(f"El porcentaje aplicado es: {porcentaje_cuota}")
    print(f"El valor de la cuota es: ${cuota:,}")


# 4. Una fábrica ha sido sometida a un programa de control de
# contaminación para lo cual se efectúa una revisión de los puntos de
# contaminación generados por la fábrica. El programa de control de
# contaminación consiste en medir los puntos que emite la fábrica en
# cinco días de una semana y si el promedio es superior a los 170
# puntos entonces tendrá la sanción de parar su producción por una
# semana y una multa del 50% de las ganancias diarias cuando no se
# detiene la producción. Si el promedio obtenido de puntos es de 170 o
# menos entonces no tendrá ni sanción ni multa. El dueño de la fábrica
# desea saber cuanto dinero perderá después de ser sometido a la
# revisión.


putos_primer_dia4 = float(input("Digite los punto del dia #1: "))
putos_segundo_dia4 = float(input("Digite los punto del dia #2: "))
putos_tercer_dia4 = float(input("Digite los punto del dia #3: "))
putos_cuarto_dia4 = float(input("Digite los punto del dia #4: "))
putos_quinto_dia4 = float(input("Digite los punto del dia #5: "))
print("_____________________________________________________________")
ganancias_primer_dia4 = float(input("Digite las ganacias del dia #1: "))
ganancias_segundo_dia4 = float(input("Digite las ganacias del dia #2: "))
ganancias_tercer_dia4 = float(input("Digite las ganacias del dia #3: "))
ganancias_cuarto_dia4 = float(input("Digite las ganacias del dia #4: "))
ganancias_quinto_dia4 = float(input("Digite las ganacias del dia #5: "))
print("_____________________________________________________________")
promedio4 = (putos_primer_dia4 + putos_segundo_dia4 + putos_tercer_dia4 + putos_cuarto_dia4 + putos_quinto_dia4) / 5
ganancia_semana4 = (ganancias_primer_dia4 + ganancias_segundo_dia4 + ganancias_tercer_dia4 + ganancias_cuarto_dia4 + ganancias_quinto_dia4)
multa4 = 0.0
if(putos_primer_dia4 < 0
   or putos_segundo_dia4 < 0
   or putos_tercer_dia4 < 0
   or putos_cuarto_dia4 < 0
   or putos_quinto_dia4 < 0
   or ganancias_primer_dia4 < 0
   or ganancias_segundo_dia4 < 0
   or ganancias_tercer_dia4 < 0
   or ganancias_cuarto_dia4 < 0
   or ganancias_quinto_dia4 < 0):
    print("Por favor verificar datos digitados, los datos no pueden ser menor a 0")
else:
    if(promedio4 > 170):
        multa4 = ganancia_semana4 * 0.05
    print(f"El promedio de puntos es: {promedio4}")
    print(f"Las ganancias en la semana fueron de: ${ganancia_semana4:,}")
    print(f"La multa por la revision es de: ${multa4:,}")












