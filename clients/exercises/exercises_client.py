import allure

from clients.api_client import APIClient, Response
from clients.exercises.exercises_schema import (
    CreateExerciseRequestSchema, 
    CreateExerciseResponseSchema, 
    GetExerciseResponseSchema, 
    GetExercisesQuerySchema, 
    GetExercisesResponseSchema, 
    UpdateExerciseRequestSchema, 
    UpdateExerciseResponseSchema,
)
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    @allure.step("Get exercises by course_is {query.course_is}")
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Метод выполняет получение списка заданий для определенного курса.

        :param query: GetExercisesQuerySchema
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    @allure.step("Get exercise by exercise_id {exercise_id}")
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    @allure.step("Create exercise")
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания задания.

        :param request: CreateExerciseRequestSchema
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    @allure.step("Update exercise by id {exercise_id}")
    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Метод обновления задания.

        :param exercise_id: Идентификатор задания.
        :param request: UpdateExerciseRequestSchema
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True))

    @allure.step("Delete exercise by id {exercise_id}")
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """
        Метод выполняет получение списка заданий для определенного курса.

        :param query: GetExercisesQuerySchema
        :return: Ответ от сервера в виде объекта GetExercisesResponseSchema
        """
        response = self.get_exercises_api(query=query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Метод получения задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта GetExerciseResponseSchema
        """
        response = self.get_exercise_api(exercise_id=exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Метод создания задания.

        :param request: CreateExerciseRequestSchema
        :return: Ответ от сервера в виде объекта CreateExerciseResponseSchema
        """
        response = self.create_exercise_api(request=request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        """
        Метод обновления задания.

        :param exercise_id: Идентификатор задания.
        :param request: UpdateExerciseRequestSchema
        :return: Ответ от сервера в виде объекта UpdateExerciseResponseSchema
        """
        response = self.update_exercise_api(exercise_id=exercise_id, request=request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
