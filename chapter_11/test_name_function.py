from name_function import get_formatted_name


def test_first_last_name():
    formatted_name = get_formatted_name("adam", "tykwa")
    assert formatted_name == "Adam Tykwa"


def test_first_middle_last_name():
    formatted_name = get_formatted_name("janosik", "kowalski", "andrzej")
    assert formatted_name == "Janosik Andrzej Kowalski"
