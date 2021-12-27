from app.schemas.QuintoAndarSchema import QuintoAndarSchema
from app.schemas.TableNameSchema import TableNameSchema
from app.services.backoffice_services.create.create import create


def create_residence_address(
    x_request_id: str, residence_data: QuintoAndarSchema
):
    """
    Function responsible for
        send the data to create of
        residence address information.

    Parameters:
        x_request_id: str
        residence_data: QuintoAndarSchema

    Returns:
    """
    tableNameSchema = TableNameSchema()
    data = {
        "street": residence_data.street_name,
        "numberResidence": None,
        "district": residence_data.district_name,
        "state": residence_data.state_name,
        "country": "Brasil",
        "CEP": None,
        "complement": None,
    }
    address_data = create(
        x_request_id=x_request_id,
        data=data,
        table_name=tableNameSchema.residence_address,
    )

    address_data = dict(address_data)

    return address_data.get("id", None)
