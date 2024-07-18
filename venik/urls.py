
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('nov/', views.nov, name='nov'),
    path('opt/', views.opt, name='opt'),
    path('venik/', views.venik, name='venik'),
]
