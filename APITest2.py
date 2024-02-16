import requests



def main():
    id = "668"
    url = "https://restful-booker.herokuapp.com/booking/"

    restful_url = url+id
    print(restful_url)

    response_body = requests.get(restful_url)

    assert response_body.status_code == 200

    data = response_body.json()
    #Assert keys
    assert 'firstname' in data, "FirstName key is present" # "Firstname key present is any msg"
    assert 'lastname' in data, "LastName key is present"

    #Assert data
    assert data ["firstname"] == "Amit", "Incorrect first name"
    assert data ["lastname"] == "Test", "Incorrect last name"
    assert data ["bookingdates"]["checkin"] == "2018-01-01", "Incorrect message"

if __name__ == '__main__':
    main()