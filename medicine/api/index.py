from django.core.wsgi import get_wsgi_application
from vercel_wsgi import make_lambda_handler


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicine.settings')
application = get_wsgi_application()
handler = make_lambda_handler(application)
