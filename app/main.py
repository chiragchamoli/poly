from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.websockets import WebSocket

from app.api.errors.http_error import http_error_handler
from app.api.errors.validation_error import http422_error_handler
from app.api.routes.api import router as api_router
from app.api.config.base import ALLOWED_HOSTS, API_PREFIX, DEBUG, PROJECT_NAME, VERSION, REDIS_URL
from app.api.config.events import create_start_app_handler, create_stop_app_handler
from app.api.redis.connection import RedisCache


def include_router(application):
    application.include_router(api_router, prefix=API_PREFIX)


def include_middleware(application):
    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def include_exception_handlers(application):
    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(RequestValidationError, http422_error_handler)


def include_event_handlers(application):
    application.add_event_handler("startup", create_start_app_handler(application))
    application.add_event_handler("shutdown", create_stop_app_handler(application))


def get_application() -> FastAPI:
    """
        Initiates the FastAPI application by including all the required handlers.
        Includes
            - Middleware
            - Exception Handlers
            - Router
            - Event Handlers
                In the event handlers we are connecting to the redis DB.
    :return:
        application(FastAPI)
    """
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    include_middleware(application)
    include_exception_handlers(application)
    include_router(application)
    include_event_handlers(application)
    return application


app = get_application()


"""
    Initiated the Base APIs to test the server, WebSocket and Redis connections.
    
    - Http/Https Server endpoint '/'
    - Web socket endpoint '/wb'
    - Redis connection endpoint '/health-check'
"""


@app.get("/", tags=["Base URL"])
def base_url():
    return {
        "title": PROJECT_NAME,
        "version": VERSION,
        "debug": DEBUG,
        "allowed_hosts": ALLOWED_HOSTS,
        "api_prefix": API_PREFIX
    }



@app.get("/health")
async def health_check():
    try:
        value = await RedisCache.core().set('health-check', 'Redis-server:Up')
    except Exception as e:
        print(e)
        value = "Redis-server:Down"
    return {"cache_server": 'redis', 'url': str(REDIS_URL), 'health-check': value}
