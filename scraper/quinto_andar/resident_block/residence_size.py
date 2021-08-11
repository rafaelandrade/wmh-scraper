import re

from helpers.error_handler.main import error_handler


def residence_size(uuid: str, driver) -> int:
    """
        Function responsible for return the size of the residence.

        Parameters:
        -----------
                uuid: unique id
                driver: google chrome instance
    Returns:
        int: size of residence
    """
    print("Procurando pela numero de quartos")
    try:
        print("começando emmm....")
        size_residence_data = driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/main/section/div/div[1]/div/div[2]/div/div[1]/div/div/span'
        )

        if size_residence_data:
            print(
                f"{uuid} - Encontrado tamanho do quarto"
            )

            size_residence = size_residence_data.text
            size_residence = re.findall(r'\d+', size_residence)[0]
            return int(size_residence)
    except Exception as exception:
        error_handler(uuid=uuid, exception=exception)
