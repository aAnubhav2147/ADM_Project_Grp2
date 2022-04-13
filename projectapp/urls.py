from django.urls import path
#now import the views.py file into this code
from . import views
urlpatterns=[
  path('response/', views.responseform),
  path('thankyou/', views.responseform),
  path('',views.responseform)
]