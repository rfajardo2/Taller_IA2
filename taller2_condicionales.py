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
total_camisas_pagar1 = precio_camisa1 * cantidad_camisa1
descuento1 = 0.0
if(precio_camisa1 < 0 or cantidad_camisa1 < 0):
    print("Por favor verificar datos digitados, los datos no pueden ser menor a 0")
    print(f" precio de la camisa digitado: ${precio_camisa1:,}")
    print(f" cantidad de la camisa digitado:{cantidad_camisa1}")
else:
    if(cantidad_camisa1 >= 3):
        descuento1 = total_camisas_pagar1 * 0.3
    else:
        descuento1 = total_camisas_pagar1 * 0.1
    total_camisas_pagar_descuento1 = total_camisas_pagar1 - descuento1
    print(f"El total a pagar es: ${total_camisas_pagar_descuento1:,}")
    print(f"El descuento aplicado es: ${descuento1:,}")
    print(f"El valor unitario es: ${precio_camisa1:,}")
    print(f"La cantidad comprade es: {cantidad_camisa1}")


# 2. En un supermercado se hace una promoción, mediante la cual el
# cliente obtiene un descuento dependiendo de un número que se
# escoge al azar. Si el número escogido es menor que 74 el descuento
# es del 15% sobre el total de la compra, si es mayor o igual a 74 el
# descuento es del 20%. Obtener cuanto dinero se le descuenta.

precio_compra2 = float(input("Digite el total de la compra: $"))
nuemo_azar2 = int(input("Digite un nuemro al azar mayor o igual a 0: "))
descuento2 = 0.0
if(precio_compra2 < 0 or nuemo_azar2 < 0):
    print("Por favor verificar datos digitados, los datos no pueden ser menor a 0")
    print(f" precio de la compra ${precio_compra2:,}")
    print(f" nuemro al azar digitado:{nuemo_azar2}")
else:
    if(nuemo_azar2 < 74):
        descuento2 = precio_compra2 * 0.15
    else:
        descuento2 = precio_compra2 * 0.2
    total_a_pagar_descuento2 = precio_compra2 - descuento2
    print(f"El total a pagar es: ${total_a_pagar_descuento2:,}")
    print(f"El descuento aplicado es: ${descuento2:,}")
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
    porcentaje_cuota3 = 0.0
    if(monto3 < 50000):
        porcentaje_cuota3 = 0.03
    else:
        porcentaje_cuota3 = 0.02
    cuota3 = monto3 * porcentaje_cuota3
    print(f"El total del monto a financiar es: ${monto3:,}")
    print(f"El porcentaje aplicado es: {porcentaje_cuota3}")
    print(f"El valor de la cuota es: ${cuota3:,}")


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
        multa4 = ganancia_semana4 * 0.5
    print(f"El promedio de puntos es: {promedio4}")
    print(f"Las ganancias en la semana fueron de: ${ganancia_semana4:,}")
    print(f"La multa por la revision es de: ${multa4:,}")


# 5. Una persona se encuentra con un problema de comprar un automóvil
# o un terreno, los cuales cuestan exactamente lo mismo. Sabe que
# mientras el automóvil se devalúa, con el terreno sucede lo contrario.
# Esta persona comprará el automóvil si al cabo de tres años la
# devaluación de este no es mayor que la mitad del incremento del
# valor del terreno. Ayúdale a esta pesona a determinar si debe o no
# comprar el automóvil.

precio5 = float(input("Digite el precio del terreno o automovil: "))
porcentaje_incremento5 = float(input("Digite el incremento anual del terreno: %"))
porcentaje_decremento5 = float(input("Digite la devaluacion anual del automovil: %"))
print("_____________________________________________________________")
incremento5 = (((precio5 * porcentaje_incremento5) / 100) * 3) / 2
decremento5 = ((precio5 * porcentaje_decremento5) / 100) * 3
print(f"La mitad del incremento de la casa en 3 años es: ${incremento5:,}")
print(f"La devaluacion del automovil en 3 años es: ${decremento5:,}")
if(decremento5 < incremento5):
    print("Te conviene comprar el Automovil")
else:
    print("Te conviene comprar el terreno")


# 6. En una fábrica de computadoras se planea ofrecer a los clientes un
# descuento que dependerá del número de computadoreas que
# compre. Si las computadoras son menos de cinco se les dará un 10%
# de descuento sobre el total de la compra; si el número de
# computadoras es mayor o igual a cinco pero menos de diez se le
# otorga un 20% de descuento; y si son 10 o más se les da un 40%. El
# precio de cada computadora es de $11.000.


precio_pc6 = 11000
cantidad_pc6 = int(input("Digite cantidad de computadoras a comprar: "))
total_pc_pagar6 = precio_camisa1 * cantidad_camisa1
descuento6 = 0.0
if(precio_pc6 < 0):
    print("Por favor verificar datos digitados, los datos no pueden ser menor a 0")
    print(f" cantidad de las computadoras digitado:{cantidad_pc6}")
else:
    if(cantidad_pc6 < 5):
        descuento6 = total_pc_pagar6 * 0.1
    elif(cantidad_pc6 >= 5 and cantidad_pc6 < 10):
        descuento6 = total_pc_pagar6 * 0.2
    else:
        descuento6 = total_pc_pagar6 * 0.4
    total_cp_pagar_descuento = total_pc_pagar6 - descuento6
    print("_____________________________________________________________")
    print(f"El total a pagar es: ${total_cp_pagar_descuento:,}")
    print(f"El descuento aplicado es: ${descuento6:,}")
    print(f"El valor unitario es: ${precio_pc6:,}")
    print(f"La cantidad comprade es: {cantidad_pc6}")


