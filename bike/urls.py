from django.urls import path
from . import views


app_name='bike'

urlpatterns = [
    path("",views.index,name="index"),
    path("post/<str:post_id>",views.detail,name="detail")
]