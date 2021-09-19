from utils.formatting_events import formatting_events


def test_formatting_events():
    """
    Should turn all words in lower case
    """
    event = "Name_Of_Event"

    assert formatting_events(event=event) == event.lower()
