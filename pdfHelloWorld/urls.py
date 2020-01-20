from django.urls import path
from pdfHelloWorld import views


urlpatterns = [
    path('index/', views.index),
    path('excel/',views.logout,name="downloadexcel"),
]