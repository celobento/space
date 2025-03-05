from django.shortcuts import render
from galeria.models import Fotografia

dados = {
    1:  {"nome":"Nebulosa de Carina", "legenda":"webtelescope.oirb/NASA/JamesWebb"},
    2:  {"nome":"Galaxia NGC 1079", "legenda":"bnasa.org/NASA/HUbble"}
}

def index(request):
    fotografias = Fotografia.objects.all()
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request):
    return render(request, 'galeria/imagem.html')