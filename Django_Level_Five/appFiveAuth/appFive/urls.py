from django.conf.urls import url
from appFive import views

#TEMPLATE URLs
app_name = 'appFive'
urlpatterns = [
    url(r"^register/$", views.register, name = "register")
]
