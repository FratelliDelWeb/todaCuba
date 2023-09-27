from django.shortcuts import render, HttpResponse
from .models import QuienesSomos,SabiasQ
from .models import Excursion1, Excursion2, Excursion3, Excursion4, Excursion5, Excursion6, Casas

from django.shortcuts import get_object_or_404, render, redirect





# Create your views here.

def home(request):
    return render(request,"TodaCubaApp/home.html")

def excursion1(request):
# Recuperamos el objeto QuienesSomos que queremos mostrar
    excursion1 = Excursion1.objects.first() # Por ejemplo, recuperamos el primer objeto
    
    # Creamos un diccionario con el objeto y lo pasamos al contexto
    context = {
        'excursion1': excursion1
    }
    
    # Retornamos la plantilla HTML con el contexto
    return render(request, 'TodaCubaApp/excursion1.html', context)

def excursion2(request):
# Recuperamos el objeto QuienesSomos que queremos mostrar
    excursion2 = Excursion2.objects.first() # Por ejemplo, recuperamos el primer objeto
    
    # Creamos un diccionario con el objeto y lo pasamos al contexto
    context = {
        'excursion2': excursion2
    }
    
    # Retornamos la plantilla HTML con el contexto
    return render(request, 'TodaCubaApp/excursion2.html', context)

def excursion3(request):
# Recuperamos el objeto QuienesSomos que queremos mostrar
    excursion3 = Excursion3.objects.first() # Por ejemplo, recuperamos el primer objeto
    
    # Creamos un diccionario con el objeto y lo pasamos al contexto
    context = {
        'excursion3': excursion3
    }
    
    # Retornamos la plantilla HTML con el contexto
    return render(request, 'TodaCubaApp/excursion3.html', context)

def excursion4(request):
# Recuperamos el objeto QuienesSomos que queremos mostrar
    excursion4 = Excursion4.objects.first() # Por ejemplo, recuperamos el primer objeto
    
    # Creamos un diccionario con el objeto y lo pasamos al contexto
    context = {
        'excursion4': excursion4
    }
    
    # Retornamos la plantilla HTML con el contexto
    return render(request, 'TodaCubaApp/excursion4.html', context)

def excursion5(request):
# Recuperamos el objeto QuienesSomos que queremos mostrar
    excursion5 = Excursion5.objects.first() # Por ejemplo, recuperamos el primer objeto
    
    # Creamos un diccionario con el objeto y lo pasamos al contexto
    context = {
        'excursion5': excursion5
    }
    
    # Retornamos la plantilla HTML con el contexto
    return render(request, 'TodaCubaApp/excursion5.html', context)

def excursion6(request):
# Recuperamos el objeto QuienesSomos que queremos mostrar
    excursion6 = Excursion6.objects.first() # Por ejemplo, recuperamos el primer objeto
    
    # Creamos un diccionario con el objeto y lo pasamos al contexto
    context = {
        'excursion6': excursion6
    }
    
    # Retornamos la plantilla HTML con el contexto
    return render(request, 'TodaCubaApp/excursion6.html', context)



def quienes_somos(request):
    # Recuperamos el objeto QuienesSomos que queremos mostrar
    quienes_somos = QuienesSomos.objects.first() # Por ejemplo, recuperamos el primer objeto
    
    # Creamos un diccionario con el objeto y lo pasamos al contexto
    context = {
        'quienes_somos': quienes_somos
    }
    
    # Retornamos la plantilla HTML con el contexto
    return render(request, 'TodaCubaApp/quienesSomos.html', context)

def personalizatutour(request):
    return render(request,"TodaCubaApp/personalizatutour.html")

def sabiasQ(request):
    sabiasQ_list = SabiasQ.objects.all()
    return render(request, 'TodaCubaApp/SabiasQ.html', {'sabiasQ_list': sabiasQ_list})

def enviosCuba(request):
    return render(request,"TodaCubaApp/enviosCuba.html")




def casas_en_habana(request):
    casas = Casas.objects.filter(provincias__provincia='Habana')
    provincia = 'Habana'
    return render(request, 'casas_por_provincia.html', {'casas': casas, 'provincia': provincia})

def casas_en_pinar(request):
    casas = Casas.objects.filter(provincias__provincia='Pinar del Rio')
    provincia = 'Pinar del Rio'
    return render(request, 'casas_por_provincia.html', {'casas': casas, 'provincia': provincia})



def casas_en_cienfuegos(request):
    casas = Casas.objects.filter(provincias__provincia='Cienfuegos')
    provincia = 'Cienfuegos'
    return render(request, 'casas_por_provincia.html', {'casas': casas, 'provincia': provincia})


def casas_en_matanzas(request):
    casas = Casas.objects.filter(provincias__provincia='Matanzas')
    provincia = 'Matanzas'
    return render(request, 'casas_por_provincia.html', {'casas': casas, 'provincia': provincia})