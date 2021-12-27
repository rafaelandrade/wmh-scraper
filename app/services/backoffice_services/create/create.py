from app.services.api_service.api import api_integration
from app.helpers.error_handler.main import error_handler
from app.config.config import config


def create(x_request_id: str, data: dict, table_name: str) -> dict:
    """
    Function responsible for create data
        scraped.

    Parameters:
        x_request_id: str
        data: dict
        table_name: str

    Returns:
        int
    """
    body = {"data": data, "tableName": table_name}
    path = config.get("wmh_backoffice_endpoint", None)
    token = config.get("wmh_backoffice_token", None)
    try:
        response = api_integration(
            x_request_id=x_request_id,
            url=f"{path}/v1/wmh/update-data",
            token=token,
            body=body,
        )
        response = dict(response)
        return response["data"]
    except (AssertionError, AttributeError, IndexError) as exception:
        return error_handler(
            x_request_id=x_request_id,
            _msg="Exception occurred in create service.",
            exception=exception,
        )
