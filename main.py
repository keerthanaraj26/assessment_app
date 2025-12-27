from fastapi import FastAPI
from routes.auth_routes import router as auth_router

app = FastAPI(title="Assessment App API")

app.include_router(auth_router)

@app.get("/")
def health_check():
    return {"status": "API running"}
