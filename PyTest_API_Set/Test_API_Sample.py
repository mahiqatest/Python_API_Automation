import pytest
import requests

def test_sample1():
    assert 1 == 1

def test_sample2():
    assert 2 == 3

def test_get_bookinginfo():
    id = "3909"
    url = "https://restful-booker.herokuapp.com/booking/"

    restful_url = url + id
    print(restful_url)

    response_body = requests.get(restful_url)

    assert response_body.status_code == 200

    data = response_body.json()
    # Assert keys
    assert 'firstname' in data, "FirstName key is present"  # "Firstname key present is any msg"
    assert 'lastname' in data, "LastName key is present"

    # Assert data
    assert data["firstname"] == "Amit", "Incorrect first name"
    assert data["lastname"] == "Brown", "Incorrect last name"
    assert data["bookingdates"]["checkin"] == "2018-01-01", "Incorrect message"
