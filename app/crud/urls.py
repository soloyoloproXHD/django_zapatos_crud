from django.urls import path
from . import views

urlpatterns = [
    path('', views.User.login_page , name='login'),
    path('register/', views.User.register_page , name='register'),
    path('tabla/', views.Shoes.tabla_page , name='tabla'),
    path('zapatos/', views.Shoes.zapato_page , name='zapatos'),
    
    #Rutas para base de datos
    path('register_user/', views.User.register_user , name='register_user'),
    path('validate_user/', views.User.validate_user , name='validate_user'),
    path('eliminar/<int:id>/', views.Shoes.eliminar_zapato , name='eliminar'),
    path('actualizar/<int:id>/', views.Shoes.actualizar_zapato , name='actualizar'),
    path('register_zapato/', views.Shoes.register_zapato , name='registrar'),
]