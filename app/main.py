from fastapi import FastAPI
from fastapi.responses import JSONResponse
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from app.routers import calculator
import uvicorn




#Init otel tracel
otel_trace_init()
#Instrument the requests module
RequestsInstrumentor().instrument()

app = FastAPI()
FastAPIInstrumentor().instrument_app(app)

app.include_router(calculator.router)

@app.get('/heatlhz')
def healthz():
    return JSONResponse( code = 200 )

if __name__ == '__main__':
    print("Webserver: rest service starting")
    uvicorn.run( app, host='0.0.0.0', port=5000)

