from app.services.backoffice_services.create.quinto_andar.create_residence import (
    create_residence,
)
from app.schemas.QuintoAndarSchema import QuintoAndarSchema


def test_create_residence(mocker):
    """
    Test responsible for return the
        number of id that is save in database
        in these case going to return id = 1
    """
    quinto_andar_schema = QuintoAndarSchema()

    quinto_andar_schema.residence_id = 1
    quinto_andar_schema.source = "source"
    quinto_andar_schema.link_apartment = "link_apartment"
    quinto_andar_schema.number_rooms = 1
    quinto_andar_schema.number_bathrooms = 1
    quinto_andar_schema.number_parking_space = 1
    quinto_andar_schema.type_building = "typeBuilding"
    quinto_andar_schema.size_residence = 210
    mocker_create = mocker.patch(
        "app.services.backoffice_services.create.quinto_andar.create_residence.create",
        return_value={"id": 1},
    )

    assert (
        create_residence(
            x_request_id="",
            residence_address_id=1,
            residence_data=quinto_andar_schema,
        )
        == 1
    )
    assert mocker_create.call_count == 1


def test_create_residence_none(mocker):
    """
    Result:
        Expect return None
            in case of some error happens.
    """
    quinto_andar_schema = QuintoAndarSchema()

    mocker_create = mocker.patch(
        "app.services.backoffice_services.create.quinto_andar.create_residence.create",
        return_value=None,
    )
    assert (
        create_residence(
            x_request_id="",
            residence_address_id=1,
            residence_data=quinto_andar_schema,
        )
        is None
    )
    assert mocker_create.call_count == 1
