import pytest
from main import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_index_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200


def test_index_contains_default_message(client):
    response = client.get("/")
    assert b"Hello from Flask on Kubernetes!" in response.data


def test_index_returns_html(client):
    response = client.get("/")
    assert b"<html>" in response.data
