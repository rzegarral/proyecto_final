from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from blog_ricardo.models import Post
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog_ricardo.forms import UsuarioForm
from blog_ricardo.models import Avatar, Post, Mensaje
from django.contrib.auth.admin import User   


def index(request):
    posts = Post.objects.order_by('-publicado_el').all()
    return render(request, "blog_ricardo/index.html",{"posts":posts})

class PostDetalle(DetailView):
    model = Post

class PostList(ListView):
    model = Post

class PostCrear(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("blog-ricardo-listar")
    fields = '__all__'

class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("blog-ricardo-listar")

class PostActualizar(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("blog-ricardo-listar")
    fields = '__all__'

class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('blog-ricardo-listar')

class UserLogin(LoginView):
    next_page = reverse_lazy('blog-ricardo-listar')

class UserLogout(LogoutView):
    next_page = reverse_lazy('blog-ricardo-listar')

class AvatarActualizar(UpdateView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy('blog-ricardo-listar')

class UserActualizar(UpdateView):
    model = User
    fields = ['first_name','last_name','email']
    success_url = reverse_lazy('blog-ricardo-listar')

class MensajeDetalle(LoginRequiredMixin, DetailView):
    model = Mensaje

class MensajeListar(LoginRequiredMixin, ListView):
    model = Mensaje

class MensajeCrear(CreateView):
    model = Mensaje
    fields = ['nombre','email','texto']
    success_url = reverse_lazy('blog-ricardo-mensajes-crear')

class MensajeBorrar(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy('blog-ricardo-mensajes-listar')

