from pydantic import BaseModel, Field, ConfigDict

from clients.files.files_schema import FileSchema
from clients.pydantic_create_user import UserSchema


class ExerciseSchema(BaseModel):
    """
    Описание структуры курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str| None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")


class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления курса.
    """
    exercise: ExerciseSchema


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    model_config = ConfigDict(populate_by_name=True)

    course_is: str = Field(alias="courseId")


class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры запроса получения курсов.
    """
    exercises: ExerciseSchema


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры запроса получения курсов.
    """
    exercises: list[ExerciseSchema]
