from faker import Faker

from scraper.quinto_andar.resident_block.main import get_resident_block_data
from schemas.QuintoAndarSchema import QuintoAndarSchema

fake = Faker()


def test_get_resident_block_data(mocker):
    """Should return None after recursive scraper logic finished"""

    class Driver:
        current_url = "www.google.com.br"

    driver = Driver()
    quinto_andar_schema = QuintoAndarSchema()

    mock_localization_data = mocker.patch(
        "scraper.quinto_andar.resident_block.main.resident_localization_data",
        return_value=["Rua Potatoes", "Potatoes", "São Potatoes"],
    )
    mock_number_rooms = mocker.patch(
        "scraper.quinto_andar.resident_block.main.number_of_rooms",
        return_value=2,
    )
    mock_number_bathroom = mocker.patch(
        "scraper.quinto_andar.resident_block.main.get_number_bathrooms",
        return_value=1,
    )
    mock_get_number_parking_space = mocker.patch(
        "scraper.quinto_andar.resident_block.main.get_number_parking_space",
        return_value=0,
    )
    mock_pet_flag = mocker.patch(
        "scraper.quinto_andar.resident_block.main.pet_flag", return_value=True
    )
    mock_get_furniture_flag = mocker.patch(
        "scraper.quinto_andar.resident_block.main.get_furniture_flag",
        return_value=False,
    )
    mock_residence_size = mocker.patch(
        "scraper.quinto_andar.resident_block.main.residence_size",
        return_value=123,
    )
    mock_get_type_residence = mocker.patch(
        "scraper.quinto_andar.resident_block.main.get_type_residence",
        return_value="house",
    )
    mock_rent_values = {
        "rent_without_taxes": 12121,
        "condominium_tax": 1212,
        "house_tax": 2,
        "fire_insurance": 1231,
        "service_tax": 121,
        "total_rent_value": 22222,
    }
    mock_get_rent_values = mocker.patch(
        "scraper.quinto_andar.resident_block.main.get_rent_values",
        return_value=mock_rent_values,
    )
    mock_get_residence_id = mocker.patch(
        "scraper.quinto_andar.resident_block.main.get_residence_id",
        return_value=22,
    )

    response = get_resident_block_data(
        x_request_id="", quinto_andar_data=quinto_andar_schema, driver=driver
    )
    assert response is not None
    assert type(response) == QuintoAndarSchema
    assert response.link_apartment == "www.google.com.br"
    assert mock_localization_data.call_count == 1
    assert mock_number_rooms.call_count == 1
    assert mock_number_bathroom.call_count == 1
    assert mock_get_number_parking_space.call_count == 1
    assert mock_pet_flag.call_count == 1
    assert mock_residence_size.call_count == 1
    assert mock_get_type_residence.call_count == 1
    assert mock_get_furniture_flag.call_count == 1
    assert mock_get_rent_values.call_count == 1
    assert mock_get_residence_id.call_count == 1
