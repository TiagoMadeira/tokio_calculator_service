from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.routers import calculator
import uvicorn

app = FastAPI()
app.include_router(calculator.router)

@app.get('/heatlhz')
def healthz():
    return JSONResponse( code = 200 )

if __name__ == '__main__':
    print("Webserver: rest service starting")
    uvicorn.run( app, host='0.0.0.0', port=5000)

