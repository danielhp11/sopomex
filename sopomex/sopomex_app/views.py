from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    estados = setEstadoApi()
    return render(request,'index_cargar_datos.html',{'estado':estados})

##########METODOS DEL API######
def setEstadoApi():
    url = "http://localhost:5000/auth/estados"         
    r = requests.get(url)
    return r.json() 
