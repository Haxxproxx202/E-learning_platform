import os
import django
from channels.routing import get_default_application
from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'E_learning_platform.settings')
django.setup()
application = get_default_application()
