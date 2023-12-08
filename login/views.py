from django.shortcuts import render, redirect
from .forms import registroForm, Login
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


# Create your views here.





@csrf_protect
def registro(request):
    data = {"form": registroForm()}
    if request.method == "POST":
        formulario = registroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(
                username=formulario.cleaned_data["username"],
                password=formulario.cleaned_data["password1"],
            )

            login(request, user)
            messages.success(request, "Usuario creado correctamente")
            return redirect(to="home:home")
            
        else:
            try:
                password = formulario.cleaned_data["password1"]
                validate_password(
                    password, user=formulario.instance
                )  # Pasar 'user' si aplica
            except ValidationError as error:
                # Acceder a los mensajes de error generados
                error_messages = list(error.messages)
                mensaje = ""

            for error in error_messages:
                mensaje += error

            
            messages_text = []

            messages.warning(request, mensaje)

        data["form"] = formulario

    return render(request, "registration/registro.html", data)
