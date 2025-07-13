import httpx

login_body = {
    "email": "superpracion@example.com",
    "password": "superpracion",
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_body)


access_token = login_response.json()["token"]["accessToken"]
headers = {
    "Authorization": f"Bearer {access_token}",
}
me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
print(me_response.json())
print(me_response.status_code)
