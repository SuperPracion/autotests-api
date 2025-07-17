from http import HTTPStatus

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


def test_login():

    public_users_client = get_public_users_client() # Инициализировать клиентов

    create_user_request = CreateUserRequestSchema()
    public_users_client.create_user(create_user_request) # Создать нового пользователя

    authentication_user = AuthenticationUserSchema(
        email=create_user_request.email,
        password=create_user_request.password,
    )

    private_users_client = get_authentication_client()
    authentication_user_response = private_users_client.login_api(authentication_user) # Выполнить аутентификацию

    login_response_data = LoginResponseSchema.model_validate_json(authentication_user_response.text) # Десериализовать JSON-ответ в LoginResponseSchema

    assert_status_code(authentication_user_response.status_code, HTTPStatus.OK) # Проверить статус-код ответа
    assert_login_response(login_response_data) # Проверить корректность тела ответа
    validate_json_schema(authentication_user_response.json(), login_response_data.model_json_schema()) # Выполнить валидацию JSON-схемы
