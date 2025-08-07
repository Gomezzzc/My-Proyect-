ARCHIVO = 'new work.json'

def leer():
    try:
        with open(ARCHIVO, 'r') as f:
            return [line.strip() for line in f]
    except:
        return []

def guardar(nombres):
    with open(ARCHIVO, 'w') as f:
        f.write('\n'.join(nombres))

def mostrar():
    for i, nombre in enumerate(leer(), 1):
        print(f"{i}. {nombre}")

def agregar():
    nombres = leer()
    nombres.append(input("Nombre: ").strip())
    guardar(nombres)

def actualizar():
    nombres = leer()
    mostrar()
    i = int(input("Número a cambiar: ")) - 1
    nombres[i] = input("Nuevo nombre: ").strip()
    guardar(nombres)

def borrar():
    nombres = leer()
    mostrar()
    i = int(input("Número a borrar: ")) - 1
    del nombres[i]
    guardar(nombres)

def menu():
    while True:
        op = input("1)Agregar 2)Mostrar 3)Cambiar 4)Borrar 5)Salir: ")
        if op == '1': agregar()
        elif op == '2': mostrar()
        elif op == '3': actualizar()
        elif op == '4': borrar()
        elif op == '5': break

menu()
