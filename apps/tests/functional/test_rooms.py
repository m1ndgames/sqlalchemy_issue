import json


headers = {"Content-Type": "application/json", "Accept": "application/json"}

endpoint = "/api/rooms"


def test_rooms_get(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/api/rooms' page is requested (GET)
    THEN check that the response is valid
    """
    with test_client:
        response = test_client.get(endpoint)
        assert response.status_code == 200
        assert response.json == []


def test_rooms_post(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/api/rooms' page is requested (POST)
    THEN check that the response is valid
    """
    with test_client:
        data = {"name": "Test Room"}

        response = test_client.post(endpoint, data=json.dumps(data), headers=headers)

        assert response.status_code == 201
        assert response.json == {"id": 1, "name": "Test Room"}


def test_rooms_put(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/api/rooms' page is requested (PUT)
    THEN check that the response is valid
    """
    with test_client:
        data = {"id": 1, "name": "Tested Room"}

        response = test_client.put(endpoint, data=json.dumps(data), headers=headers)

        assert response.status_code == 200
        assert response.json == {"id": 1, "name": "Tested Room"}


def test_rooms_delete(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/api/rooms' page is requested (DELETE)
    THEN check that the response is valid
    """
    with test_client:
        data = {"id": 1}

        response = test_client.delete(endpoint, data=json.dumps(data), headers=headers)

        assert response.status_code == 200
        assert response.json == {"message": "Room deleted"}
