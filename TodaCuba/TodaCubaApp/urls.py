from django.urls import path
from TodaCubaApp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home,name="home"),  
    path('excursion1', views.excursion1,name="excursion1"),
    path(' excursion1/', views. excursion1, name=' excursion1'),
    path('excursion2', views.excursion2,name="excursion2"),  
    path(' excursion2/', views. excursion2, name=' excursion2'),
    path('excursion3', views.excursion3,name="excursion3"),  
    path(' excursion3/', views. excursion3, name=' excursion3'),
    path('excursion4', views.excursion4,name="excursion4"),  
    path(' excursion4/', views. excursion4, name=' excursion4'),
    path('excursion5', views.excursion5,name="excursion5"),  
    path(' excursion5/', views. excursion5, name=' excursion5'),
    path('excursion6', views.excursion6,name="excursion6"),  
    path(' excursion6/', views. excursion6, name=' excursion6'),
    path(' quienes_somos/', views. quienes_somos,name="quienesSomos"),  
    path(' quienes_somos/', views. quienes_somos, name=' quienes_somos'),

    path('personalizatutour', views.personalizatutour,name="personalizatutour"),  
    path('SabiasQ', views.sabiasQ,name="SabiasQ"),  
    path(' sabiasQ/', views.sabiasQ, name=' sabiasQ'),

    path('enviosCuba', views.enviosCuba,name="enviosCuba"),  

    path('habana/', views.casas_en_habana, name='casas_en_habana'),
    path('Pinar del Rio/', views.casas_en_pinar, name='casas_en_pinar'),
    path('Cienfuegos/', views.casas_en_cienfuegos, name='casas_en_cienfuegos'),
    path('Matanzas/', views.casas_en_matanzas, name='casas_en_matanzas'),




  ] 


