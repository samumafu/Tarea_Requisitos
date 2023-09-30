class Cliente:
    def __init__(self, dni, nombre, direccion, telefono, codigo_unico):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.codigo_unico = codigo_unico
        self.avalador = None

    def asignar_avalador(self, avalador):
        self.avalador = avalador

    def mostrar_datos(self):
        print(f"DNI: {self.dni}, Nombre: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}, Código Único: {self.codigo_unico}")
        if self.avalador:
            print(f"Avalado por: {self.avalador.nombre}")


class Coche:
    def __init__(self, matricula, modelo, color, marca, garaje):
        self.matricula = matricula
        self.modelo = modelo
        self.color = color
        self.marca = marca
        self.garaje = garaje

    def mostrar_datos(self):
        print(f"Matrícula: {self.matricula}, Modelo: {self.modelo}, Color: {self.color}, Marca: {self.marca}")
        print(f"Garaje: {self.garaje}")


class Garaje:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


class Reserva:
    def __init__(self, cliente, coches, agencia, fecha_inicio, fecha_final, precio_alquiler, litros_gasolina, precio_total, entregado):
        self.cliente = cliente
        self.coches = coches
        self.agencia = agencia
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self.precio_alquiler = precio_alquiler
        self.litros_gasolina = litros_gasolina
        self.precio_total = precio_total
        self.entregado = entregado

    def mostrar_datos(self):
        print("Datos de la Reserva:")
        self.cliente.mostrar_datos()
        print("Coches:")
        for coche in self.coches:
            coche.mostrar_datos()
        print(f"Agencia: {self.agencia}")
        print(f"Fecha de inicio: {self.fecha_inicio}, Fecha de finalización: {self.fecha_final}")
        print(f"Precio de alquiler: {self.precio_alquiler}, Litros de gasolina: {self.litros_gasolina}")
        print(f"Precio total: {self.precio_total}, Entregado: {self.entregado}")


def agregar_cliente():
    dni = input("Ingrese el DNI del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    codigo_unico = input("Ingrese el código único del cliente: ")
    return Cliente(dni, nombre, direccion, telefono, codigo_unico)


def agregar_coche():
    matricula = input("Ingrese la matrícula del coche: ")
    modelo = input("Ingrese el modelo del coche: ")
    color = input("Ingrese el color del coche: ")
    marca = input("Ingrese la marca del coche: ")
    garaje_nombre = input("Ingrese el nombre del garaje del coche: ")
    garaje = Garaje(garaje_nombre)
    return Coche(matricula, modelo, color, marca, garaje)


def agregar_reserva(clientes, coches):
    print("Lista de clientes:")
    for i, cliente in enumerate(clientes):
        print(f"{i + 1}. {cliente.nombre} - Código Único: {cliente.codigo_unico}")

    cliente_index = int(input("Ingrese el número del cliente que realizará la reserva: ")) - 1
    cliente = clientes[cliente_index]

    print("Lista de coches disponibles:")
    for i, coche in enumerate(coches):
        print(f"{i + 1}. {coche.modelo} - Matrícula: {coche.matricula}")

    coche_indices = input("Ingrese los números de los coches separados por comas para la reserva (por ejemplo, 1,2): ").split(",")
    coches_reserva = [coches[int(index) - 1] for index in coche_indices]

    agencia = input("Ingrese el nombre de la agencia de la reserva: ")
    fecha_inicio = input("Ingrese la fecha de inicio de la reserva (YYYY-MM-DD): ")
    fecha_final = input("Ingrese la fecha de finalización de la reserva (YYYY-MM-DD): ")
    precio_alquiler = float(input("Ingrese el precio de alquiler por día: "))
    litros_gasolina = float(input("Ingrese los litros de gasolina en el depósito: "))
    precio_total = precio_alquiler * len(coches_reserva)
    entregado = input("¿El coche ha sido entregado? (Sí/No): ").lower() == "sí"

    return Reserva(cliente, coches_reserva, agencia, fecha_inicio, fecha_final, precio_alquiler, litros_gasolina, precio_total, entregado)


# Ejemplo de uso
clientes = []
coches = []

# Agregar clientes
num_clientes = int(input("Ingrese el número de clientes a agregar: "))
for _ in range(num_clientes):
    cliente = agregar_cliente()
    clientes.append(cliente)

# Agregar coches
num_coches = int(input("Ingrese el número de coches a agregar: "))
for _ in range(num_coches):
    coche = agregar_coche()
    coches.append(coche)

# Crear una reserva
reserva = agregar_reserva(clientes, coches)

# Mostrar datos de la reserva
reserva.mostrar_datos()
