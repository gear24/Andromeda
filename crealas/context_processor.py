# context_processors.py en la aplicación 'Calas'

from decimal import Decimal

def total_carrito(request):
    totalc = Decimal('0')
    articulosc = 0

    # Asegúrate de usar la sesión específica de la aplicación 'Calas'
    if "Calas" in request.session.keys() and "carrito" in request.session["Calas"]:
        for key, value in request.session["Calas"]["carrito"].items():
            totalc += Decimal(value["acumulado"])
            articulosc += value.get("cantidad", 0)



    return {"totalc": totalc, "articulosc": articulosc}
