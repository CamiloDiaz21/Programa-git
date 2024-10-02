class Producto:
    def __init__(self, nombre, cantidad, precio_unitario):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.total = cantidad * precio_unitario

    def __str__(self):
        return f"{self.nombre} - Cantidad: {self.cantidad} - Precio Unitario: ${self.precio_unitario:.2f} - Total: ${self.total:.2f}"

class Factura:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = sum(producto.total for producto in self.productos)
        return total

    def mostrar_factura(self):
        print(f"\nFactura para: {self.cliente}")
        print("=" * 40)
        for producto in self.productos:
            print(producto)
        print("=" * 40)
        print(f"Total a pagar: ${self.calcular_total():.2f}\n")


def main():
    cliente = input("Ingrese el nombre del cliente: ")
    factura = Factura(cliente)

    while True:
        nombre_producto = input("\nIngrese el nombre del producto (o 'salir' para finalizar): ")
        if nombre_producto.lower() == 'salir':
            break
        cantidad = int(input(f"Ingrese la cantidad de {nombre_producto}: "))
        precio_unitario = float(input(f"Ingrese el precio unitario de {nombre_producto}: "))

        producto = Producto(nombre_producto, cantidad, precio_unitario)
        factura.agregar_producto(producto)

    factura.mostrar_factura()


if __name__ == "__main__":
    main()
