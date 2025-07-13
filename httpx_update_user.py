import httpx

from tools.fakers import get_random_email

# create
credentials = get_random_email()
create_users_body = {
    "email": credentials,
    "password": credentials,
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
}
create_users_response = httpx.post("http://localhost:8000/api/v1/users", json=create_users_body)


# login
login_body = {
    "email": credentials,
    "password": credentials,
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_body)


# update
user_id = create_users_response.json()["user"]["id"]
access_token = login_response.json()["token"]["accessToken"]
headers = {
    "Authorization": f"Bearer {access_token}",
}
update_users_body = {
    "email": get_random_email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
update_users_response = httpx.patch(f"http://localhost:8000/api/v1/users/{user_id}", json=update_users_body, headers=headers)
