from django.urls import path
from app import views

app_name='app'

urlpatterns = [
    path('page3/',views.page1,name='page3'),
]