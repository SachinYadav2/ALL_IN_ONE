import AgeGender.urls
from Dashboard import views
from django.urls import path,include
import AgeGender

urlpatterns = [
    path('' , views.home , name='home'),
    

]