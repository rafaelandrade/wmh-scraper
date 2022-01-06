from app.services.backoffice_services.create.create import create


def test_create(mocker):
    """
    Should return data
        created in database
        from residence functions
    """
    data_mock = {"data": {"id": 1, "name": "teste"}}
    mocker_api_integration = mocker.patch(
        "app.services.backoffice_services.create.create.api_integration",
        return_value=data_mock,
    )

    assert (
        create(x_request_id="", data={}, table_name="table_name")
        == data_mock["data"]
    )
    assert mocker_api_integration.call_count == 1


def test_error_handler(mocker):
    """
    Should call error_handler
        in case of some error
    """
    mocker_api_integration = mocker.patch(
        "app.services.backoffice_services.create.create.api_integration",
        return_value={},
    )
    mocker_error_handler = mocker.patch(
        "app.services.backoffice_services.create.create.error_handler",
        return_value=None,
    )

    assert create(x_request_id="", data={}, table_name="table_name") is None
    assert mocker_api_integration.call_count == 1
    assert mocker_error_handler.call_count == 1
