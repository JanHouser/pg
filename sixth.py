import sys
import requests


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"chybný status kód: {response.status_code}")
    html = response.text

    hrefs = []
    start = 0
    while True:
        start_link = html.find('<a href="', start)
        if start_link == -1:
            break

        start_quote = start_link + len('<a href="')

        end_quote = html.find('"', start_quote)
        if end_quote == -1:
            break

        link = html[start_quote:end_quote]
        hrefs.append(link)

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        odkazy = download_url_and_get_all_hrefs(url)
        for odkaz in odkazy:
            print(f'"{odkaz}"')
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
