from clients.users.users_schema import UserSchema
from tools.assertions.base import assert_equal


def assert_user(actual: UserSchema, expected: UserSchema):
    """
    Проверяет корректность пользовательских моделей.

    :param actual: Объект UserSchema.
    :raises expected: Объект UserSchema.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.last_name, expected.last_name, "last_name")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.middle_name, expected.middle_name, "middle_name")


def assert_get_user_response(get_user_response, create_user_response):
    """
    Проверяет корректности данных пользователя при создании и при запросе.

    :param get_user_response: ответ API при запросе пользователя.
    :raises create_user_response: ответ API при создании пользователя.
    """
    assert_user