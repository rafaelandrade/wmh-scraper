from schemas.QuintoAndarSchema import QuintoAndarSchema

from street_name import street_view


def get_resident_block_data(uuid: str, driver):
    """Function responsible for have functions to get data
        of specific building in homepage.

        Parameters:
            uuid: Str
            driver: Google Chrome instance

        Returns:
            any
    """
    quinto_andar_data = QuintoAndarSchema()

    quinto_andar_data.street_name = street_view(uuid=uuid, driver=driver)