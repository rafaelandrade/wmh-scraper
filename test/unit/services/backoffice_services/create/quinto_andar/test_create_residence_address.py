from app.services.backoffice_services.create.quinto_andar.create_residence_address import (
    create_residence_address,
)
from app.schemas.QuintoAndarSchema import QuintoAndarSchema


def test_create_residence_address(mocker):
    """
    Test responsible for return the
        number of id that is save in database
        in these case going to return id = 5
    """
    quinto_andar_schema = QuintoAndarSchema()

    quinto_andar_schema.street_name = "street_name"
    quinto_andar_schema.district_name = "district_name"
    quinto_andar_schema.state_name = "state_name"
    mocker_create = mocker.patch(
        "app.services.backoffice_services.create.quinto_andar.create_residence_address.create",
        return_value={"id": 5},
    )

    assert (
        create_residence_address(
            x_request_id="", residence_data=quinto_andar_schema
        )
        == 5
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
        "app.services.backoffice_services.create.quinto_andar.create_residence_address.create",
        return_value=None,
    )
    assert (
        create_residence_address(
            x_request_id="", residence_data=quinto_andar_schema
        )
        is None
    )
    assert mocker_create.call_count == 1
