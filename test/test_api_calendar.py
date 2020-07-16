from models.api_calendar import Calendar
import pytest


@pytest.fixture
def calendar():
    calendar = Calendar(
        year= "2020",
        month= "7",
        day="25",
        plant="Aloe")

    return calendar


def test_calendar_return_json(calendar):
    expected =[{"year": "2020",
        "month": "7",
        "day": "25",
        "plant": "Aloe"}]

    result = calendar.convertJson()

    return expected == result

