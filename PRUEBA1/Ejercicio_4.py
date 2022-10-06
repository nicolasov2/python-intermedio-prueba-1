# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
# Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

def main():
    
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lenguaje"]
    for i in range(len(asignaturas)-1, -1, -1):
        notas = float(input("Ingresa tu nota en " + asignaturas[i] + ": "))
        if notas >= 4 and notas <=7:
            asignaturas.pop(i)
    print("\nTienes que repetir " + str(asignaturas))

if __name__ == '__main__':
    main()


