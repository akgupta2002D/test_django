from django.apps import AppConfig


class TodoappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "todoApp"


class UserprofileConfig(AppConfig):
    name = 'userprofile'

    def ready(self):
        import todoApp.signals
