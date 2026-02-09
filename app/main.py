from fastapi import FastAPI
from fastapi.responses import JSONResponse
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from app.routers import calculator
from app.utils import otel_trace_init
from app.config import settings

app = FastAPI()
app.include_router(calculator.router)

if settings.ENABLE_MONOTORING:
    #Init otel tracel
    otel_trace_init()
    #Instrument the requests module
    RequestsInstrumentor().instrument()
    FastAPIInstrumentor().instrument_app(app)

@app.get('/heatlhz')
def healthz():
    return JSONResponse( code = 200 )

