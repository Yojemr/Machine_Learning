import os
import sys
from pathlib import Path

from django.core.asgi import get_asgi_application

from backend.main import app

# El proyecto Django usa módulos locales también al ejecutarse por separado.
sys.path.insert(0, str(Path(__file__).resolve().parent / 'frontend'))
os.environ['ESTIMADOR_INTEGRADO'] = '1'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django_app = get_asgi_application()


@app.get('/health', include_in_schema=False)
def health():
    return {'status': 'ok'}


# FastAPI registra primero sus rutas. Django atiende las demás, incluida '/'.
app.mount('/', django_app)
