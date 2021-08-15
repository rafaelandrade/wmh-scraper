def verification_string_has_digit(uuid: str, text: str) -> bool:
    """
    Function responsible for verify if text has an digit or not.

    Parameters:
    -----------
            uuid: unique id
            text: sentence that going to be verified

    Returns:
    --------
        bool: True or False
    """
    print(f"{uuid} - Going to verify if text has digit")
    if text is None:
        return False
    return any(map(str.isdigit, text))
