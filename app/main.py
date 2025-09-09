from fastapi import FastAPI
from app.api.routes import router  # make sure path is correct

app = FastAPI(title="Marksheet Extraction API")

app.include_router(router, prefix="/api")  # router prefix

@app.get("/")
def health_check():
    return {"message": "Marksheet Extraction API is running"}
