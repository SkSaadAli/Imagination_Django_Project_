
from django.urls import path
from . import views
urlpatterns = [

    path('', views.home, name='home'),
    path('create-poem', views.createForm, name='create-poem'),
    path('poem/<str:slug>', views.poem, name="poem"),
    path('update-poem/<str:slug>', views.updatePoem, name='update-poem'),
    path('delete-poem/<str:slug>', views.deletePoem, name='delete-poem'),
    path('delete-comment/<str:slug>', views.deleteMessage, name='delete-comment'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('search', views.search, name='search'),
    path('author', views.author, name='author'),
    path('category', views.categorys, name='category'),
    path('registration', views.registration, name='registration'),
    path('about', views.about_us, name='about'),



]
