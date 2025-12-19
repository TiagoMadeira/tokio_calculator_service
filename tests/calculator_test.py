import pytest
import sys;sys.path.append('.')
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_add():
    response = client.get("/add/1&4")
    assert response.status_code == 200
    assert response.json() == {"result": 5}

def test_subtraction():
    response = client.get("/subtract/1&4")
    assert response.status_code == 200
    assert response.json() == {"result": -3}
    

def test_multiplication():
    response = client.get("/multiply/2&4")
    assert response.status_code == 200
    assert response.json() == {"result": 8}

def test_division():
    response = client.get("/divide/8&4")
    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_type_error():
    response = client.get("/add/1&\"error\"")
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "Input should be a valid integer, unable to parse string as an integer"

def test_division_by_zero_error():
    with pytest.raises(ZeroDivisionError):
        response = client.get("/divide/2&0")
        assert response.json() == {"result": 2}
    
