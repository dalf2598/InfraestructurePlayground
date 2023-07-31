from fastapi import FastAPI
import uvicorn
from routes import student_routes

app = FastAPI()

app.include_router(student_routes.router)

if __name__ == "__main__":
    uvicorn.run('main:app', host="localhost", port=8000, reload=True)
