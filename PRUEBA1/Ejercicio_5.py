# Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. 
# Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 19%.


def iva(total_sin_iva, monto_iva):
    if (monto_iva == ''):
        monto_iva = 19
        monto_iva = int(monto_iva)

    monto_iva = int(monto_iva)
    valor_iva = total_sin_iva * (monto_iva / 100)
    monto_total = valor_iva + total_sin_iva
    return monto_total

def main():
    valor_neto = int(input("Ingrese el valor de la factura: "))
    valor_iva = str(input("Ingrese el porcentaje del IVA: "))
    total_a_pagar = iva(valor_neto,valor_iva)
    print("El total con IVA de la factura es: $" + str(total_a_pagar))


if __name__ == '__main__':
    main()