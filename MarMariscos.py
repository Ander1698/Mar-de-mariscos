# Función para limpiar la pantalla de la terminal
import os
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

# Función para agregar insumos al inventario 5 maximo por insumo
def incluir_insumo(insumos):
    limpiar_pantalla()
    max_insumos = 5
    while len(insumos) < max_insumos:
        nombre = input("Ingrese el nombre del insumo: ")
        codigo = str(len(insumos)).zfill(2)
        cantidad = int(input(f"\n¿Cuántos '{nombre}' desea guardar? (máximo 5): "))
        if cantidad > 5:
            print("\nLa cantidad máxima permitida por insumo es 5.")
            continue
        insumos[codigo] = {"nombre": nombre, "cantidad": cantidad}
        print(f"\nInsumo '{nombre}' con código {codigo} guardado correctamente.")
        continuar = input("\n¿Desea guardar otro insumo? (si/no): ").lower()
        if continuar != "si":
            break

# Función para mostrar el menú de los platillos
def consultar_platos(platos):
    print("\n--- Menú de Platos ---")
    for i, (nombre, precio) in enumerate(platos):
        descuento = " (15% de descuento)" if nombre in ["Coctel de mariscos", "Sopa de mariscos", "Arroz con mariscos", "Tacos de pescado"] else ""
        print(f"{i+1}. {nombre} - {precio} colones{descuento}")

# Función para mostrar menu de las bebidas
def consultar_bebidas():
    bebidas = [
        "Piña colada", "Mojito", "Cerveza artesanal", "Whisky con hielo", "Ron con Coca-Cola",
        "Margarita", "Gaseosa de naranja", "Agua tónica", "Refresco natural de tamarindo", "Limonada con hierbabuena"
    ]
    print("\n--- Menú de Bebidas (2000 colones cada una) ---")
    for i, bebida in enumerate(bebidas):
        print(f"{i+1}. {bebida} - 2000 colones")

# Función para seleccionar platillo
def seleccionar_platillo(platos):
    consultar_platos(platos)
    try:
        opcion = int(input("\nSeleccione el número del platillo que desea: ")) - 1
        if 0 <= opcion < len(platos):
            platillo, precio = platos[opcion]
            tiene_descuento = platillo in ["Coctel de mariscos", "Sopa de mariscos", "Arroz con mariscos", "Tacos de pescado"]
            print(f"\nUsted seleccionó: {platillo} - {precio} colones")
            return platillo, precio, tiene_descuento
        else:
            print("\nOpción inválida.")
    except ValueError:
        print("\nEntrada no válida.")
    return None, 0, False

# Función para seleccionar bebida
def seleccionar_bebida():
    bebidas = [
        "Piña colada", "Mojito", "Cerveza artesanal", "Whisky con hielo", "Ron con Coca-Cola",
        "Margarita", "Gaseosa de naranja", "Agua tónica", "Refresco natural de tamarindo", "Limonada con hierbabuena"
    ]
    consultar_bebidas()
    try:
        opcion = int(input("\nSeleccione el número de la bebida que desea: ")) - 1
        if 0 <= opcion < len(bebidas):
            bebida = bebidas[opcion]
            print(f"\nUsted seleccionó: {bebida} - 2000 colones")
            return bebida, 2000
        else:
            print("\nOpción inválida.")
    except ValueError:
        print("\nEntrada no válida.")
    return None, 0

# Función creada por Francini para modificar insumos o platillos
def modificar_elemento(insumos, platos):
    print("\n¿Desea modificar un insumo o un platillo?")
    eleccion = input("Escriba 'insumo' o 'platillo': ").lower()
    if eleccion == "insumo":
        for codigo, insumo in insumos.items():
            print(f"Código {codigo}: {insumo['nombre']} - Cantidad: {insumo['cantidad']}")
        codigo = input("\nIngrese el código del insumo a modificar: ")
        if codigo in insumos:
            nuevo_nombre = input("Nuevo nombre: ")
            nueva_cantidad = int(input("Nueva cantidad: "))
            insumos[codigo] = {"nombre": nuevo_nombre, "cantidad": nueva_cantidad}
            print("Insumo modificado correctamente.")
        else:
            print("Código no encontrado.")
    elif eleccion == "platillo":
        consultar_platos(platos)
        nombre_actual = input("Ingrese el nombre del platillo a modificar: ")
        for i, (nombre, precio) in enumerate(platos):
            if nombre.lower() == nombre_actual.lower():
                nuevo_nombre = input("Nuevo nombre: ")
                nuevo_precio = int(input("Nuevo precio: "))
                platos[i] = (nuevo_nombre, nuevo_precio)
                print("Platillo modificado correctamente.")
                return
        print("Platillo no encontrado.")
    else:
        print("Opción no válida.")

