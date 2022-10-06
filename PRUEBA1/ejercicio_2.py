# Ejercicio 2 (18 puntos):
# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes: (IMAGEN ADJUNTA). 
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla lo que tiene que pagar.

def main():
    
    print("DECLARACION DE RENTA \n")
    
    renta_anual = float(input("Ingrese su renta anual en EUROS: \n"))
    print("\n")
    
    
    if renta_anual <= 10000:
        print("Le corresponde pagar 5% en impuestos.")
        pago_final = renta_anual + (renta_anual * 0.05)
        print("El monto a pagar es: \n",pago_final)
    elif renta_anual > 10000 and renta_anual <= 20000:
        print("Le corresponde pagar 15% en impuestos.")
        pago_final = renta_anual + (renta_anual * 0.15)
        print("El monto a pagar es: \n",pago_final)
    elif renta_anual > 20000 and renta_anual <= 35000:
        print("Le corresponde pagar 20% en impuestos.")
        pago_final = renta_anual + (renta_anual * 0.20)
        print("El monto a pagar es: \n",pago_final)
    elif renta_anual > 35000 and renta_anual <= 60000:
        print("Le corresponde pagar 30% en impuestos.")
        pago_final = renta_anual + (renta_anual * 0.30)
        print("El monto a pagar es: \n",pago_final)
    else:
        print("Le corresponde pagar 45% en impuestos.")
        pago_final = renta_anual + (renta_anual * 0.45)
        print("El monto a pagar es: \n"+"$",pago_final)
    
if __name__ == '__main__':
    main()    
    