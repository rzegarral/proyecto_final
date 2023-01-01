from django.shortcuts import render, get_object_or_404
from ejemplo.models import Familiar, Amigos, Carros
from ejemplo.forms import Buscar, FamiliarForm, AmigosForm, CarrosForm
from django.views import View

def index(request):
    return render(request, "ejemplo/saludar.html")

def saludar_a(request, nombre):
    return render(request, 
    'ejemplo/saludar_a.html',
    {"nombre": nombre}  )

def sumar(request, a, b):
    return render (request, 
    'ejemplo/sumar.html', 
    {"a":a, 
     "b":b,
     "Resultado":a + b
    } )

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


class ActualizarFamiliar(View):
  form_class = FamiliarForm
  template_name = 'ejemplo/actualizar_familiar.html'
  initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  #   def get(self, request, pk): 
  def get(self, request, pk): 
    familiar = get_object_or_404(Familiar, pk=pk)
    form = self.form_class(instance=familiar)
    return render(request, self.template_name, {'form':form,'familiar': familiar})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk):
    familiar = get_object_or_404(Familiar, pk=pk)
    form = self.form_class(request.POST ,instance=familiar)
    if form.is_valid():
      form.save()
      msg_exito = f"se actualizó con éxito el familiar {form.cleaned_data.get('nombre')}"
      form = self.form_class(initial=self.initial)
      return render(request, self.template_name, {'form':form, 
                              'familiar': familiar,
                              'msg_exito': msg_exito})
    return render(request, self.template_name, {"form": form})

class BorrarFamiliar(View):
  template_name = 'ejemplo/familiares.html'

  def get(self, request, pk): 
    familiar = get_object_or_404(Familiar, pk=pk)
    familiar.delete()
    familiares = Familiar.objects.all()
    return render(request, self.template_name, {'lista_familiares':familiares})

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

class AltaAmigos(View):
  form_class = AmigosForm
  template_name = 'ejemplo/alta_amigos.html'
  initial = {"Id":"","nombre":"", "direccion":"", "edad":"", "pais":""}

  def get(self, request):
    form = self.form_class(initial=self.initial)
    return render(request, self.template_name, {'form':form})

  def post(self, request):
    form = self.form_class(request.POST)
    if form.is_valid():
      form.save()
      msg_exito = f"se cargo con éxito el amigo {form.cleaned_data.get('nombre')}"
      form = self.form_class(initial=self.initial)
      return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
    return render(request, self.template_name, {"form": form})

class Amigosactualizar(View):
  form_class = AmigosForm
  template_name = 'ejemplo/amigos_actualizar.html'
  initial = {"nombre":"", "direccion":"", "pais":"", "edad":""}

  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk):
    amigos = get_object_or_404(Amigos, pk=pk)
    form = self.form_class(instance=amigos)
    return render(request, self.template_name, {'form':form,'amigos': amigos})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk): 
    amigos = get_object_or_404(Amigos, pk=pk)
    form = self.form_class(request.POST ,instance=amigos)
    if form.is_valid():
      form.save()
      msg_exito = f"se actualizó con éxito el amigo {form.cleaned_data.get('nombre')}"
      form = self.form_class(initial=self.initial)
      return render(request, self.template_name, {'form':form, 
                                'amigos': amigos,
                                'msg_exito': msg_exito})
    return render(request, self.template_name, {"form": form})

class BorrarAmigo(View):
  template_name = 'ejemplo/amigos.html'
   
  def get(self, request, pk):
    amigos = get_object_or_404(Amigos, pk=pk)
    amigos.delete()
    amigos = Amigos.objects.all()
    return render(request, self.template_name, {'lista_amigos':amigos})

#----------------AUTOS

def buscar_autos(request):
  query = request.GET['q']
  return render(request,'ejemplo/buscar_autos.html', {"query": query})

def monstrar_autos(request):
  lista_autos = Carros.objects.all()
  return render(request, "ejemplo/autos.html", {"lista_autos": lista_autos})

class BuscarAutos(View):
  form_class = Buscar
  template_name = 'ejemplo/buscar_auto.html'
  initial = {"marca":""}

  def get(self, request):
    form = self.form_class(initial=self.initial)
    return render(request, self.template_name, {'form':form})
  def post(self, request):
    form = self.form_class(request.POST)
    if form.is_valid():
      marca = form.cleaned_data.get("marca")
      lista_autos = Carros.objects.filter(marca__icontains=marca).all() 
      form = self.form_class(initial=self.initial)
      return render(request, self.template_name, {'form':form, 
                                'lista_autos':lista_autos})
    return render(request, self.template_name, {"form": form})

class AltaAutos(View):
  form_class = CarrosForm
  template_name = 'ejemplo/alta_autos.html'
  initial = {"Id":"","marca":"", "origen":"", "ano":"", "valor":""}

  def get(self, request):
    form = self.form_class(initial=self.initial)
    return render(request, self.template_name, {'form':form})

  def post(self, request):
    form = self.form_class(request.POST)
    if form.is_valid():
      form.save()
      msg_exito = f"se cargo con éxito el auto {form.cleaned_data.get('marca')}"
      form = self.form_class(initial=self.initial)
      return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
    return render(request, self.template_name, {"form": form})

class Autosactualizar(View):
  form_class = CarrosForm
  template_name = 'ejemplo/actualizar_autos.html'
  initial = {"id":"","marca":"", "origen":"", "ano":"", "valor":""}
  
  # preutstar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk):
    autos = get_object_or_404(Carros, pk=pk)
    form = self.form_class(instance=autos)
    return render(request, self.template_name, {'form':form,'autos': autos})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk): 
    autos = get_object_or_404(Carros, pk=pk)
    form = self.form_class(request.POST ,instance=autos)
    if form.is_valid():
      form.save()
      msg_exito = f"se actualizó con éxito el auto {form.cleaned_data.get('marca')}"
      form = self.form_class(initial=self.initial)
      return render(request, self.template_name, {'form':form, 
                                'autos': autos,
                                'msg_exito': msg_exito})
    return render(request, self.template_name, {"form": form})

class BorrarAuto(View):
  template_name = 'ejemplo/autos.html'
   
  def get(self, request, pk):
    autos = get_object_or_404(Carros, pk=pk)
    autos.delete()
    autos = Carros.objects.all()
    return render(request, self.template_name, {'lista_autos':autos})
