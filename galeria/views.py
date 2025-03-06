from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

dados = {
    1:  {"nome":"Nebulosa de Carina", "legenda":"webtelescope.oirb/NASA/JamesWebb"},
    2:  {"nome":"Galaxia NGC 1079", "legenda":"bnasa.org/NASA/HUbble"}
}

def index(request):
    fotografias = Fotografia.objects.all()
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})