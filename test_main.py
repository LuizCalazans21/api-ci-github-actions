from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_somar():
    response = client.get("/somar/2/3")
    assert response.json() == {"resultado": 5}

def test_multiplicar():
    response = client.get("/multiplicar/2/2")
    # ERRO INTENCIONAL: 2*2 é 4, não 5
    assert response.json() == {"resultado": 5}