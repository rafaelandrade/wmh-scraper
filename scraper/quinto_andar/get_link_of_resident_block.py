from selenium.common.exceptions import NoSuchElementException


def get_link_of_resident_block(
    uuid, div_number_row: int, div_number_column: int, driver
) -> classmethod:
    """
    Function responsible for get link of one of blocks in QuintoAndar
        homepage.

        Parameters:
            uuid: UniqueId
            div_number_row: Number of the block in row in the page
            div_number_column: Number of the block in column in page
            driver: Google Chrome instance

        Returns
            Link <str>
    """
    print(uuid)
    print("Iniciando o processo de pegar o link")
    print(
        f"\n\n "
        f"--- COMEÇANDO COM LINHA {div_number_row} "
        f"--- COLUNA {div_number_column}"
    )
    try:
        link = driver.find_element_by_xpath(
            "/html/body/div[1]/div/main"
            "/section[2]/div[2]/div"
            f"/div[1]/div[{div_number_row}]/div[{div_number_column}]/div/a"
        )
        return link if link else None
    except (AttributeError, NoSuchElementException) as exception:
        print(f"ERROR IN GET A LINK {exception}")