# 7. Un proveedor de estéreos ofrece un descuento del 10% sobre el
# precio sin IVA, de algún aparato si este cuesta $2000 o más. Además,
# independientemente de esto, ofrece un 5% de descuento si la marca
# es NOSY. Determinar cuanto pagará, con IVA incluido, un cliente
# cualquiera por la compra de su aparato. IVA es del 16%.


precio_estereo7 = float(input("Digite el precio del estéreo: $"))
marca_estero7 = (input("Digite la marca del estéreos a comprar: "))
print("_____________________________________________________________")
descuento_compra7 = 0.0
descuento_marca7 = 0.0
iva7 = 0.16
if(precio_estereo7 < 0):
    print("Por favor verificar datos digitados, los datos no pueden ser menor a 0")
    print(f" precio del estéreo digitado: ${precio_estereo7:,}")
else:
    if(precio_estereo7 >= 2000):
        descuento_compra7 = precio_estereo7 * 0.1
    if(marca_estero7 == "NOSY" or marca_estero7 == "nosy"):
        descuento_marca7 = precio_estereo7 * 0.05
    subtotal_pagar_descuento7 = precio_estereo7 - descuento_compra7 - descuento_marca7
    valor_iva7 = subtotal_pagar_descuento7 * iva7
    total_pagar_descuento7 = subtotal_pagar_descuento7 + valor_iva7
    print(f"El valor unitario es: ${precio_estereo7:,}")
    print(f"El descuento aplicado por compra es: ${descuento_compra7:,}")
    print(f"El descuento aplicado por marca es: ${descuento_marca7:,}")
    print(f"El subtotal es: ${subtotal_pagar_descuento7:,}")
    print(f"El iva(16%) es: ${valor_iva7:,}")
    print(f"El subtotal es: ${total_pagar_descuento7:,}")


# 8.Una empresa quiere hacer una compra de varias piezas de la misma
# clase a una fábrica de refacciones. La empresa, dependiendo del
# monto total de la compra, decidirá que hacer para pagar al fabricante.
# Si el monto total de la compra excede de $500.000 la empresa tendrá
# la capacidad de invertir de su propio dinero un 55% del monto de la
# compra, pedir prestado al banco un 30% y el resto lo pagará
# solicitando un crédito al fabricante. Si el monto total de la compra no
# excede de $500.00 la empresa tendrá capacidad de invertir de su
# propio dinero un 70% y el restante 30% lo pagará solicitando crédito
# al fabricante. El fabricante cobra por concepto de interes un 20%
# sobre la cantidad que se le pague a crédito. Obtener la cantidad a
# inverir, valor del préstamo, valor del crédito y los intereses.


cantidad_piesas8 = int(input("Digite el numero de piezas: "))
precio_piesas8 = float(input("Digite el costo de la pieza: $"))

sub_total8 = cantidad_piesas8 * precio_piesas8
inversion8 = 0.0
banco8 = 0.0
credito8 = 0.0
if(sub_total8 > 500000):
    inversion8 = sub_total8 * 0.55
    banco8 = sub_total8 * 0.30
    credito8 = sub_total8 * 0.15
else:
    inversion8 = sub_total8 * 0.70
    banco8 = 0
    credito8 = sub_total8 * 0.30
interes8 = credito8 * 0.20

print(f"La inversion es de: ${inversion8:,}")
print(f"El prestamo del banco es de: ${banco8:,}")
print(f"El credito a pagar es por: ${credito8:,}")
print(f"El interes por el credito es: ${interes8:,}")


# 9. Leer 2 números; si son iguales que lo multiplique, si el primero es
# mayor que el segundo que los reste y sino que los sume.


primer_numero9 = float(input("Digite el primer numero:"))
segundo_numero9 = float(input("Digite el segundo numero:"))

resultado9 = 0
if(primer_numero9 == segundo_numero9):
    resultado9 = primer_numero9 * segundo_numero9
    operador9 = "*"
else:
    if(primer_numero9 < segundo_numero9):
        resultado9 = primer_numero9 + segundo_numero9
        operador9 = "+"
    else:
        resultado9 = primer_numero9 - segundo_numero9
        operador9 = "-"
print(f"{primer_numero9} {operador9} {segundo_numero9} = {resultado9}")


# 10.Leer tres números diferentes e imprimir el número mayor de los tres.

primer_numero10 = float(input("Digite el primer numero:"))
segundo_numero10 = float(input("Digite el segundo numero:"))
tercer_numero10 = float(input("Digite el tercer numero:"))

if(primer_numero10 > segundo_numero9 and primer_numero10 > tercer_numero10):
    mayor10 = primer_numero10
    print(f"El numero mayor es: {mayor10}")
elif(segundo_numero9 > primer_numero10 and segundo_numero9 > tercer_numero10):
    mayor10 = segundo_numero9
    print(f"El numero mayor es: {mayor10}")
elif(tercer_numero10 > primer_numero10 and tercer_numero10 > segundo_numero9):
    mayor10 = tercer_numero10
    print(f"El numero mayor es: {mayor10}")
else:
    print("los numeros son iguales")















