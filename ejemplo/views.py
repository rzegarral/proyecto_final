from django.shortcuts import render
from ejemplo.models import Familiar
from ejemplo.forms import Buscar, FamiliarForm    # <--- NUEVO IMPORT
from django.views import View # <-- NUEVO IMPORT 
from ejemplo.models import Amigos

def index(request):
    return render(request, "ejemplo/saludar.html")

def saludar_a(request, nombre):
    return render(request, 
    'ejemplo/saludar_a.html',
    {"nombre": nombre}
    )

def sumar(request, a, b):
    return render (request, 
    'ejemplo/sumar.html', 
    {"a":a, 
     "b":b,
     "Resultado":a + b
    }
    )

def buscar(request):
    query = request.GET['q']
    return render(request,'ejemplo/buscar.html', {"query": query})

#----------------FAMILIARES
def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})

class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})
###-------------------- Clase AltaFamiliar heredada de VIEW
class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

#----------------AMIGOS
def buscar_amigos(request):
    query = request.GET['q']
    return render(request,'ejemplo/buscar_amigos.html', {"query": query})

def monstrar_amigos(request):
  lista_amigos = Amigos.objects.all()
  return render(request, "ejemplo/amigos.html", {"lista_amigos": lista_amigos})

class BuscarAmigos(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar_amigos.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_amigos = Amigos.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_amigos':lista_amigos})
        return render(request, self.template_name, {"form": form})
