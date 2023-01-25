from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", inicio, name="home"),
    path("about/", sobremi, name= "sobremi"),
    path("registrar/", registro, name="usuarioform" ),
    path("perfil/", profile, name="profile" ),
    path("login/", usuario_login, name="login"),
    path("logout/", LogoutView.as_view(template_name="home.html"), name="logout"),
    path("leerusuarios/", leerusuarios, name="leerusuarios"),
    path("editaruser/", edit_user , name="editarperfil"),
    path("crearpost/", crearposteo , name="crearpost"),
    path("leerpost/", leerposteo , name="leerposteo"),
    path("editarpost/<id>", editarpost, name="editarpost"),
    path("eliminarpost/<id>", eliminarpost, name="eliminarpost"),
    path("leerpost/<id>", leerpost_detalle, name="leerpostid"),
    path("agregaravatar", agregaravatar, name="agregaravatar"),



]