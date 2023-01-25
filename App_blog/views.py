from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, CreateView , UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.


def inicio(request):
    return render(request, "home.html")

def sobremi(request):
    return render(request, "about.html")

"""def crearusuario(request): 
    if request.method == "POST":
        username= request.POST["username"]
        contraseña= request.POST["contraseña"]
        nombre= request.POST["nombre"]
        apellido= request.POST["apellido"]
        email= request.POST["email"]
        nacimiento= request.POST["nacimiento"]
        telefono= request.POST["telefono"]                
        user = usuarioform( username=username , contraseña=contraseña , nombre= nombre , apellido= apellido , email=email , nacimiento=nacimiento, telefono=telefono)
        user.save()
        return render (request, "home.html" )
    else:
        return render ( request, "crear_usuario.html", {"form": usuarioform})"""


"""class crearusuario(CreateView):
    model = usuario
    template_name= "usuario_form.html"
    success_urls = reverse_lazy("home")
    fields= ['username','contraseña','nombre','apellido','email','nacimiento','telefono']"""

def registro(request):

    if request.method == "POST":
        form=  usuarioform(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password1=form.cleaned_data.get("password1")
            password2=form.cleaned_data.get("password2")
            first_name=form.cleaned_data.get("first_name")
            last_name=form.cleaned_data.get("last_name")
            email=form.cleaned_data.get("email")
            telefono=form.cleaned_data.get("telefono")
            form.save()
            return render (request, "home.html", {"mensaje":"Usuario registrado."})
        else:
            return render(request, "crear_usuario.html", {"form": form, "mensaje":"Error"})
    else:
        form= usuarioform()
        return render(request,"crear_usuario.html", {"form":form})


@login_required

def profile(request):

    lista= avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        useravatar=lista[0].imagen.url
    else:
        useravatar="/media/avatar/defecto.png"

    return render(request, "profile.html", {"useravatar": useravatar})


def usuario_login(request):
    
    if request.method == 'POST':
     
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  

            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contraseña)

            if user is not None:
                login(request, user)
                return render(request, "home.html")
            else:
                return render(request, "login.html", {"mensaje":"Datos incorrectos, intente nuevamente."})
        else:
            return render(request, "login.html", {"mensaje":"Datos incorrectos, intente nuevamente." , "form": form})

    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


def leerusuarios(request):
    usuarios = User.objects.all()
    return render(request, "leerusuarios.html", {"usuarios" : usuarios})


@login_required
def edit_user(request):
    usuario=request.user

    if request.method=="POST":
        form=formeditar_usuario(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.telefono=info["telefono"]
            usuario.nacimiento=info["nacimiento"]
            usuario.save()
            return render(request, "profile.html", {"mensaje2":f"Tus datos se han editado correctamente!"})
        else:
            return render(request,"editarusuario.html", {"form": form , "nombreusuario": usuario.username})

    else:
        form=formeditar_usuario(instance=usuario)
        return render (request, "editarusuario.html", {"form": form})

@login_required
def crearposteo(request): 
    if request.method == "POST":
        titulo= request.POST["titulo"]
        reseña= request.POST["reseña"]
        contenido= request.POST["contenido"]
        imagen= request.FILES["imagen"]
        fecha= request.POST["fecha"]
        autor= User.objects.get(username=request.user)
        posteo = post( titulo=titulo , reseña=reseña, contenido= contenido , imagen=imagen, fecha= fecha, autor=autor)
        posteo.save()
        return render (request, "profile.html" , {"mensaje4": "Tu posteo fue publicado con éxito! Muchas gracias por sumar tu aporte al blog!"})
    else:
        return render ( request, "crearpost.html")





def leerposteo(request):
    posteos= post.objects.all()
    page= request.GET.get("page",1)

    try:
        paginator = Paginator(posteos, 2)
        posteos = paginator.page(page)
    except:
        return render(request, "home.html")

    data= {"entity": posteos , 
    "paginator": paginator}

    return render(request, "leerposteo.html", data)



"""def editarpost(request, id):
    posteo= post.objects.get(id=id)
    if request.method=="POST":
        form= crearpost(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            posteo.titulo=info["titulo"]
            posteo.reseña=info["reseña"]
            posteo.contenido=info["contenido"]
            posteo.imagen=info["imagen"]
            posteo.fecha=info["fecha"]
            posteo.save()
            return render(request, "profile.html", {"mensaje": "El posteo fue editado correctamente."})
        else:
            return render(request,"editarpost.html", {"form": crearpost , "form": form})

    else:
        formulario= crearpost(initial={"titulo": posteo.titulo, "reseña": posteo.reseña, "contenido": posteo.contenido , "imagen": posteo.imagen , "fecha": posteo.fecha })
        return render(request,"editarpost.html", {"form": crearpost , "posteo": posteo}) """

def editarpost(request, id):
        if request.method=="POST":
            postear=post.objects.get(id=id)
            form=crearpost(request.POST)
            if form.is_valid():
                info=form.cleaned_data
                titulo=info["titulo"]
                reseña=info["reseña"]
                contenido=info["contenido"]
                fecha=info["fecha"]
                postear.titulo=titulo
                postear.reseña=reseña
                postear.contenido=contenido
                postear.fecha=fecha
                postear.save()
                return render(request, "home.html", { "mensaje": "El posteo se edito correctamente!"})
        else:
            postear=post.objects.get(id=id)
            form= crearpost(initial={"titulo": postear.titulo , "reseña": postear.reseña , "contenido": postear.contenido , "fecha": postear.fecha}) 
            return render(request, "editarpost.html", {"form":form , "postear": postear})



def eliminarpost(request, id):
    posteo= post.objects.get(id=id)
    posteo.delete()
    return render(request, "profile.html", {"mensaje3": "El posteo fue eliminado correctamente."})


def leerpost_detalle(request, id):
    posteo= post.objects.filter(id=id)
    return render(request, "leerpostid.html", {"posteo": posteo})


def agregaravatar(request):
    if request.method=="POST":
        form= avatarform(request.POST, request.FILES)
        if form.is_valid():
            avatarid=avatar(user=request.user , imagen=request.FILES["imagen"])
            avatarviejo=avatar.objects.filter(user=request.user)
            if len(avatarviejo)>0:
                avatarviejo[0].delete()
            avatarid.save()
            return render(request, "home.html" , {"mensaje": "Avatar agregado correctamente."})
        else:
            return render(request, "agregaravatar.html", {"form": form, "usuario":request.user, "mensaje":"Error al agregar el avatar."})
    else:
        form=avatarform()
        return render(request, "agregaravatar.html", {"form":form, "usuario":request.user})