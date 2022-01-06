from app.schemas.QuintoAndarSchema import QuintoAndarSchema
from app.schemas.TableNameSchema import TableNameSchema
from app.services.backoffice_services.create.create import create
from app.helpers.logger.console_logger import send_log
from app.helpers.error_handler.main import error_handler


def create_residence_values(
    x_request_id: str, residence_id: int, residence_data: QuintoAndarSchema
) -> None:
    """
    Function responsible for create residence
        values.

    Parameters:
        x_request_id: str
        residence_id: int
        residence_data: QuintoAndarSchema

    Returns:
        int
    """
    try:
        table_name = TableNameSchema()
        data = {
            "ResidenceId": residence_id,
            "price": float(residence_data.rent_price_without_tax),
            "condominiumTax": float(residence_data.condominium_tax),
            "houseTax": float(residence_data.house_tax),
            "fireInsurence": float(residence_data.fire_insurance),
            "serviceTax": float(residence_data.service_tax),
            "totalRentPrice": float(residence_data.total_rent_price),
        }

        residence_values = create(
            x_request_id=x_request_id,
            data=data,
            table_name=table_name.residence_values,
        )
        send_log(
            x_request_id=x_request_id,
            message=f"Inserted in database the follow residence values {residence_values}...",
        )
    except (
        TimeoutError,
        SyntaxError,
        IndexError,
        AttributeError,
    ) as exception:
        return error_handler(
            x_request_id=x_request_id,
            exception=exception,
            _msg="Exception occurred in create_residence_value",
        )
