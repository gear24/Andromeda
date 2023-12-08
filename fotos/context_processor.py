# context_processors.py en la aplicación 'fotos'

from decimal import Decimal

def total_carrito(request):
    totalf = Decimal('0')
    articulosf = 0

    # Asegúrate de usar la sesión específica de la aplicación 'fotos'
    if "fotos" in request.session.keys() and "carrito" in request.session["fotos"]:
        for key, value in request.session["fotos"]["carrito"].items():
            totalf += Decimal(value["acumulado"])
            articulosf += value.get("cantidad", 0)

    return {"totalf": totalf, "articulosf": articulosf}
