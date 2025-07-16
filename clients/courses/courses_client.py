from httpx import Response

from clients.api_client import APIClient
from clients.courses.courses_schema import (
    CreateCourseRequestSchema,
    CreateCourseResponseSchema,
    GetCourseResponseSchema,
    GetCoursesQuerySchema,
    GetCoursesResponseSchema,
    UpdateCourseRequestSchema,
    UpdateCourseResponseSchema,
)
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """

    def get_courses_api(self, query: GetCoursesQuerySchema) -> GetCoursesResponseSchema:
        """
        Метод получения списка курсов.

        :param query: GetCoursesQuerySchema
        :return: Ответ в виде объекта GetCoursesResponseSchema
        """
        response = self.get("/api/v1/courses", params=query.model_dump(by_alias=True))
        return GetCoursesResponseSchema.model_validate_json(response.text)

    def get_course_api(self, course_id: str) -> GetCourseResponseSchema:
        """
        Метод получения курса.

        :param course_id: Идентификатор курса.
        :return: Ответ в виде объекта GetCourseResponseSchema
        """
        response = self.get(f"/api/v1/courses/{course_id}")
        return GetCourseResponseSchema.model_validate_json(response.text)

    def create_course_api(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        """
        Метод создания курса.

        :param request: CreateCourseRequestSchema
        :return: Ответ в виде объекта CreateCourseResponseSchema
        """
        response = self.post("/api/v1/courses", json=request.model_dump(by_alias=True))
        return CreateCourseResponseSchema.model_validate_json(response.text)

    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> UpdateCourseResponseSchema:
        """
        Метод обновления курса.

        :param course_id: Идентификатор курса.
        :param request: UpdateCourseRequestSchema.
        :return: Ответ в виде объекта UpdateCourseResponseSchema
        """
        response = self.patch(f"/api/v1/courses/{course_id}", json=request.model_dump(by_alias=True))
        return UpdateCourseResponseSchema.model_validate_json(response.text)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")

    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        return self.create_course_api(request)

def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))
