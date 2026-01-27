from curl_cffi import requests
import cloudscraper
from bs4 import BeautifulSoup



def get_response(url):

    scraper = cloudscraper.create_scraper(
        browser={
            'browser': 'chrome',
            'platform': 'windows',
            'mobile': False
        }
    )

    cookies = {
        "cf_clearance": "твой_cf_clearance_сюда_______очень_длинный",
        "__cf_bm": "тут_тоже_если_есть",
        # другие куки, если они есть
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'ru,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
    }




    try:
        r = requests.get(url, headers=headers, cookies=cookies, timeout=15)
        r.raise_for_status()
    #     response = requests.get(url, impersonate="chrome", timeout=10)
    #     response.raise_for_status()

        return r
    except requests.RequestsError as e:
        print(f"Ошибка запроса: {e}")


def get_visible_text(soup):
    for tag in soup(["script", "style", "head", "title", "meta", "[document]"]):
        tag.decompose()

    text = soup.get_text(separator="\n", strip=True)

    lines = [line.strip() for line in text.splitlines() if line.strip()]
    raise RuntimeError(text)
    return "\n".join(lines)


def get_nicks_for_name(name):
    url = f"https://ru.nickfinder.com/{name}"
    response = get_response(url)

    soup = BeautifulSoup(response.text, "html.parser")

    clean_text = get_visible_text(soup)
    start_index = clean_text.find("Генератор ников для")
    end_index = clean_text.find("Уже скопировано")

    return clean_text[start_index:end_index - 1].split('\n')[1:]