from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('entry/<int:pk_test>/',views.content,name="content")

]