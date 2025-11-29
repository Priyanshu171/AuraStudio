from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .api.endpoints import router as gen_router

app = FastAPI(title="GenAI Content Studio")

# Serve frontend
app.mount("/", StaticFiles(directory="app/static", html=True), name="static")

# API routes
app.include_router(gen_router, prefix="/api")
