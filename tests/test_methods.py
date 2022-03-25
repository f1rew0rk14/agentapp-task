from fastapi.testclient import TestClient

from networks_connector.src.app import api
from tests.links import get_info_link_exc, get_info_link_success, get_info_link_not_found, \
    get_wall_link_success, get_wall_link_exc, get_wall_link_conflict, \
    get_friends_link_success, get_friends_link_conflict, get_friends_link_exc

client = TestClient(api)


def test_get_user_info():
    response = client.get(get_info_link_success)
    assert response.status_code == 200
    response = client.get(get_info_link_not_found)
    assert response.status_code == 409
    response = client.get(get_info_link_exc)
    assert response.status_code == 500


def test_get_user_wall():
    response = client.get(get_wall_link_success)
    assert response.status_code == 200
    response = client.get(get_wall_link_conflict)
    assert response.status_code == 409
    response = client.get(get_wall_link_exc)
    assert response.status_code == 500


def test_get_user_friends():
    response = client.get(get_friends_link_success)
    assert response.status_code == 200
    response = client.get(get_friends_link_conflict)
    assert response.status_code == 409
    response = client.get(get_friends_link_exc)
    assert response.status_code == 500
