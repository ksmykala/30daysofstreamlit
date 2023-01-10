from fastapi.testclient import TestClient
from api.api import api


client = TestClient(api)


def test_read_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'msg': 'Hi!'}
