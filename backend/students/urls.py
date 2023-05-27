from django.urls import path
from . import views
# from django.conf.urls import url

# app_name = 'students'

urlpatterns = [
    path('register/', views.StudentRegistrationView.as_view(), name='student_registration'),
]