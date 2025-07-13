from django.apps import AppConfig


class StudentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'students'
# This configuration class is used to set up the 'students' app in the Django project.
# It specifies the default field type for auto-generated primary keys and the name of the app.