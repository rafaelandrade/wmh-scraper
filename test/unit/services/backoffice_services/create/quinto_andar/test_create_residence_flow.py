from app.services.backoffice_services.create.quinto_andar.create_residence_flow import (
    creation_residence_data,
)
from app.schemas.QuintoAndarSchema import QuintoAndarSchema


def test_create_residence_flow(mocker):
    """
    Should call 1 time
        all the creation residence data functions
    """
    quinto_andar_schema = QuintoAndarSchema()
    mocker_create_address = mocker.patch(
        "app.services.backoffice_services.create.quinto_andar."
        "create_residence_flow.create_residence_address",
        return_value=1,
    )
    mocker_create_residence = mocker.patch(
        "app.services.backoffice_services.create.quinto_andar."
        "create_residence_flow.create_residence",
        return_value=2,
    )
    mocker_create_residence_values = mocker.patch(
        "app.services.backoffice_services.create.quinto_andar."
        "create_residence_flow.create_residence_values",
        return_value=None,
    )
    mocker_deal_with_feature = mocker.patch(
        "app.services.backoffice_services.create.quinto_andar."
        "create_residence_flow.deal_with_feature",
        return_value=None,
    )

    quinto_andar_schema.pet_flag = True
    quinto_andar_schema.metro_flag = False
    quinto_andar_schema.furniture_flag = True

    assert (
        creation_residence_data(
            x_request_id="", residence_data=quinto_andar_schema
        )
        is None
    )
    assert mocker_create_address.call_count == 1
    assert mocker_create_residence.call_count == 1
    assert mocker_create_residence_values.call_count == 1
    assert mocker_deal_with_feature.call_count == 1


def test_error_handler(mocker):
    """
    Should call error_handler
    """
    mocker_create_address = mocker.patch(
        "app.services.backoffice_services.create.quinto_andar."
        "create_residence_flow.create_residence_address",
        return_value=1,
    )
    mocker_create_residence = mocker.patch(
        "app.services.backoffice_services.create.quinto_andar."
        "create_residence_flow.create_residence",
        return_value=2,
    )
    mocker_create_residence_values = mocker.patch(
        "app.services.backoffice_services.create.quinto_andar."
        "create_residence_flow.create_residence_values",
        return_value=None,
    )
    mocker_deal_with_feature = mocker.patch(
        "app.services.backoffice_services.create.quinto_andar."
        "create_residence_flow.deal_with_feature",
        return_value=None,
    )
    mocker_error_handler = mocker.patch(
        "app.services.backoffice_services.create.quinto_andar."
        "create_residence_flow.error_handler",
        return_value=None,
    )
    assert creation_residence_data(x_request_id="", residence_data={}) is None
    assert mocker_error_handler.call_count == 1
    assert mocker_create_address.call_count == 1
    assert mocker_create_residence.call_count == 1
    assert mocker_create_residence_values.call_count == 1
    assert mocker_deal_with_feature.call_count == 0
