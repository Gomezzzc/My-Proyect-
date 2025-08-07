import json
import os

ARCHIVO = 'proyect.json'

def leer_datos():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def mostrar_datos():
    datos = leer_datos()
    if not datos:
        print(" No hay datos registrados.")
        return
    print("\nLista de personas:")
    for d in datos:
        print(f"ID: {d['id']} | {d['nombre']} {d['apellido']} | Edad: {d['edad']} | Correo: {d['correo']} | Teléfono: {d['telefono']}")

def agregar_dato():
    datos = leer_datos()
    nuevo_id = 1 if not datos else datos[-1]['id'] + 1
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    while True:
        try:
            edad = int(input("Edad: ").strip())
            break
        except ValueError:
            print("Por favor ingresa un número válido para la edad.")
    correo = input("Correo: ").strip()
    telefono = input("Teléfono: ").strip()
    nuevo = {
        "id": nuevo_id,
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "correo": correo,
        "telefono": telefono
    }
    datos.append(nuevo)
    with open(ARCHIVO, 'w') as f:
        json.dump(datos, f, indent=4)
    print(" Persona agregada.")

def actualizar_dato():
    datos = leer_datos()
    if not datos:
        print(" No hay datos para actualizar.")
        return
    mostrar_datos()
    try:
        id_buscar = int(input("ID de la persona a actualizar: "))
    except ValueError:
        print(" ID inválido.")
        return
    for d in datos:
        if d['id'] == id_buscar:
            nuevo_nombre = input(f"Nuevo nombre (actual: {d['nombre']}): ").strip() or d['nombre']
            nuevo_apellido = input(f"Nuevo apellido (actual: {d['apellido']}): ").strip() or d['apellido']
            nueva_edad_input = input(f"Nueva edad (actual: {d['edad']}): ").strip()
            if nueva_edad_input:
                try:
                    nueva_edad = int(nueva_edad_input)
                except ValueError:
                    print("Edad inválida. Se mantiene la actual.")
                    nueva_edad = d['edad']
            else:
                nueva_edad = d['edad']
            nuevo_correo = input(f"Nuevo correo (actual: {d['correo']}): ").strip() or d['correo']
            nuevo_telefono = input(f"Nuevo teléfono (actual: {d['telefono']}): ").strip() or d['telefono']

            d['nombre'] = nuevo_nombre
            d['apellido'] = nuevo_apellido
            d['edad'] = nueva_edad
            d['correo'] = nuevo_correo
            d['telefono'] = nuevo_telefono

            with open(ARCHIVO, 'w') as f:
                json.dump(datos, f, indent=4)
            print("✅ Persona actualizada.")
            return
    print(" ID no encontrado.")

def borrar_dato():
    datos = leer_datos()
    if not datos:
        print(" No hay datos para borrar.")
        return
    mostrar_datos()
    try:
        id_borrar = int(input("ID de la persona a borrar: "))
    except ValueError:
        print(" ID inválido.")
        return
    nuevos_datos = [d for d in datos if d['id'] != id_borrar]
    if len(nuevos_datos) == len(datos):
        print(" ID no encontrado.")
    else:
        with open(ARCHIVO, 'w') as f:
            json.dump(nuevos_datos, f, indent=4)
        print(" Persona borrada.")

def menu():
    while True:
        print("\n--- MENÚ CRUD ---")
        print("1. Agregar persona")
        print("2. Mostrar personas")
        print("3. Actualizar persona")
        print("4. Borrar persona")
        print("5. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == '1':
            agregar_dato()
        elif opcion == '2':
            mostrar_datos()
        elif opcion == '3':
            actualizar_dato()
        elif opcion == '4':
            borrar_dato()
        elif opcion == '5':
            print(" Saliendo...")
            break
        else:
            print(" Opción inválida.")

if __name__ == "__main__":
    menu()



