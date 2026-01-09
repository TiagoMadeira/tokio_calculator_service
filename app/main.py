from fastapi import FastAPI
from fastapi.responses import JSONResponse
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from app.routers import calculator
import uvicorn

# --------------------------
# OpenTelemetry Tracing
# --------------------------
def otel_trace_init():
    trace.set_tracer_provider(
       TracerProvider(
           resource=Resource.create({}),
       ),
    )

otel_trace_init()
app = FastAPI()
FastAPIInstrumentor().instrument_app(app)
app.include_router(calculator.router)

@app.get('/heatlhz')
def healthz():
    return JSONResponse( code = 200 )

if __name__ == '__main__':
    print("Webserver: rest service starting")
    uvicorn.run( app, host='0.0.0.0', port=5000)