# Función creada por Francini para borrar insumos o platillos
def borrar_elemento(insumos, platos):
    print("\n¿Desea borrar un insumo o un platillo?")
    eleccion = input("Escriba 'insumo' o 'platillo': ").lower()
    if eleccion == "insumo":
        for codigo, insumo in insumos.items():
            print(f"Código {codigo}: {insumo['nombre']} - Cantidad: {insumo['cantidad']}")
        codigo = input("Ingrese el código del insumo a borrar: ")
        if codigo in insumos:
            del insumos[codigo]
            print("Insumo eliminado correctamente.")
        else:
            print("Código no encontrado.")
    elif eleccion == "platillo":
        consultar_platos(platos)
        nombre = input("Ingrese el nombre del platillo a borrar: ")
        for i, (nombre_platillo, _) in enumerate(platos):
            if nombre_platillo.lower() == nombre.lower():
                del platos[i]
                print("Platillo eliminado correctamente.")
                return
        print("Platillo no encontrado.")
    else:
        print("Opción no válida.")

# Nueva opción: Lista de insumos
def listar_insumos(insumos):
    if not insumos:
        print("\nNo hay insumos registrados.")
    else:
        print("\n--- Lista de Insumos ---")
        for codigo, insumo in insumos.items():
            print(f"Código {codigo}: {insumo['nombre']} - Cantidad: {insumo['cantidad']}")

# Menú para empleados
def menu_empleados(insumos, platos):
    while True:
        print("\n--- Menú para Empleados ---")
        print("1. Agregar insumo")
        print("2. Ver menú de platillos")
        print("3. Lista de insumos")
        print("4. Modificar (platillo o insumo)")
        print("5. Borrar (platillo o insumo)")
        print("6. Salir")
        try:
            opcion = int(input("\nSeleccione una opción: "))
            if opcion == 1:
                incluir_insumo(insumos)
            elif opcion == 2:
                consultar_platos(platos)
            elif opcion == 3:
                listar_insumos(insumos)
            elif opcion == 4:
                modificar_elemento(insumos, platos)
            elif opcion == 5:
                borrar_elemento(insumos, platos)
            elif opcion == 6:
                break
            else:
                print("\nOpción inválida.")
        except ValueError:
            print("\nPor favor, ingrese un número válido.")

# Menú para usuarios
def menu_usuarios(platos):
    total = 0
    while True:
        print("\n--- Menú para Usuarios ---")
        print("1. Ver menú de platillos")
        print("2. Ver bebidas")
        print("3. Seleccionar platillo")
        print("4. Seleccionar bebida")
        print("5. Ver total y pagar")
        print("6. Salir")
        try:
            opcion = int(input("\nSeleccione una opción: "))
            if opcion == 1:
                consultar_platos(platos)
            elif opcion == 2:
                consultar_bebidas()
            elif opcion == 3:
                platillo, precio, descuento = seleccionar_platillo(platos)
                if platillo:
                    if descuento:
                        rebaja = precio * 0.15
                        precio -= rebaja
                        print(f"\nDescuento aplicado: -{int(rebaja)} colones")
                    total += precio
            elif opcion == 4:
                bebida, precio_bebida = seleccionar_bebida()
                if bebida:
                    total += precio_bebida
            elif opcion == 5:
                print(f"\nTotal a pagar: {int(total)} colones")
                print("\nOpciones de pago:")
                print("1. Tarjeta")
                print("2. Efectivo")
                metodo = input("Seleccione opción de pago: ")
                if metodo == "1":
                    monto = int(input("Ingrese el monto a pagar con tarjeta: "))
                    if monto < total:
                        print("Transacción denegada: monto insuficiente.")
                    else:
                        print("Transacción realizada con éxito.")
                elif metodo == "2":
                    monto = int(input("Ingrese el monto en efectivo: "))
                    if monto < total:
                        print("Pago insuficiente.")
                    else:
                        vuelto = monto - total
                        print(f"Pago aceptado. Vuelto: {vuelto} colones")
            elif opcion == 6:
                break
            else:
                print("\nOpción inválida.")
        except ValueError:
            print("\nPor favor, ingrese un número válido.")

# Menú principal
def menu():
    insumos = {}
    platos = [
        ("Pulpo a la gallega", 8000),
        ("Langosta al ajillo", 7500),
        ("Pescado entero frito", 5500),
        ("Coctel de mariscos", 10500),
        ("Sopa de mariscos", 7000),
        ("Arroz con mariscos", 5000),
        ("Tacos de pescado", 4500)
    ]
    while True:
        print("\n--- MarMariscos Sistema ---")
        print("1. Menú de empleados")
        print("2. Menú de usuarios")
        print("3. Salir")
        try:
            seleccion = int(input("\nSeleccione una opción: "))
            if seleccion == 1:
                menu_empleados(insumos, platos)
            elif seleccion == 2:
                menu_usuarios(platos)
            elif seleccion == 3:
                print("\n¡Gracias por usar MarMariscos!")
                break
            else:
                print("\nOpción inválida.")
        except ValueError:
            print("\nPor favor, ingrese un número válido.")

# Ejecutar programa
if __name__ == "__main__":
    menu()

















