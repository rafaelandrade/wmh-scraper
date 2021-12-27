from schemas.TableNameSchema import TableNameSchema
from services.backoffice_services.create.create import create
from helpers.logger.console_logger import log
from helpers.error_handler.main import error_handler


def deal_with_feature(
    features: dict, x_request_id: str, residence_id: int
) -> dict:
    """
    Function responsible for deal
        with each feature and send
        to insert in database.

    Parameters:
        features: dict
        x_request_id: str
        residence_id: int

    Returns:
        dict
    """
    try:
        for feature in features.keys():
            create_residence_features(
                x_request_id=x_request_id,
                residence_id=residence_id,
                residence_feature_key=feature,
                residence_feature_value=features[feature],
            )
    except (
        AttributeError,
        IndexError,
        NotImplementedError,
        SyntaxError,
    ) as exception:
        error_handler(
            x_request_id=x_request_id,
            exception=exception,
            _msg="Exception occurred in deal with feature.",
        )


def create_residence_features(
    x_request_id: str,
    residence_id: int,
    residence_feature_key: str,
    residence_feature_value: any,
) -> None:
    """
    Function responsible for create residence feature data.

    Parameters:
        x_request_id: str
        residence_id: int
        residence_feature_key: str
        residence_feature_value: any

    Returns:
        None
    """
    table_name = TableNameSchema()

    data = {
        "ResidenceId": residence_id,
        "key": residence_feature_key,
        "value": str(residence_feature_value),
    }
    residence_feature = create(
        x_request_id=x_request_id,
        data=data,
        table_name=table_name.residence_features,
    )
    log(
        x_request_id=x_request_id,
        message=f"Inserted in database the follow residence values {residence_feature}...",
    )
