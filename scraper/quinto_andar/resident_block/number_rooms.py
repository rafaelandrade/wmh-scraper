import re

from helpers.error_handler.main import error_handler


def number_of_rooms(uuid: str, driver) -> int:
    """
        Function responsible for return number of rooms.

        Parameters:
        -----------
                uuid: unique id
                driver: google chrome instance
    Returns:
        Bool <True or False>
    """
    print("Procurando pela numero de quartos")
    try:
        print("começando emmm....")
        number_rooms_data = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/main/section/div/div[1]/div/div[2]/div/div[2]/div/div"
        )

        if number_rooms_data:
            print(f"{uuid} - Encontrado info sobre numero de quartos")

            number_rooms = number_rooms_data.text
            number_rooms = re.findall(r"\d+", number_rooms)[0]
            return int(number_rooms)
    except Exception as exception:
        error_handler(uuid=uuid, exception=exception)
