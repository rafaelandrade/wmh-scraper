
def get_link_of_resident_block(uuid, driver) -> classmethod:
    """Function responsible for get link of one of blocks in QuintoAndar
        homepage.

        Parameters:
            uuid: UniqueId
            driver: Google Chrome instance

        Returns
            Link <str>
    """
    print("Iniciando o processo de pegar o link")

    link = driver.find_element_by_xpath('/html/body/div[1]/div/main'
                                        '/section[2]/div[2]/div/div[1]/div[3]/div[1]/div/a')
    return link if link else None
