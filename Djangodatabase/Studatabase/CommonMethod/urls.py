
from django.urls import path
from CommonMethod import views

urlpatterns = [
    path("test_all/", views.test_all),
    path("test_filter/", views.test_filter),
    path("test_get/", views.test_get),
    path("test_first/", views.test_first),
    path("test_last/", views.test_last),
    path("test_exclude/", views.test_exclude),
    path("test_values/", views.test_values),
    path("test_values_list/", views.test_values_list),
    path("test_order_by/", views.test_order_by),
    path("test_person_obj_list/", views.test_person_obj_list),
    path("test_count/", views.test_count),
    path("test_exists/", views.test_exists),
    path("test1/", views.test1),
    path("test2/", views.test2),


]