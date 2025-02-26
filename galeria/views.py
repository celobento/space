from django.shortcuts import render

dados = {
    1:  {"nome":"Nebulosa de Carina", "legenda":"webtelescope.oirb/NASA/JamesWebb"},
    2:  {"nome":"Galaxia NGC 1079", "legenda":"bnasa.org/NASA/HUbble"}
}

def index(request):
    return render(request, 'galeria/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')