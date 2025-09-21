from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .db import Base, engine
from .routers import products, auth

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    openapi_tags=[
        {"name": "auth", "description": "Login to get a JWT token."},
        {
            "name": "products",
            "description": "Browse and manage products with search, sort, and pagination.",
        },
    ],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix=settings.API_PREFIX)
app.include_router(products.router, prefix=settings.API_PREFIX)


@app.get("/", tags=["meta"])
def root():
    return {
        "app": settings.APP_NAME,
        "docs": f"{settings.API_PREFIX}/docs"
    }
