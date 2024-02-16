import requests
def main():

    response_body= requests.get("https://restful-booker.herokuapp.com/booking/2008")

    if response_body.status_code == 200:
        print("TC#1 - Get booking info successful")
    else:
        print("TC#1 - Get booking info failed")

if __name__ == '__main__':
    main()