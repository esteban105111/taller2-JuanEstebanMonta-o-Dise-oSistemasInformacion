from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_endpoint_principal():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "API Calculadora funcionando"}


def test_endpoint_sumar_numeros_positivos():
    response = client.post("/sumar", json={"a": 5, "b": 3})

    assert response.status_code == 200
    assert response.json()["result"] == 8


def test_endpoint_sumar_numeros_negativos():
    response = client.post("/sumar", json={"a": -5, "b": -3})

    assert response.status_code == 200
    assert response.json()["result"] == -8


def test_endpoint_restar_numeros_positivos():
    response = client.post("/restar", json={"a": 10, "b": 4})

    assert response.status_code == 200
    assert response.json()["result"] == 6


def test_endpoint_restar_numeros_negativos():
    response = client.post("/restar", json={"a": -10, "b": -4})

    assert response.status_code == 200
    assert response.json()["result"] == -6


def test_endpoint_multiplicar_numeros_positivos():
    response = client.post("/multiplicar", json={"a": 6, "b": 7})

    assert response.status_code == 200
    assert response.json()["result"] == 42


def test_endpoint_multiplicar_numeros_negativos():
    response = client.post("/multiplicar", json={"a": -6, "b": -7})

    assert response.status_code == 200
    assert response.json()["result"] == 42


def test_endpoint_dividir_numeros_positivos():
    response = client.post("/dividir", json={"a": 20, "b": 5})

    assert response.status_code == 200
    assert response.json()["result"] == 4


def test_endpoint_dividir_numeros_negativos():
    response = client.post("/dividir", json={"a": -20, "b": -5})

    assert response.status_code == 200
    assert response.json()["result"] == 4


def test_endpoint_dividir_entre_cero():
    response = client.post("/dividir", json={"a": 20, "b": 0})

    assert response.status_code == 400
    assert response.json() == {"detail": "No se puede dividir entre cero"}


def test_endpoint_rechaza_valores_no_numericos():
    response = client.post("/sumar", json={"a": "texto", "b": 3})

    assert response.status_code == 422
