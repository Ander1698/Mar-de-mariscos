# Menu, las funciones del menu no funcionan por que estan en construccion de codigo
def incluir_insumo():  
    print("Opción en construcción")

def consultar_platos():  
    print("Opción en construcción")


def aplicar_descuento():  
    print("Opción en construcción")

def generar_reporte():  
    print("Opción en construcción")

def mostrar_menu():  
    print("\nMenú de opciones:")
    print("1. Incluir Insumo")
    print("2. Consultar Platos")
    print("3. Aplicar Descuento/Promoción")
    print("4. Generar Reporte de Costos")
    print("5. modificar)
    print("6. Salir")

def menu_secundario():
    print("\n¿Quieres volver al menú principal?")
    print("1. Sí")
    print("2. No (Salir)")

    # Variable que almacena opción seleccionada por el usuario
    opcion_secundaria = None  # Almacena la respuesta del usuario sobre si quiere regresar al menú

    # repite hasta que el usuario ingresa una opción válida
    while True:
        try:
            # El usuario elige si quiere volver al menú o salir
            opcion_secundaria = int(input("Seleccione una opción: "))
            
            if opcion_secundaria == 1:
                return True  # Volver al menú principal
            elif opcion_secundaria == 2:
                print("Saliendo del sistema...")
                return False  # Salir del sistema
            else:
                print("Opción no válida. Intente nuevamente.")  # Si la opción no es válida
        except ValueError:
            print("Por favor, ingrese un número válido.")  # Si el usuario ingresa algo que no es un número

# Función principal que ejecuta el flujo principal del programa
def main():  # Controla el flujo del programa y llama a las funciones dependiendo de la opción del menú
    # Variable para almacenar la opción seleccionada por el usuario del menú principal
    opcion = None  # Guarda la opción seleccionada por el usuario del menú principal
    
    while True:
        mostrar_menu()  # Muestra el menú principal
        
        try:
            # El usuario elige una opción del menú
            opcion = int(input("Seleccione una opción: "))
            
            # Según la opción seleccionada, se llama a la función correspondiente
            if opcion == 1:
                incluir_insumo()
            elif opcion == 2:
                consultar_platos()
            elif opcion == 3:
                aplicar_descuento()
            elif opcion == 4:
                generar_reporte()
            elif opcion ==5:
                aplicar_modificacion()
                 modificar = input("Igresar el código a modificar")
                   for x in range(len(código)):
                       if código[x] == modificar:
                           comida[x] = input("ingresar nuevo platillo")
                           precio[x] = int(input("ingresar nuevo precio"))
                   print("platillo modificado")
            elif opcion == 6:
                print("Saliendo del sistema...")
                break  # Si selecciona "Salir", termina el ciclo y finaliza el programa
            else:
                print("Opción no válida. Intente nuevamente.")  # Si la opción no es válida

            # Preguntar al usuario si quiere volver al menú principal o salir
            if not menu_secundario():
                break  # Si selecciona "No", salir del ciclo y terminar el programa
        except ValueError:
            print("Por favor, ingrese un número válido.")  # Si el usuario ingresa algo que no es un número

# Inicia el programa
if __name__ == "__main__":
    main()


