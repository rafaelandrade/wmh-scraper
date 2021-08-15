from schemas.QuintoAndarSchema import QuintoAndarSchema
from scraper.quinto_andar.resident_block.furnisished_residence_flag import \
    get_furniture_flag
from scraper.quinto_andar.resident_block.metro_flag import get_metro_flag
from scraper.quinto_andar.resident_block.number_bathrooms import \
    get_number_bathrooms
from scraper.quinto_andar.resident_block.number_parking_space import \
    get_number_parking_space
from scraper.quinto_andar.resident_block.number_rooms import number_of_rooms
from scraper.quinto_andar.resident_block.pet_residence_flag import pet_flag
from scraper.quinto_andar.resident_block.residence_rent_values import \
    get_rent_values
from scraper.quinto_andar.resident_block.residence_size import residence_size
from scraper.quinto_andar.resident_block.resident_localization_data import \
    resident_localization_data
from scraper.quinto_andar.resident_block.type_of_residence import \
    get_type_residence


def get_resident_block_data(uuid: str, quinto_andar_data: QuintoAndarSchema, driver):
    """Function responsible for have functions to get data
    of specific building in homepage.

    Parameters:
        uuid: Str
        quinto_andar_data: QuintoAndarSchema
        driver: Google Chrome instance

    Returns:
        any
    """
    localization_data = resident_localization_data(uuid=uuid, driver=driver)

    quinto_andar_data.street_name = localization_data[0]
    quinto_andar_data.district_name = localization_data[1]
    quinto_andar_data.state_name = localization_data[2]

    quinto_andar_data.number_rooms = number_of_rooms(uuid=uuid, driver=driver)

    quinto_andar_data.number_bathrooms = get_number_bathrooms(uuid=uuid, driver=driver)
    quinto_andar_data.number_parking_space = get_number_parking_space(
        uuid=uuid, driver=driver
    )
    quinto_andar_data.pet_flag = pet_flag(uuid=uuid, driver=driver)
    quinto_andar_data.metro_flag = get_metro_flag(uuid=uuid, driver=driver)
    quinto_andar_data.furniture_flag = get_furniture_flag(uuid=uuid, driver=driver)
    quinto_andar_data.size_residence = residence_size(uuid=uuid, driver=driver)
    quinto_andar_data.type_building = get_type_residence(uuid=uuid, driver=driver)

    rent_values = get_rent_values(uuid=uuid, driver=driver)

    quinto_andar_data.rent_price_without_tax = rent_values["rent_without_taxes"]
    quinto_andar_data.condominium_tax = rent_values["condominium_tax"]
    quinto_andar_data.house_tax = rent_values["house_tax"]
    quinto_andar_data.fire_insurance = rent_values["fire_insurance"]
    quinto_andar_data.service_tax = rent_values["service_tax"]
    quinto_andar_data.total_rent_price = rent_values["total_rent_value"]

    return quinto_andar_data
