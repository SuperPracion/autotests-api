from http import HTTPStatus

import pytest

from clients.users.users_schema import GetUserResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_get_user_response


@pytest.mark.users
@pytest.mark.regression
def test_get_user_me(function_user, private_users_client):
    get_user_me_response = private_users_client.get_user_me_api()
    get_user_me_data = GetUserResponseSchema.model_validate_json(get_user_me_response.text)

    assert_status_code(get_user_me_response.status_code, HTTPStatus.OK)
    assert_get_user_response(get_user_me_data, function_user.response)
    validate_json_schema(get_user_me_response.json(), get_user_me_data.model_json_schema())
