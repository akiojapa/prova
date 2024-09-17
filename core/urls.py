from django.urls import path

from . import views

app_name = 'core' 

urlpatterns = [
    path("", views.index, name="index"),
    path("computadores", views.computador, name="computador"),
    path('computadores/criar/', views.criar_computador, name='criar-computador'),
    path("perifericos", views.periferico, name="periferico"),
    path("perifericos/criar/", views.criar_periferico, name="criar-periferico"),
    path("computadores/editar/<int:id>", views.editar_computador, name="editar-computador"),
    path("computadores/deletar/<int:id>", views.deletar_computador, name="deletar-computador"),
    path("perifericos/editar/<int:id>", views.editar_periferico, name="editar-periferico"),
    path("perifericos/deletar/<int:id>", views.deletar_periferico, name="deletar-periferico"),
]