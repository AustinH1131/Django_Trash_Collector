from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.create, name="create"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('pickup_list/', views.pickup_list, name="pickup_list"),
    path('pickup_confirm/<int:customer_id>', views.pickup_confirm, name="pickup_confirm"),
    path('sunday/',views.sunday, name="sunday"),
    path('monday/',views.monday, name="monday"),
    path('tuesday/',views.tuesday, name="tuesday"),
    path('wednesday/',views.wednesday, name="wednesday"),
    path('thursday/',views.thursday, name="thursday"),
    path('friday/',views.friday, name="friday"),
    path('saturday/',views.saturday, name="saturday"),
]