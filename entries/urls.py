from django.urls import path
from . import views
import entries

urlpatterns = [
    path('',views.index,name="index"),
    path('entry/<int:pk_test>/',views.content,name="content"),
    path('newentry',views.entry,name="entry")

]