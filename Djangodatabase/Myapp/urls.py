
from django.urls import path
from Myapp import views

urlpatterns = [
    path("add/", views.add_person),
    path("all/", views.all_person),
    path("delete/", views.delete_person),
    path("update/", views.update_person),

]