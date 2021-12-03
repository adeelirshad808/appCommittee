from django.urls import path
from app.views.authentication.register import register
from app.views.authentication.user_login import user_login
from app.views.authentication.user_logout import user_logout
from app.views.create_committee import create_committee
from app.views.committe_creator_payment import committe_creator_payment
from app.views.index import index
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('',index,name='index'),
    path('register/', register, name='register'),
    path('user_login/', user_login, name='user_login'),
    path('user_logout/', user_logout , name='user_logout'),
    path('create_committee/', create_committee , name='create_committee'),
    path('committe_creator_payment/', committe_creator_payment , name='committe_creator_payment'),
   
]