from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseSettings
from routers import product_router, user_router, auth_router, chat_router
from services.product_service import ProductService
from services.user_service import UserService

class Settings(BaseSettings):
    authjwt_secret_key: str = "your_jwt_secret_key"

@AuthJWT.load_config
def get_config():
    return Settings()

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Routers
app.include_router(product_router, prefix="/products")
app.include_router(user_router, prefix="/users")
app.include_router(auth_router, prefix="/auth")
app.include_router(chat_router, prefix="/chat")

@app.get("/")
def read_root():
    return {"message": "Welcome to SaaS Application API"}

# Health Check
@app.get("/health")
def health_check():
    return {"status": "Healthy"}