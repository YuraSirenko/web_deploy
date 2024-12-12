from django.apps import AppConfig
import logging

class MyAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "math_app"

    def ready(self):
        # Enable SDK-level debugging
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s %(levelname)s %(message)s"
        )
