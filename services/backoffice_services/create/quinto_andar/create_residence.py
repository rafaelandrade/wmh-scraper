from schemas.QuintoAndarSchema import QuintoAndarSchema
from schemas.TableNameSchema import TableNameSchema
from services.backoffice_services.create.create import create


def create_residence(
    x_request_id: str,
    residence_address_id: int,
    residence_data: QuintoAndarSchema,
) -> int:
    """
    Function responsible for create
        residence in database.

    Parameters:
        x_request_id: str
        residence_address_id: int
        residence_data: QuintoAndarSchema

    Returns:
        str
    """
    table_name = TableNameSchema()
    data = {
        "residenceCode": residence_data.residence_id,
        "source": residence_data.source,
        "urlSource": residence_data.link_apartment,
        "numberRooms": residence_data.number_rooms,
        "numberBathrooms": residence_data.number_bathrooms,
        "numberParkingSpace": residence_data.number_parking_space,
        "typeBuilding": residence_data.type_building,
        "sizeResidence": residence_data.size_residence,
        "ResidenceAddressId": residence_address_id,
    }
    residence = create(
        x_request_id=x_request_id, data=data, table_name=table_name.residence
    )

    return residence.get("id", None)
