import uuid
import re

# Estructura de datos para almacenar los clientes
lista_clientes = []

# --- Funciones para la gestión de clientes ---

# Crear un nuevo cliente
def crear_cliente(nombre, tipo, telefono, direccion, servicios):
    cliente = {
        "id": generar_id_cliente(),
        "nombre": nombre,
        "tipo": tipo,
        "telefono": telefono,
        "direccion": direccion,
        "servicios": servicios,
        "historial_servicios": []
    }
    return cliente

# Buscar un cliente por ID
def buscar_cliente_por_id(id_cliente, lista_clientes):
    for cliente in lista_clientes:
        if cliente["id"] == id_cliente:
            return cliente
    return None

# Buscar un cliente por nombre
def buscar_cliente_por_nombre(nombre_cliente, lista_clientes):
    resultados = []
    for cliente in lista_clientes:
        if cliente["nombre"] == nombre_cliente:
            resultados.append(cliente)
    return resultados

# Agregar un servicio a un cliente
def agregar_servicio_a_cliente(cliente, servicio):
    cliente["servicios"].append(servicio)
    cliente["historial_servicios"].append(servicio)

# Actualizar la información de contacto de un cliente
def actualizar_contacto(cliente, telefono, correo_electronico):
    cliente["telefono"] = telefono
    cliente["correo_electronico"] = correo_electronico

# Eliminar un cliente
def eliminar_cliente(id_cliente, lista_clientes):
    for i, cliente in enumerate(lista_clientes):
        if cliente["id"] == id_cliente:
            del lista_clientes[i]
            return True
    return False

# --- Funciones para la gestión de servicios ---

# Crear un nuevo servicio
def crear_servicio(nombre, descripcion, fecha_contratacion):
    servicio = {
        "nombre": nombre,
        "descripcion": descripcion,
        "fecha_contratacion": fecha_contratacion
    }
    return servicio

# --- Funciones auxiliares ---

# Generar un ID único para cada cliente
def generar_id_cliente():
    return str(uuid.uuid4())

# Validar el formato del número de teléfono
def validar_telefono(telefono):
    patron = re.compile(r"^\d{10}$")  # 10 dígitos
    return patron.match(telefono) is not None

# --- Funciones para la interfaz de usuario ---

# Mostrar el menú principal
def mostrar_menu():
    print("\n--- Aplicación de Gestión de Clientes Sky ---")
    print("1. Crear cliente")
    print("2. Buscar cliente por ID")
    print("3. Buscar cliente por nombre")
    print("4. Agregar servicio a cliente")
    print("5. Actualizar contacto de cliente")
    print("6. Eliminar cliente")
    print("7. Salir")

# Obtener la opción del usuario
def obtener_opcion():
    mostrar_menu()
    opcion = input("Ingrese el número de la opción deseada: ")
    return opcion

# --- Bucle principal de la aplicación ---

while True:
    opcion = obtener_opcion()

    if opcion == "1":
        # Crear cliente
        nombre = input("Ingrese el nombre del cliente: ")
        tipo = input("Ingrese el tipo de cliente (persona/negocio): ")
        telefono = input("Ingrese el teléfono del cliente: ")
        while not validar_telefono(telefono):
            print("Teléfono inválido. Debe tener 10 dígitos.")
            telefono = input("Ingrese el teléfono del cliente: ")
        direccion = input("Ingrese la dirección del cliente: ")
        servicios = input("Ingrese los servicios contratados (separados por comas): ").split(",")

        nuevo_cliente = crear_cliente(nombre, tipo, telefono, direccion, servicios)
        lista_clientes.append(nuevo_cliente)
        print("Cliente creado con éxito.")
        print(f"ID del cliente: {nuevo_cliente['id']}")  # Agregamos esta línea

    elif opcion == "2":
        # Buscar cliente por ID
        id_cliente = input("Ingrese el ID del cliente a buscar: ")
        cliente_encontrado = buscar_cliente_por_id(id_cliente, lista_clientes)

        if cliente_encontrado:
            print("Cliente encontrado:")
            print(cliente_encontrado)
        else:
            print("Cliente no encontrado.")

    elif opcion == "3":
        # Buscar cliente por nombre
        nombre_cliente = input("Ingrese el nombre del cliente a buscar: ")
        clientes_encontrados = buscar_cliente_por_nombre(nombre_cliente, lista_clientes)

        if clientes_encontrados:
            print("Clientes encontrados:")
            for cliente in clientes_encontrados:
                print(cliente)
        else:
            print("No se encontraron clientes con ese nombre.")

    elif opcion == "4":
        # Agregar servicio a cliente
        id_cliente = input("Ingrese el ID del cliente al que desea agregar un servicio: ")
        cliente_encontrado = buscar_cliente_por_id(id_cliente, lista_clientes)

        if cliente_encontrado:
            nombre_servicio = input("Ingrese el nombre del servicio a agregar: ")
            descripcion_servicio = input("Ingrese la descripción del servicio: ")
            fecha_contratacion = input("Ingrese la fecha de contratación del servicio: ")
            nuevo_servicio = crear_servicio(nombre_servicio, descripcion_servicio, fecha_contratacion)
            agregar_servicio_a_cliente(cliente_encontrado, nuevo_servicio)
            print("Servicio agregado al cliente con éxito.")
        else:
            print("Cliente no encontrado.")

    elif opcion == "5":
        # Actualizar contacto de cliente
        id_cliente = input("Ingrese el ID del cliente cuyo contacto desea actualizar: ")
        cliente_encontrado = buscar_cliente_por_id(id_cliente, lista_clientes)

        if cliente_encontrado:
            telefono = input("Ingrese el nuevo teléfono del cliente: ")
            while not validar_telefono(telefono):
                print("Teléfono inválido. Debe tener 10 dígitos.")
                telefono = input("Ingrese el nuevo teléfono del cliente: ")
            correo_electronico = input("Ingrese el nuevo correo electrónico del cliente: ")
            actualizar_contacto(cliente_encontrado, telefono, correo_electronico)
            print("Contacto del cliente actualizado con éxito.")
        else:
            print("Cliente no encontrado.")

    elif opcion == "6":
        # Eliminar cliente
        id_cliente = input("Ingrese el ID del cliente que desea eliminar: ")
        if eliminar_cliente(id_cliente, lista_clientes):
            print("Cliente eliminado con éxito.")
        else:
            print("Cliente no encontrado.")

    elif opcion == "7":
        # Salir
        print("Saliendo de la aplicación...")
        break

    else:
        print("Opción inválida. Por favor, ingrese un número entre 1 y 7.")