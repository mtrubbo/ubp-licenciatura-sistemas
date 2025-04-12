class Producto:
    def __init__(self, nombre: str, precio: float, impuesto: float, stock: int):
        if not nombre:
            raise ValueError("El nombre del producto no puede ser vacío")
        if not (0 <= impuesto <= 1):
            raise ValueError("El impuesto debe ser un número entre 0 y 1")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo")

        self.nombre = nombre
        self.precio_base = precio
        self.impuesto = impuesto
        self.precio_total = precio * (1 + impuesto)
        self.stock = stock

    def mostrar_datos(self):
        return f"{self.nombre} | Precio base: ${self.precio_base:.2f} | Impuesto: {self.impuesto * 100:.0f}% | Precio total: ${self.precio_total:.2f} | Stock: {self.stock}"


class ItemFactura:
    def __init__(self, producto: Producto, cantidad: int):
        self.producto = producto
        self.cantidad = cantidad
        self.total_item = producto.precio_total * cantidad


class Factura:
    def __init__(self):
        # {
            # "Leche": ItemFactura(Producto, cantidad)
            # ... otros elementos
        # }
        self.items = {}
        self.total = 0

    def agregar_item(self, producto: Producto, cantidad: int):
        if cantidad <= 0:
            raise ValueError("Cantidad inválida")

        if cantidad > producto.stock:
            print(f"El producto no tiene stock suficiente ({producto.stock})")
            return

        print(f"Se agrega item {producto.nombre} x{cantidad}")
        if producto.nombre in self.items:
            self.items[producto.nombre].cantidad += cantidad
        else:
            self.items[producto.nombre] = ItemFactura(producto, cantidad)

        self.total += producto.precio_total * cantidad
        producto.stock -= cantidad
        print(f"Stock restante de {producto.nombre}: {producto.stock}")

    def procesar_cupon_descuento(self, cupon: str):
        print(f"Cupon ingresado: {cupon}")
        if not cupon or cupon.strip() not in cupones_de_descuento:
            print("El cupon ingresado no es válido")
            return

        porcentaje = cupones_de_descuento[cupon.strip()]
        total_anterior = self.total
        self.total = descontar_porcentaje(self.total, porcentaje)
        print(f"Cupon de {porcentaje}% aplicado sobre el monto ${total_anterior:.2f}. Nuevo total: ${self.total:.2f}")

    def mostrar_detalle(self):
        print("\n=========== DETALLES DE FACTURA ===========\n")
        for nombre, itemFactura in self.items.items():
            print(f"{nombre} x{itemFactura.cantidad} ud. | Precio unit. ${itemFactura.producto.precio_total:.2f} | Total: ${itemFactura.total_item:.2f}")

        print("\n------------")
        print(f"Subtotal: ${self.total:.2f}")

        if self.total >= 10000:
            self.total = descontar_porcentaje(self.total, 10)
            print("\nSe aplica descuento por compra grande: 10%")
            print("===========")

        print(f"TOTAL: ${self.total:.2f}")
        print("===========")

# Funcion helper
def descontar_porcentaje(numero: float, porcentaje: int):
    return numero - (numero * (porcentaje / 100))


productos_validos = [
    Producto("Leche", 1500.50, 0.21, 5),
    Producto("Aceite", 2399.45, 0.10, 10),
    Producto("Fideos", 1300, 0.18, 20)
]

cupones_de_descuento = {
    "CUP10": 10,
    "CUP20": 20
}


def pedir_cantidad(producto: Producto):
    while True:
        try:
            cantidad = int(input("Seleccione la cantidad: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0")
                continue
            if cantidad > producto.stock:
                print(f"El producto no tiene stock suficiente ({producto.stock})")
                continue
            return cantidad
        except ValueError:
            print("Entrada inválida.")


def pedir_productos(factura: Factura):
    while True:
        print("\nSeleccione los productos a incluir en la factura")
        print("0. Finalizar carga")
        for i, p in enumerate(productos_validos, start=1):
            print(f"{i}. {p.mostrar_datos()}")

        try:
            opcion = int(input("Ingrese una opción: "))
        except ValueError:
            print("Entrada inválida.")
            continue

        if opcion == 0:
            break
        if opcion < 1 or opcion > len(productos_validos):
            print("No se seleccionó un producto válido.")
            continue

        cantidad = pedir_cantidad(productos_validos[opcion - 1])
        factura.agregar_item(productos_validos[opcion - 1], cantidad)


def ejecutar():
    factura = Factura()
    pedir_productos(factura)

    cupon = input(f"Si desea aplicar un cupón de descuento al total de ${factura.total:.2f}, escriba el código del mismo: ")
    factura.procesar_cupon_descuento(cupon)
    factura.mostrar_detalle()


ejecutar()