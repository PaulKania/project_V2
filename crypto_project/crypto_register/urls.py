from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.coin_form, name="coin_insert"), #got, post for insert
    path('<int:id>/', views.coin_form, name="coin_update"), #get, post req for update
    path('delete/<int:id>', views.coin_delete, name="coin_delete"), #get req to retrieve nd display entries.
    path('list/', views.coin_list, name="coin_list"), #get req to retrieve nd display entries.
]
