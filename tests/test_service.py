import pytest
from service import get_user_from_db, get_users, User
import unittest.mock as mock
import requests


@mock.patch("service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Alice"
    user_name = get_user_from_db(1)
    
    
    assert user_name == "Alice"
    
@mock.patch("requests.get")
def test_get_users(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value =  [
        {
            "id": 1,
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz",
            "address": {
                "street": "Kulas Light",
                "suite": "Apt. 556",
                "city": "Gwenborough",
                "zipcode": "92998-3874",
                "geo": {"lat": "-37.3159", "lng": "81.1496"}
            },
            "phone": "1-770-736-8031 x56442",
            "website": "hildegard.org",
            "company": {
                "name": "Romaguera-Crona",
                "catchPhrase": "Multi-layered client-server neural-net",
                "bs": "harness real-time e-markets"
            }
        }
    ]
    
    mock_get.return_value = mock_response
    
    data = get_users()
    
    assert isinstance(data, list)
    assert all(isinstance(user, User) for user in data)
    
    
@mock.patch("requests.get")
def test_get_users_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    
    with pytest.raises(requests.HTTPError):
        get_users()