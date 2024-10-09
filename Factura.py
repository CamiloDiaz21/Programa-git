from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import pdfimages

# Clase para representar un Producto en la factura
class Producto:
    def __init__(self, nombre, cantidad, precio_unitario):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.total = cantidad * precio_unitario

# Clase para gestionar la Factura
class Factura:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        return sum(producto.total for producto in self.productos)

    # Función para generar el archivo PDF
    def generar_pdf(self, nombre_archivo):
        c = canvas.Canvas(nombre_archivo, pagesize=letter)
        ancho, alto = letter

        # Encabezado
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, alto - 50, f"Factura para: {self.cliente}")

        # Título de columnas
        c.setFont("Helvetica", 12)
        y_position = alto - 100
        c.drawString(50, y_position, "Producto")
        c.drawString(200, y_position, "Cantidad")
        c.drawString(300, y_position, "Precio Unitario")
        c.drawString(450, y_position, "Total")
        
        # Línea para separar el encabezado
        c.line(50, y_position - 10, 550, y_position - 10)

        # Lista de productos
        y_position -= 30
        for producto in self.productos:
            c.drawString(50, y_position, producto.nombre)
            c.drawString(200, y_position, str(producto.cantidad))
            c.drawString(300, y_position, f"${producto.precio_unitario:.2f}")
            c.drawString(450, y_position, f"${producto.total:.2f}")
            y_position -= 20

        # Total general de la factura
        y_position -= 20
        c.setFont("Helvetica-Bold", 12)
        c.drawString(400, y_position, "Total a pagar:")
        c.drawString(450, y_position, f"${self.calcular_total():.2f}")

        # Guardar y cerrar el archivo PDF
        c.save()
        print(f"Factura generada en el archivo: {nombre_archivo}")

# Función principal que ejecuta el flujo de creación de factura
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

    nombre_archivo = input("Ingrese el nombre del archivo PDF (ej. factura.pdf): ")
    factura.generar_pdf(nombre_archivo)

if __name__ == "__main__":
    main()
