import requests

def test_contact_api():
    url = "https://doonarchitects.com/api/contact"

    payload = {
        "name": "Vansh",
        "email": "test@gmail.com",
        "phone": "9876543210",
        "message": "Testing API"
    }

    response = requests.post(url, json=payload)

    assert response.status_code in [200, 201]