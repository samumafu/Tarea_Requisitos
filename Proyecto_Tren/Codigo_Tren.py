import time

# Función para recopilar información del usuario
def solicitar_informacion():
    identificacion = input("Ingrese su identificación: ")
    tarjeta = input("Ingrese el número de tarjeta de crédito: ")
    return identificacion, tarjeta

# Función para mostrar el menú de destinos y seleccionar uno
def seleccionar_destino():
    print("Menú de destinos:")
    print("1. Ciudad A")
    print("2. Ciudad B")
    print("3. Ciudad C")
    opcion = input("Seleccione su destino (1/2/3): ")
    destinos = ["Ciudad A", "Ciudad B", "Ciudad C"]
    destino_elegido = destinos[int(opcion) - 1]
    return destino_elegido

# Función para generar el boleto y realizar el cobro
def generar_boleto(identificacion, tarjeta, destino):
    print("Generando boleto...")
    time.sleep(1.5)  
    print("Boleto generado para:", destino)
    print("Cobro automático realizado a la tarjeta:", tarjeta)

# Función para validar la tarjeta y la identificación
def validar_tarjeta_identificacion(identificacion, tarjeta):
    return True

# Función principal del programa
def main():
    print("Bienvenido al sistema de compra de boletos de tren")

    identificacion, tarjeta = solicitar_informacion()

    if validar_tarjeta_identificacion(identificacion, tarjeta):
        destino = seleccionar_destino()
        generar_boleto(identificacion, tarjeta, destino)
        print("¡Gracias por su compra!")
    else:
        print("Tarjeta o identificación inválidas. Compra cancelada.")
main()