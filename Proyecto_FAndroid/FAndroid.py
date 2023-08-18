class casoFandroid:
    def __init__(self, nombre, correo):
        self.nombre = nombre 
        self.correo = correo
        self.tarjeta = None 
        self.carrito = []
        self.datos_personales = {
            "nombre" : self.nombre,
            "correo" : self.correo
        }
        self.puntos = 0
        
    def vincular_tarjeta(self):
        marca = input('Ingresa la marca de la tarjeta:')
        numero = input('Ingresa el numero de la tarjeta:')
        vencimiento = input('Fecha de vencimiento (MM/AA):')
        codigo = input('Codigo de verificacion (respaldo)')

        self.tarjeta = {
            "Marca": marca,
            "Numero": numero,
            "Vencimiento": vencimiento,
            "Codigo": codigo
        }
        print("Tarjeta de crédito vinculada con éxito")
    
    def modificar_datos(self):
        self.nombre = input("Ingresa un nuevo nombre: ")
        self.correo = input("Ingresa un nuevo correo: ")
        print('Datos actualizados con éxito')

    def comprar_producto(self, producto):
        self.carrito.append(producto)
        self.puntos += 1
        print(f'{producto} agregado al carrito')
    
    def ver_compras(self):
        if self.carrito:
            print('Productos en el carrito:')
            for producto in self.carrito:
                print(producto)
        else: 
            print("El carrito está vacío")
    
    def ver_puntos(self):
        if len(self.carrito) >= 1:
            print(f'Tienes {self.puntos + 1} puntos de canje acumulados')

    def ver_datos(self):
        if self.tarjeta:
            print('Informacion de la tarjeta')
            for clave, valor in self.tarjeta.items():
                print(f'{clave} : {valor}')
        else:
            print('No se ha vinculado ninguna tarjeta')
    
    def imprimir_datos(self):
        print('Datos personales')
        for clave, valor in self.datos_personales.items():
            print(f'{clave} : {valor}')

def main():
    print("Bienvenido a la plataforma de ventas Fandroid")
    nombre = input('Nombre: ')
    correo = input('Ingresa un correo: ')
    usuario = casoFandroid(nombre, correo)

    while True:
        print('\nAntes de proceder con una compra, es necesario que vincules los datos de tu tarjeta de crédito.')
        print(' 1. Vincular Tarjeta')
        print(' 2. Modificar Datos')
        print(' 3. Comprar Producto')
        print(' 4. Ver historial de compras')
        print(' 5. Ver puntos acumulados por compra')
        print(' 6. Consultar datos de la tarjeta de credito')
        print(' 7. Consultar datos personales')
        print(' 8. Salir')
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            usuario.vincular_tarjeta()
        elif opcion == "2":
            usuario.modificar_datos()
        elif opcion == "3":
            producto = input("Nombre del producto: ")
            usuario.comprar_producto(producto)
        elif opcion == "4":
            usuario.ver_compras()
        elif opcion == "5":
            usuario.ver_puntos()
        elif opcion == "6":
            usuario.ver_datos()
        elif opcion == "7":
            usuario.imprimir_datos()
        elif opcion == "8":
            break
        else: 
            print("Opción no válida. Inténtelo de nuevo.")

main()
