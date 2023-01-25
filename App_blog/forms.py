from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class usuarioform(UserCreationForm):
    username=forms.CharField(max_length=20)
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label="Nombre" ,max_length=50)
    last_name=forms.CharField(label="Apellido", max_length=50)
    email=forms.EmailField()
    nacimiento=forms.DateField(label="Fecha de nacimiento")
    telefono=forms.IntegerField()

    class Meta:
        model=User
        fields= ['username','password1','password2','first_name','last_name','email','telefono','nacimiento']
        help_text= {k: "" for k in fields}



class formeditar_usuario(UserCreationForm):

    first_name= forms.CharField(label="Nombre", max_length=50)
    last_name= forms.CharField(label="Apellido", max_length=50)
    password1 = forms.CharField(label= "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label= "Confirmar contraseña", widget=forms.PasswordInput)
    email= forms.EmailField(label= "Email")
    telefono=forms.IntegerField(label= "Telefono")
    nacimiento= forms.DateField(label="Fecha de nacimiento")

    class Meta:
        model= User
        fields= ["email","password1","password2","first_name","last_name", "telefono", "nacimiento"]
        help_texts= {k: "" for k in fields}




"""class post(forms.Form):
    titulo=forms.CharField(max_length=200)
    reseña=forms.CharField(max_length=200)
    contenido=forms.Textarea(max_length=5000)
    imagen=forms.ImageField(upload_to="imgpost", null=True, blank=True)
    fecha= forms.DateField()

    def __str__(self):
        return f"Titulo: {self.titulo} - Reseña: {self.reseña} - Fecha: {self.fecha}"""



class crearpost(forms.Form):
    titulo=forms.CharField(max_length=200)
    reseña=forms.CharField(max_length=200)
    contenido=forms.CharField(max_length=5000)
    fecha= forms.DateField()

class avatarform(forms.Form):
    imagen=forms.ImageField(label="Imagen")