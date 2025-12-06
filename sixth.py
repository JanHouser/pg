import sys
import requests
import re


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

    # Regulární výraz pro nalezení href atributu bez ohledu na pořadí atributů
    pattern = r'<a\s+[^>]*href=["\']([^"\']+)["\']'
    hrefs = re.findall(pattern, html, re.IGNORECASE)

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        odkazy = download_url_and_get_all_hrefs(url)
        for odkaz in odkazy:
            print(f'"{odkaz}"')
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
