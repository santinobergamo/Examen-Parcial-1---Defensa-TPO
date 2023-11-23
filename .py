import random

def generar_stock():  # Genera un stock aleatorio del 1 al 100
    return random.randint(1, 100)

def ingresar_datos_stock():
    codigos = []
    modelos = []
    cantidades = []

    while True:
        modelo = input("Ingrese el modelo (Presione ENTER para finalizar): ")
        if not modelo:
            break

        # Genera un código aleatorio entre 1000 y 9000 y asegura que no esté repetido
        codigo = random.randint(1000, 9000)
        while codigo in codigos:
            codigo = random.randint(1000, 9000)
        
        # Agrega los datos ingresados a las listas correspondientes
        codigos.append(codigo)
        modelos.append(modelo)
        cantidades.append(generar_stock())

    return codigos, modelos, cantidades

def ordenar_por_codigo(codigos, modelos, cantidades):
    # Algoritmo de ordenación de burbuja para ordenar por código de producto
    for i in range(len(codigos)):
        for j in range(i + 1, len(codigos)):
            if codigos[i] > codigos[j]:
                # Intercambia elementos si el código actual es mayor al siguiente
                codigos[i], codigos[j] = codigos[j], codigos[i]
                modelos[i], modelos[j] = modelos[j], modelos[i]
                cantidades[i], cantidades[j] = cantidades[j], cantidades[i]

def mostrar_stock(codigos, modelos, cantidades):
    print("\nListado completo por Código del producto, nombre y cantidad en stock actual:")
    # Itera sobre las listas para imprimir la información
    for i in range(len(codigos)):
        print(f"Código: {codigos[i]} - Modelo: {modelos[i]} - Stock: {cantidades[i]}")

def stock_bajo_minimo(codigos, modelos, cantidades):
    print("\nCódigos de productos por debajo del stock mínimo (5 unidades):")
    # Itera sobre las listas para identificar productos con stock bajo
    for i in range(len(codigos)):
        if cantidades[i] < 5:
            print(f"Código: {codigos[i]} - Modelo: {modelos[i]} - Stock: {cantidades[i]}")

def mostrar_mayor_cantidad_stock(codigos, modelos, cantidades):
    max_cantidad = max(cantidades)  # Encuentra la mayor cantidad en stock
    print("\nCódigos de productos con la mayor cantidad en stock:")
    # Itera sobre las listas para identificar productos con la mayor cantidad en stock
    for i in range(len(codigos)):
        if cantidades[i] == max_cantidad:
            print(f"Código: {codigos[i]} - Modelo: {modelos[i]} - Stock: {cantidades[i]}")

def main():
    codigos, modelos, cantidades = ingresar_datos_stock()  # Ingresa los datos
    ordenar_por_codigo(codigos, modelos, cantidades)  # Ordena por código
    mostrar_stock(codigos, modelos, cantidades)  # Muestra el listado completo
    stock_bajo_minimo(codigos, modelos, cantidades)  # Muestra stock bajo mínimo
    mostrar_mayor_cantidad_stock(codigos, modelos, cantidades)  # Muestra mayor cantidad en stock

main()  # Llama a la función principal
