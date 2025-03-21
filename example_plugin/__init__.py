from fastapi import FastAPI
from .routers import example_router

def register_plugin(app: FastAPI):
    """ This method is needed to register the plugin for the main FastAPI app. """

    app.include_router(example_router.router)
