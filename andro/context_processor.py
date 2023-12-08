# context_processors.py en la aplicación 'andro'

from decimal import Decimal

def total_carrito(request):
    totala = Decimal('0')
    articulosa = 0

    # Asegúrate de usar la sesión específica de la aplicación 'andro'
    if "andro" in request.session.keys() and "carrito" in request.session["andro"]:
        for key, value in request.session["andro"]["carrito"].items():
            totala += Decimal(value["acumulado"])
            articulosa += value.get("cantidad", 0)

    return {"totala": totala, "articulosa": articulosa}
