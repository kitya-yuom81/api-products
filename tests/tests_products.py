from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_list_products_empty():
    r = client.get("/api/products")
    assert r.status_code == 200
    assert isinstance(r.json(), list)