
from django.contrib import admin
from django.urls import path
from myfolio_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('starter/', views.starter, name='starter'),
]
