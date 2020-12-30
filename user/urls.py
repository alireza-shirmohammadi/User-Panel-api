from django.urls import path
from . import views

urlpatterns = [
    path('image-api',views.ImageApi.as_view()),

]