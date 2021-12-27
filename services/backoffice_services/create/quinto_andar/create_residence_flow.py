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
    deal_with_feature,
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

    Notes:
        Function deal_with_feature is responsible for
            receive each different features and create
            respectively to each residence.
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
    features = {
        "petFlag": residence_data.pet_flag,
        "metroFlag": residence_data.metro_flag,
        "furnitureFlag": residence_data.furniture_flag,
    }

    deal_with_feature(
        features=features, x_request_id=x_request_id, residence_id=residence_id
    )
