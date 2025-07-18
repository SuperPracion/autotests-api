from pydantic import BaseModel
import pytest

from clients.exercises.exercises_client import ExercisesClient, get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.users import UserFixture


class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema


@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentication_user)


@pytest.fixture
def function_exercise(exercises_client: ExercisesClient) -> ExerciseFixture:
    request = CreateExerciseRequestSchema()
    response = exercises_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)
