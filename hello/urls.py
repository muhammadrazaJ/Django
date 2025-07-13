from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]
# This file defines the URL patterns for the 'hello' app.
# It maps the root URL of the app to the `hello_world` view function.