from schemas.QuintoAndarSchema import QuintoAndarSchema
from schemas.TableNameSchema import TableNameSchema
from services.backoffice_services.create.create import create
from helpers.logger.console_logger import log


def create_residence_features(
    x_request_id: str, residence_id: int, residence_data: QuintoAndarSchema
) -> None:
    """
    Function responsible for create residence feature data.

    Parameters:
        x_request_id: str
        residence_id: int
        residence_data: QuintoAndarSchema

    Returns:
        None
    """
    table_name = TableNameSchema()

    pet_flat = QuintoAndarSchema.pet_flag
    data = {
        "ResidenceId": residence_id,
        "key": QuintoAndarSchema.name(pet_flat),
        "value": residence_data.pet_flag,
    }
    residence_feature = create(
        x_request_id=x_request_id,
        data=data,
        table_name=table_name.residence_values,
    )
    log(
        x_request_id=x_request_id,
        message=f"Inserted in database the follow residence values {residence_feature}...",
    )
