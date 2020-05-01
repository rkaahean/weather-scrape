
def format_url(url, city, api):
    """
    Simple Url formatting function.
    :param url: Base Url in constants.py
    :param city:
    :param api:
    :return: Finished URL ready for querying
    """
    return url.format(city, api)
