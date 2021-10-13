from selenium.webdriver.common.keys import Keys


def open_new_tab(link):
    """
    Function responsible for open new tab
        base on link

    Parameters:
        link

    Returns:
        void
    """
    print("Abrindo a nova aba do link")
    link.send_keys(Keys.CONTROL + Keys.RETURN)
