from django.urls import path , include
from AgeGender import views
app_name = 'AgeGender'

urlpatterns = [
    path("home/" , views.AG_Home , name="home")


]