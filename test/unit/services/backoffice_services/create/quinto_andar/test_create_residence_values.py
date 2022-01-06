from app.services.backoffice_services.create.quinto_andar.create_residence_values import (
    create_residence_values,
)
from app.schemas.QuintoAndarSchema import QuintoAndarSchema


def test_create_residence_values(mocker):
    """
    Should return None
        and create function should be called
        1 time.
    """
    quinto_andar_schema = QuintoAndarSchema()

    quinto_andar_schema.rent_price_without_tax = 1111
    quinto_andar_schema.condominium_tax = 222.2
    quinto_andar_schema.house_tax = 21.21
    quinto_andar_schema.fire_insurance = 21212.2
    quinto_andar_schema.service_tax = 12121.2
    quinto_andar_schema.total_rent_price = 1111111
    mocker_create = mocker.patch(
        "app.services.backoffice_services.create."
        "quinto_andar.create_residence_values.create",
        return_value=None,
    )

    assert (
        create_residence_values(
            x_request_id="", residence_id=1, residence_data=quinto_andar_schema
        )
        is None
    )
    assert mocker_create.call_count == 1


def test_create_residence_values_error_handler(mocker):
    """
    Should call error_handler
        in case of some wrong
        happens.
    """
    mocker_error_handler = mocker.patch(
        "app.services.backoffice_services.create.quinto_andar."
        "create_residence_values.error_handler",
        return_value=None,
    )

    assert (
        create_residence_values(
            x_request_id="", residence_id=1, residence_data={}
        )
        is None
    )
    assert mocker_error_handler.call_count == 1
