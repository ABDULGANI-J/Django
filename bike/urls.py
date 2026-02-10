from django.urls import path
from . import views


app_name='bike'

urlpatterns = [
    path("",views.index,name="index"),
    path("post/<str:slug>",views.detail,name="detail"),
    path("contact",views.contact_view,name="contact")
]