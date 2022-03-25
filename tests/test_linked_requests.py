from fastapi.testclient import TestClient

from networks_connector.src.app import api
from tests.links import get_linked_friends

client = TestClient(api)


def test_linked_request():
    response = client.get(get_linked_friends)
    assert response.status_code == 200
    if response.json():
        print(response.json())
        response = client.get(f"get_user_info?channel=vk&user={response.json()[0].get('id')}")
        assert response.status_code == 200
        print(response.json())
    else:
        print("User has no friends")
