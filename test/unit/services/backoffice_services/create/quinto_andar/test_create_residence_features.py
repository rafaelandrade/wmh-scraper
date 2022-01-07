from app.services.backoffice_services.create.quinto_andar.create_residence_features import (
    deal_with_feature,
)


def test_create_residence_features(mocker):
    """
    Should return 2 of number of times that
        create going to be called.
    """
    features = {"flag_pet": True, "flag_furniture": False}
    mocker_create = mocker.patch(
        "app.services.backoffice_services.create.quinto_andar."
        "create_residence_features.create",
        return_value=None,
    )

    assert (
        deal_with_feature(features=features, x_request_id="", residence_id=1)
        is None
    )
    assert mocker_create.call_count == 2


def test_create_residence_features_error_handler(mocker):
    """
    Should call error_handler
        in case of something wrong
        happen.
    """
    features = []
    mocker_error_handler = mocker.patch(
        "app.services.backoffice_services.create.quinto_andar."
        "create_residence_features.error_handler",
        return_value=None,
    )

    assert (
        deal_with_feature(features=features, x_request_id="", residence_id=1)
        is None
    )
    assert mocker_error_handler.call_count == 1
