from pydantic import BaseModel, Field, ConfigDict

from clients.files.files_schema import FileSchema
from clients.pydantic_create_user import UserSchema


class CourseSchema(BaseModel):
    """
    Описание структуры курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file: FileSchema = Field(alias="previewFile")
    created_by_user: UserSchema = Field(alias="createdByUser")


class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")


class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: str | None = Field(alias="maxScore")
    min_score: str | None = Field(alias="minScore")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")


class UpdateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    course: CourseSchema


class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")


class GetCourseResponseSchema(BaseModel):
    """
    Описание структуры запроса получения курсов.
    """
    model_config = ConfigDict(populate_by_name=True)

    courses: CourseSchema


class GetCoursesResponseSchema(BaseModel):
    """
    Описание структуры запроса получения курсов.
    """
    model_config = ConfigDict(populate_by_name=True)
    
    courses: list[CourseSchema]
