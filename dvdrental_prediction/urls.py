# dvdrental_prediction/urls.py  
from django.urls import path  
from . import views  
  
app_name = 'dvdrental_prediction'  
  
urlpatterns = [  
    path('', views.home, name='home'),  
    path('about/', views.about, name='about'),  
    path('predict-view/', views.customer_prediction_view, name='customer_prediction_view'),  
    path('predict-customer/', views.predict_customer, name='predict_customer'),  
]  