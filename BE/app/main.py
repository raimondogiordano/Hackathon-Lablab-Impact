from typing import Annotated
from fastapi import BackgroundTasks, FastAPI, File, Form, UploadFile, Depends, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from app.models.utils.models import ResponseModel
from app.db import create_session
# from app.models.data.wato import Utente, Viaggio, Itinerario, Chat, Message
from app.models.data.main import QuartiereProposalModel
import psycopg2
from sqlalchemy.orm import Session

from app.router.main import router as proposalRouter

from app.db import engine
from app.config import api_prefix
import datetime
from app.version import __version__
from typing import Any, cast
from fastapi.staticfiles import StaticFiles
import os
from app.services.auth import verify_token

def get_application() -> FastAPI:
    application = FastAPI(
        title="Vox_Populi",
        description="Vox Populi API",
        version=__version__,
        swagger_ui_parameters={"defaultModelsExpandDepth": -1, "syntaxHighlight.theme": "obsidian"},
        base_url="http://localhost:8000",
    )

    include_router_with_global_prefix_prepended(application, proposalRouter)


    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Puoi specificare i domini consentiti invece di usare "*"
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    if not os.path.exists('archive'):
        os.makedirs('archive')
    application.mount("/archive", StaticFiles(directory="archive"), name="archive")
    return application

def include_router_with_global_prefix_prepended(
    application: FastAPI, router: APIRouter, **kwargs: Any
) -> None:
    """Adds the global prefix to all routes in the router."""
    processed_global_prefix = f"/{api_prefix.strip('/')}" if api_prefix else ""

    passed_in_prefix = cast(str | None, kwargs.get("prefix"))
    if passed_in_prefix:
        final_prefix = f"{processed_global_prefix}/{passed_in_prefix.strip('/')}"
    else:
        final_prefix = f"{processed_global_prefix}"
    final_kwargs: dict[str, Any] = {
        **kwargs,
        "prefix": final_prefix,
    }

    application.include_router(router, **final_kwargs)

QuartiereProposalModel.metadata.create_all(engine)

app = get_application()
