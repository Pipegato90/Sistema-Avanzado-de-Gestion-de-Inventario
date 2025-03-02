import json

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar productos (clave: ID, valor: objeto Producto)

    def añadir_producto(self, producto):
        if producto.id in self.productos:
            print("Error: Ya existe un producto con este ID.")
        else:
            self.productos[producto.id] = producto
            print("Producto añadido correctamente.")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print("Producto eliminado correctamente.")
        else:
            print("Error: No se encontró un producto con este ID.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            producto = self.productos[id]
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            print("Producto actualizado correctamente.")
        else:
            print("Error: No se encontró un producto con este ID.")

    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_inventario(self, archivo):
        datos = {id: {"nombre": p.nombre, "cantidad": p.cantidad, "precio": p.precio}
                 for id, p in self.productos.items()}
        with open(archivo, 'w') as f:
            json.dump(datos, f)
        print("Inventario guardado correctamente.")

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'r') as f:
                datos = json.load(f)
            for id, info in datos.items():
                self.productos[int(id)] = Producto(int(id), info["nombre"], info["cantidad"], info["precio"])
            print("Inventario cargado correctamente.")
        except FileNotFoundError:
            print("No se encontró el archivo de inventario.")

def menu():
    inventario = Inventario()
    archivo = "inventario.json"

    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Cargar inventario")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = int(input("Ingrese el ID del producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id = int(input("Ingrese el ID del producto a eliminar: "))
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = int(input("Ingrese el ID del producto a actualizar: "))
            cantidad = input("Ingrese la nueva cantidad (deje en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (deje en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            inventario.guardar_inventario(archivo)

        elif opcion == "7":
            inventario.cargar_inventario(archivo)

        elif opcion == "8":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()