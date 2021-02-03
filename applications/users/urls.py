from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'login_app'
#user_app:user-logout

urlpatterns = [
    #path('', views.LoginUser.as_view(),name='login'),
    path('addusuario/', views.RegistroUserView.as_view(), name='addusuario'),
    path('login/', views.LoginUser.as_view(), name='user-login'),
    path('logout/', views.SalirView.as_view(), name='user-logout'),
    path('update/<pk>/', views.UserUpdate.as_view(), name='user-update'),

    path('listuser/', views.listaUsuarios, name='listuser'),
    path('borraruser/<pk>/', views.UserDeleteView.as_view(),name='borraruser'),

] 