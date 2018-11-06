from django.apps import AppConfig


class DialogsConfig(AppConfig):
    name = 'dialogs'

    def ready(self):
        import iSi_apps.dialogs.signals
