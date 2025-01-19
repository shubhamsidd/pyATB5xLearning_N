import pytest
import allure
import requests

@allure.title("Verify the GET Request of Restfull Booker")
@allure.description("This TestCase check Booking 1 and verify the response")
@pytest.mark.positive

def test_get_request_postive():
    URL = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url=URL)
    print(response_data.text)
    assert response_data.status_code ==200

@allure.title("Verify the GET Request of Restful Booker with invalid ID")
@allure.description("This Testcase check Booking -1 and verify the response")
@pytest.mark.positive
def test_get_request_negative():
    url_get = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url=url_get)
    assert response_data.status_code == 404