import requests


def get_niedersachsen_wiki_page():
    wikipedia_niedersachsen_page = requests.get(
        'https://de.wikipedia.org/wiki/Liste_der_St%C3%A4dte_und_Gemeinden_in_Niedersachsen')
    return str(wikipedia_niedersachsen_page.content, encoding='utf-8')
