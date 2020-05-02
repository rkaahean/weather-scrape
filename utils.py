
def format_url(url, city, api):
    """
    Simple Url formatting function.
    :param url: Base Url in constants.py
    :param city:
    :param api:
    :return: Finished URL ready for querying
    """
    return "http://" + url.format(city, api)


WEATHER_PARAMS = {
    'main': ['temp', 'temp_min', 'temp_max', 'humidity', 'pressure'],
    'weather': ['description']
}

