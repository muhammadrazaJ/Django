# myproject/urls.py (excerpt)
from django.contrib import admin
from django.urls import path, include # Ensure 'include' is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')), # Add this line
]

