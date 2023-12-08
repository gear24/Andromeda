from decimal import Decimal

class Carrito:
    def __init__(self, request, app_name):
        self.request = request
        self.app_name = app_name
        self.session = request.session

        # Usa el nombre de la aplicación para acceder a la sesión específica
        carrito = self.session.get(app_name, {}).get("carrito", {})
        if not carrito:
            self.session[app_name] = {"carrito": {}}
            self.carrito = self.session[app_name]["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "acumulado": str(producto.precio),  # Almacena el precio como cadena
                "cantidad": 1,
                "precio": str(producto.precio),  # Almacena el precio como cadena
            }
        else:
            self.carrito[id]["cantidad"] += 1
            # Sumar los precios como Decimal y luego convertir a string para almacenarlos
            self.carrito[id]["acumulado"] = str(Decimal(self.carrito[id]["acumulado"]) + Decimal(str(producto.precio)))
            #self.carrito[id]["precio"] = str(Decimal(self.carrito[id]["precio"]) + Decimal(str(producto.precio)))

        self.guardar_carrito()

    def guardar_carrito(self):
        # Usa el nombre de la aplicación para acceder a la sesión específica
        self.session[self.app_name]["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            # self.carrito[id]["acumulado"] -= Decimal(str(producto.precio))
            #print(type(Decimal(self.carrito[id]["acumulado"])))
            # self.carrito[id]["precio"] -= Decimal(str(producto.precio))
            #print(type(self.carrito[id]["precio"]))
            if self.carrito[id]["cantidad"] <= 0:
                self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        # Usa el nombre de la aplicación para acceder a la sesión específica
        self.session[self.app_name]["carrito"] = {}
        self.session.modified = True
