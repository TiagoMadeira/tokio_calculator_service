from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/add/{a}&{b}")
def add(a: int, b: int):
    result = a + b
    return JSONResponse( content = {"result": result} )

@router.get("/subtract/{a}&{b}")
def subtract(a: int, b: int):
    result = a - b
    return JSONResponse( content = {"result": result} )

@router.get("/multiply/{a}&{b}")
def multiply(a: int, b: int):
    result = a * b
    return JSONResponse( content = {"result": result} )

@router.get("/divide/{a}&{b}")
def divide(a: int, b: int):
    result = a / b
    return JSONResponse( content = {"result": result} )