inventario = {
    "impresora brother": {"precio": 850.0, "stock": 5},
    "monitor lenovo 27": {"precio": 650.0, "stock": 10},
    "notebook advance": {"precio": 1600.0, "stock": 5},
    "notebook lenovo v15": {"precio": 3350.0, "stock": 3},
    "monitor teros": {"precio": 525.0, "stock": 8},
    "antivirus kaspersky": {"precio": 90.0, "stock": 20},
    "mouse teros": {"precio": 35.0, "stock": 30},
    "audifonos teros": {"precio": 99.9, "stock": 15},
    "tinta epson negra": {"precio": 40.0, "stock": 40},
    "ulefone armor": {"precio": 4350.0, "stock": 5},
    "oukitel wp33": {"precio": 1700.0, "stock": 7}
}

clientes = {} 

historial_ventas = []

def ordenar_inventario_burbuja(diccionario_inventario):
    productos = list(diccionario_inventario.keys())
    n = len(productos)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if productos[j] > productos[j + 1]:
                temp = productos[j]
                productos[j] = productos[j + 1]
                productos[j + 1] = temp
                
    return productos

def mostrar_inventario():
    print("\n" + "="*60)
    print("                    CATALOGO DE PRODUCTOS")
    print("="*60)
    
    productos_ordenados = ordenar_inventario_burbuja(inventario)
    
    for nombre in productos_ordenados:
        datos = inventario[nombre]
        if datos['stock'] <= 0:
            estado_stock = "PRODUCTO AGOTADO"
        else:
            estado_stock = f"Stock: {datos['stock']}"
            
        print(f"- {nombre.capitalize():<25} | Precio: S/ {datos['precio']:>8.2f} | {estado_stock}")
    print("="*60 + "\n")

def generar_informe():
    print("\n" + "="*40)
    print("            INFORME DE VENTAS")
    print("="*40)
    if not historial_ventas:
        print("Aun no hay ventas registradas en el sistema.")
        return
    
    total_ingresos = 0
    for venta in historial_ventas:
        total_ingresos += venta['total']
        
    print(f"Ingresos totales recaudados: S/ {total_ingresos:.2f}")
    print(f"Cantidad de transacciones: {len(historial_ventas)}")
    print(f"Clientes en base de datos: {len(clientes)}")
    print("-" * 40)
    print("Ultimos movimientos:")
    
    for venta in historial_ventas[-5:]:
        print(f"- {venta['cliente']} compro {venta['cantidad']} x {venta['producto'].capitalize()}")
    print("="*40 + "\n")

def realizar_compra():
    dni = input("Ingrese su DNI: ").strip()
    
    if not dni:
        print("Error: El DNI no puede estar vacio.")
        return

    if dni in clientes:
        cliente = clientes[dni]
        print(f"\nBienvenido de nuevo, {cliente['nombre']}.")
    else:
        print("\nDNI no registrado. Creando nuevo perfil...")
        nombre = input("Ingrese su nombre completo: ").strip()
        clientes[dni] = {"nombre": nombre, "compras": 1}
        cliente = clientes[dni]
        print(f"Perfil creado para {nombre}.")

    mostrar_inventario()
    
    producto_elegido = input("Ingrese el nombre exacto del producto: ").strip().lower()

    if producto_elegido not in inventario:
        print("Error: El producto ingresado no existe en el catalogo.")
        return

    if inventario[producto_elegido]["stock"] <= 0:
        print(f"Lo sentimos, el producto '{producto_elegido.capitalize()}' esta AGOTADO.")
        return

    try:
        cantidad = int(input(f"Cuantas unidades de {producto_elegido.capitalize()} desea llevar?: "))
    except ValueError:
        print("Error: Debe ingresar un numero entero.")
        return

    if cantidad <= 0:
        print("Error: La cantidad debe ser mayor a cero.")
        return
        
    if cantidad > inventario[producto_elegido]["stock"]:
        print(f"Error: Solo contamos con {inventario[producto_elegido]['stock']} unidades.")
        return

    precio_unitario = inventario[producto_elegido]["precio"]
    subtotal = precio_unitario * cantidad
    
    descuento_porcentaje = 0.0
    if subtotal >= 10000.0:
        descuento_porcentaje = 0.12
    elif subtotal >= 5000.0:
        descuento_porcentaje = 0.07

    descuento_aplicado = subtotal * descuento_porcentaje
    total_pagar = subtotal - descuento_aplicado

    print("\n" + "*"*40)
    print("            BOLETA DE VENTA")
    print("*"*40)
    print(f"Cliente: {cliente['nombre']}")
    print(f"Producto: {producto_elegido.capitalize()} x {cantidad}")
    print(f"Subtotal: S/ {subtotal:.2f}")
    if descuento_porcentaje > 0:
        print(f"Descuento ({descuento_porcentaje*100}%): -S/ {descuento_aplicado:.2f}")
    print(f"TOTAL A PAGAR: S/ {total_pagar:.2f}")
    print("*"*40)
    print("Pedido realizado con exito.")

    inventario[producto_elegido]["stock"] -= cantidad
    
    if inventario[producto_elegido]["stock"] == 0:
        print(f"AVISO: El producto '{producto_elegido.capitalize()}' se ha AGOTADO.")

    historial_ventas.append({
        "cliente": cliente['nombre'],
        "producto": producto_elegido,
        "cantidad": cantidad,
        "total": total_pagar
    })

def main():
    while True:
        try:
            print("\n" + "="*40)
            print("        SISTEMA DE GESTION DE TIENDA")
            print("="*40)
            print("1. Ver catalogo y Stock")
            print("2. Registrar una compra")
            print("3. Ver Informe de Gestion")
            print("4. Salir del sistema")
            print("="*40)
            
            opcion = input("Seleccione una opcion (1-4): ").strip()

            if opcion == "1":
                mostrar_inventario()
            elif opcion == "2":
                realizar_compra()
            elif opcion == "3":
                generar_informe()
            elif opcion == "4":
                print("Saliendo del sistema. Hasta luego!")
                break
            else:
                print("Opcion no valida. Por favor, marque del 1 al 4.")
                
        except (KeyboardInterrupt, EOFError):
            print("\nSistema cerrado por el usuario. Saliendo...")
            break

if __name__ == "__main__":
    main()