class Producto:
    def __init__(self, nombre, precio, impuesto):
        if not nombre:
            raise ValueError("El nombre del producto no puede ser vacío")
        if not (0 <= impuesto <= 1):
            raise ValueError("El impuesto debe ser un número entre 0 y 1")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")

        self.nombre = nombre
        self.precio_base = precio
        self.impuesto = impuesto
        self.precio_total = precio * (1 + impuesto)

    def mostrar_datos(self):
        return f"{self.nombre} | Precio base: ${self.precio_base:.2f} | Impuesto: {self.impuesto * 100:.0f}% | Precio total: ${self.precio_total:.2f}"

    def aplicar_descuento(self, porcentaje):
        self.precio_total -= self.precio_total * (porcentaje / 100)


productos_validos = [
    Producto("Leche", 1500, 0.21),
    Producto("Aceite", 2500, 0.10),
    Producto("Fideos", 1300, 0.18)
]


def ejecutar():
    precio_total_factura = 0

    while True:
        print("\nSeleccione los productos a incluir en la factura")
        print("0. Finalizar carga")
        for i, p in enumerate(productos_validos, start=1):
            print(f"{i}. {p.mostrar_datos()}")

        try:
            prod = int(input("Ingrese una opción: "))
        except ValueError:
            print("Entrada inválida.")
            continue

        if prod == 0:
            break
        if prod < 1 or prod > len(productos_validos):
            print("No se seleccionó un producto válido.")
            continue

        while True:
            try:
                cantidad = int(input("Seleccione la cantidad: "))
                if cantidad <= 0:
                    print("La cantidad debe ser mayor a 0")
                    continue
                break
            except ValueError:
                print("Entrada inválida.")

        precio_total_factura += productos_validos[prod - 1].precio_total * cantidad

    print(f"\nTotal: ${precio_total_factura:.2f}")


ejecutar()