from django.core.wsgi import get_wsgi_application
import os
from pathlib import Path
import sys

# Убедитесь, что BASE_DIR указывает на корневую директорию проекта
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicine.settings')
application = get_wsgi_application()

# Lambda handler
def handler(event, context):
    from mangum import Mangum
    asgi_handler = Mangum(application)
    return asgi_handler(event, context)
