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
  