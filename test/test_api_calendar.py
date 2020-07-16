from services.api_calendar import Api
import pytest


@pytest.fixture
def calendar():
    calendar = Api(
        year=2020,
        month=7,
        day=25,
        plant="Aloe")
    return calendar


def test_calendar_return_json(calendar):
    expected = json
    result = calendar.convertJson()

    assert expected == result


