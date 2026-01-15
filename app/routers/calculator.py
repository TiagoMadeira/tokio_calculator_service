from fastapi import APIRouter
from fastapi.responses import JSONResponse
from opentelemetry import trace

router = APIRouter()
tracer = trace.get_tracer(__name__)

@router.get("/add/{a}&{b}")
def add(a: int, b: int):
    tracer.start_as_current_span(f"GET /add/{a}&{b}")
    result = a + b
    return JSONResponse( content = {"result": result} )

@router.get("/subtract/{a}&{b}")
def subtract(a: int, b: int):
    tracer.start_as_current_span(f"GET /subtract/{a}&{b}")
    result = a - b
    return JSONResponse( content = {"result": result} )

@router.get("/multiply/{a}&{b}")
def multiply(a: int, b: int):
    tracer.start_as_current_span(f"GET /multiply/{a}&{b}")
    result = a * b
    return JSONResponse( content = {"result": result} )

@router.get("/divide/{a}&{b}")
def divide(a: int, b: int):
    tracer.start_as_current_span(f"GET /divide/{a}&{b}")
    result = a / b
    return JSONResponse( content = {"result": result} )