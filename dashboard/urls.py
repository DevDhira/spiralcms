from unicodedata import name
from django.urls import path
from dashboard import views
from blog.views import editpost

urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    path('create-profile/',views.createprofile,name='createprofile'),
    path('profile/edit-profile/',views.editprofile,name='editprofile'),
    path('profile/',views.profile,name='profile'),
    path('<str:urlslug>/edit',editpost,name='edit')
    ]