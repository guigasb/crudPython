from django.urls import path
from cadastro.views import CreateView, ReadView, UpdateView, DeleteView

urlpatterns = [
    #path('', homeView, name='home'),
    path('create/', CreateView, name = 'create'),
    path('', ReadView, name = 'lista'),
    path('update/<int:id>/', UpdateView, name='update'),
    path('delete/<int:id>/', DeleteView, name='delete'),



]