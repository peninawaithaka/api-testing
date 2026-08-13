import requests
import json

BASE = 'https://dummyjson.com'

def login():
    response = requests.post(f"{BASE}/auth/login",
    json={
        "username": "emilys",
        "password": "emilyspass"
    })

    assert response.status_code == 200, f'Expected: 200, but got: {response.status_code}'

    login_data = response.json()

    print("LOGIN DETAILS")
    print(json.dumps(login_data, indent=4))

    return login_data['accessToken']

if __name__ == '__main__':
    token = login()
