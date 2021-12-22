from schemas.QuintoAndarSchema import QuintoAndarSchema
from schemas.TableNameSchema import TableNameSchema
from services.backoffice_services.create.create import create
from helpers.logger.console_logger import log


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
    table_name = TableNameSchema()
    data = {
        "ResidenceId": residence_id,
        "price": residence_data.rent_price_without_tax,
        "condominiumTax": residence_data.condominium_tax,
        "houseTax": residence_data.house_tax,
        "fireInsurence": residence_data.fire_insurance,
        "serviceTax": residence_data.service_tax,
        "totalRentPrice": residence_data.total_rent_price,
    }

    residence_values = create(
        x_request_id=x_request_id,
        data=data,
        table_name=table_name.residence_values,
    )
    log(
        x_request_id=x_request_id,
        message=f"Inserted in database the follow residence values {residence_values}...",
    )
