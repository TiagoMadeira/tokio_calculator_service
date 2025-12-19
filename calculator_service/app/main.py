from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .routers import calculator

app = FastAPI()
app.include_router(calculator.router)

@app.get('/heatlhz')
def healthz():
    return JSONResponse( code = 200 )

