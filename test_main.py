import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_product():
    response = client.post("/product", json={"name": "Test Product", "price": 9.99, "quantity": 10})
    assert response.status_code == 201
    assert response.json() == {"message": "Product created successfully."}


def test_get_products():
    response = client.get("/product")
    assert response.status_code == 200
    assert "data" in response.json()
    assert isinstance(response.json()["data"], list)

def test_get_product_id():
    create_response = client.post("/product", json={"name": "Test Product", "price": 9.99, "quantity": 10})
    assert create_response.status_code == 201
    get_all_response = client.get("/product")
    assert get_all_response.status_code == 200
    products = get_all_response.json()["data"]
    product_id = products[0]["id"]
    update_response = client.get(f"/product/{product_id}")
    assert update_response.status_code == 200
    data = update_response.json()['data']
    assert data

def test_update_product():
    create_response = client.post("/product",json={"name": "Test Product", "price": 9.99, "quantity": 10})
    assert create_response.status_code == 201
    get_all_response = client.get("/product")
    assert get_all_response.status_code == 200
    products = get_all_response.json()["data"]
    product_id = products[0]["id"]

    update_response = client.put(f"/product/{product_id}",json={"name": "Updated Test Product", "price": 19.99})
    assert update_response.status_code == 200
    assert update_response.json() == {"message": "Product updated successfully."}


def test_delete_product():
    delete_response = client.delete("/product/1")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": "Product deleted successfully."}
