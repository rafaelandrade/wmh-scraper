def finish_session(driver) -> None:
    """Function responsible for finish a respective session.

    Parameters:
            uuid: Unique id.
            driver: Google Chrome instance.

    Returns:
            void
    """
    print("Finishing session...")
    driver.quit()
