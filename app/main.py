from fastapi import FastAPI
from app.views import router

app = FastAPI()
#main router
app.include_router(router)


