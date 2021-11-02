from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.create, name="create"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('pickup_list/', views.pickup_list, name="pickup_list"),
    path('pickup_confirm/<int:customer.id>', views.pickup_confirm, name="pickup_confirm"),

]