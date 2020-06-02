from django.urls import path
from Faker_App import views

urlpatterns = [
   
    path('data/',views.create_view),
    path('fetch/',views.fetch_view)
]

