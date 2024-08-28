import os
from django.core.asgi import get_asgi_application
from fastapi.middleware.wsgi import WSGIMiddleware
from AppPotatoDisease.fastapi_app.main import app as fastapi_app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PotatoDisease.settings')

django_asgi_app = get_asgi_application()

# Mount FastAPI app to a subpath
fastapi_middleware = WSGIMiddleware(fastapi_app)

# Main ASGI application
async def application(scope, receive, send):
    if scope['path'].startswith("/api"):
        return await fastapi_middleware(scope, receive, send)
    return await django_asgi_app(scope, receive, send)
