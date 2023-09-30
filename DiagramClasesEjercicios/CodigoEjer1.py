class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo_bruto):
        super().__init__(nombre, edad)
        self.sueldo_bruto = sueldo_bruto

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Sueldo Bruto: {self.sueldo_bruto}")


class Directivo(Empleado):
    def __init__(self, nombre, edad, sueldo_bruto, categoria, subordinados):
        super().__init__(nombre, edad, sueldo_bruto)
        self.categoria = categoria
        self.subordinados = subordinados

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Categoría: {self.categoria}")
        print(f"Subordinados: {', '.join(self.subordinados)}")


class Cliente(Persona):
    def __init__(self, nombre, edad, telefono_contacto):
        super().__init__(nombre, edad)
        self.telefono_contacto = telefono_contacto

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Teléfono de Contacto: {self.telefono_contacto}")


class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
        self.clientes = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_datos_empleados(self):
        print("Datos de Empleados:")
        for empleado in self.empleados:
            empleado.mostrar_datos()

    def mostrar_datos_clientes(self):
        print("Datos de Clientes:")
        for cliente in self.clientes:
            cliente.mostrar_datos()


# Función para agregar un empleado con datos ingresados por el usuario
def agregar_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    edad = int(input("Ingrese la edad del empleado: "))
    sueldo_bruto = float(input("Ingrese el sueldo bruto del empleado: "))
    return Empleado(nombre, edad, sueldo_bruto)


# Función para agregar un directivo con datos ingresados por el usuario
def agregar_directivo():
    nombre = input("Ingrese el nombre del directivo: ")
    edad = int(input("Ingrese la edad del directivo: "))
    sueldo_bruto = float(input("Ingrese el sueldo bruto del directivo: "))
    categoria = input("Ingrese la categoría del directivo: ")
    subordinados = input("Ingrese los nombres de los subordinados separados por comas: ").split(",")
    return Directivo(nombre, edad, sueldo_bruto, categoria, subordinados)


# Función para agregar un cliente con datos ingresados por el usuario
def agregar_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    edad = int(input("Ingrese la edad del cliente: "))
    telefono_contacto = input("Ingrese el teléfono de contacto del cliente: ")
    return Cliente(nombre, edad, telefono_contacto)


# Ejemplo de uso
empresa = Empresa("Mi Empresa")

# Agregar empleados
num_empleados = int(input("Ingrese el número de empleados a agregar: "))
for _ in range(num_empleados):
    empleado = agregar_empleado()
    empresa.agregar_empleado(empleado)

# Agregar directivos
num_directivos = int(input("Ingrese el número de directivos a agregar: "))
for _ in range(num_directivos):
    directivo = agregar_directivo()
    empresa.agregar_empleado(directivo)

# Agregar clientes
num_clientes = int(input("Ingrese el número de clientes a agregar: "))
for _ in range(num_clientes):
    cliente = agregar_cliente()
    empresa.agregar_cliente(cliente)

# Mostrar datos de empleados y clientes
empresa.mostrar_datos_empleados()
empresa.mostrar_datos_clientes()
