from typing import TypedDict
from clients.api_client import APIClient, Response
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class Exercise(TypedDict):
    """
    Описание структуры задания.
    """

    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение заданий курса.
    """

    userId: str


class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа получения задания.
    """

    exercise: Exercise


class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа получения заданий.
    """

    exercises: list[Exercise]


class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание задания.
    """

    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str
    estimatedTime: str | None


class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа создания задания.
    """

    exercise: Exercise


class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление задания.
    """

    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа обновления задания.
    """

    exercise: Exercise


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод выполняет получение списка заданий для определенного курса.

        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", query=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания задания.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(
        self, exercise_id: str, request: UpdateExerciseRequestDict
    ) -> Response:
        """
        Метод обновления задания.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Метод выполняет получение списка заданий для определенного курса.

        :param query: GetExercisesQueryDict
        :return: GetExercisesResponseDict
        """
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        """
        Метод получения задания.

        :param exercise_id: Идентификатор задания.
        :return: GetExerciseResponseDict
        """
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise(
        self, request: CreateExerciseRequestDict
    ) -> CreateExerciseResponseDict:
        """
        Метод создания задания.

        :param request: CreateExerciseRequestDict
        :return: CreateExerciseResponseDict
        """
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(
        self, exercise_id: str, request: UpdateExerciseRequestDict
    ) -> UpdateExerciseResponseDict:
        """
        Метод обновления задания.

        :param exercise_id: Идентификатор задания.
        :param request: UpdateExerciseRequestDict
        :return: UpdateExerciseResponseDict
        """
        response = self.update_exercise_api(exercise_id, request)
        return response.json()


def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
