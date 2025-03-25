
from django.apps import AppConfig
from .utils import create_admin

class MyappConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        # Correct import statement if utils.py exists
        from .utils import create_admin
        create_admin()  # Or use the function as needed
