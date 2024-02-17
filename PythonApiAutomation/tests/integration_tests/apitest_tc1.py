from PythonApiAutomation.src.constants.api_constants import BASE_URL, APIConstants, base_url

def test_crud():
    print(BASE_URL)

    url_class = APIConstants.base_url()
    print(url_class)

    url_direct = base_url()
    print(url_direct)
