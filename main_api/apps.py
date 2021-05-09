from django.apps import AppConfig


class MainApiConfig(AppConfig): ##Class that allows for the initalisation of main_api application
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_api'
