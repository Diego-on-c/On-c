from models.calendar import Calendar


def test_calendar_get_year():
    year = 2020

    calendar = Calendar(year, str, int, str)

    result = calendar.get_year()

    assert result == year

    year = 2045

    calendar = Calendar(year, str, int, str)

    result = calendar.get_year()

    assert result == year


def test_calendar_get_month():
    month = 'july'

    calendar = Calendar(int, month, int, str)

    result = calendar.get_month()

    assert result == month

    month = 'april'

    calendar = Calendar(int, month, int, str)

    result = calendar.get_month()

    assert result == month


def test_calendar_get_day():
    day = 25

    calendar = Calendar(int, str, day, str)

    result = calendar.get_day()

    assert result == day

    day = 13

    calendar = Calendar(int, str, day, str)

    result = calendar.get_day()

    assert result == day


def test_calendar_get_tag():
    tag = 'Aloe'

    calendar = Calendar(int, str, int, tag)

    result = calendar.get_tag()

    assert result == tag




