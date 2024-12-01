from fastapi import FastAPI
from api.routes.todo import locs_router

app = FastAPI()
app.include_router(locs_router)

@app.get("/")
def index():
    return{"status": "locs api is running"}
