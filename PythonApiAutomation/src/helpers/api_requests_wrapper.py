# To make POST, PUT, PATCH, DELETE requests

import requests

class APIConstants(object):
    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"

    #Update put patch delete  -Booking id
    def url_put_patch_delete_booking(self, booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(self.booking_id)