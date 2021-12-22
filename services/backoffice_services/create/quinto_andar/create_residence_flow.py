from schemas.QuintoAndarSchema import QuintoAndarSchema
from services.backoffice_services.create.quinto_andar.create_residence_address import (
    create_residence_address,
)
from services.backoffice_services.create.quinto_andar.create_residence import (
    create_residence,
)
from services.backoffice_services.create.quinto_andar.create_residence_values import (
    create_residence_values,
)
from services.backoffice_services.create.quinto_andar.create_residence_features import (
    create_residence_features,
)


def creation_residence_data(
    x_request_id: str, residence_data: QuintoAndarSchema
) -> None:
    """
    Function responsible for
        create all data from residence.

    Parameters:
        x_request_id: str
        residence_data: QuintoAndarSchema

    Returns:
        None
    """
    residence_address_id = create_residence_address(
        x_request_id=x_request_id, residence_data=residence_data
    )
    residence_id = create_residence(
        x_request_id=x_request_id,
        residence_address_id=residence_address_id,
        residence_data=residence_data,
    )
    create_residence_values(
        x_request_id=x_request_id,
        residence_id=residence_id,
        residence_data=residence_data,
    )
    create_residence_features(
        x_request_id=x_request_id,
        residence_id=residence_id,
        residence_data=residence_data,
    )
