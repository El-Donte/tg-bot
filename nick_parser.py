import requests
import cloudscraper
from bs4 import BeautifulSoup


def get_response(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'ru',
        'Cache-Control': 'max-age=0',
        'Host': 'ru.nickfinder.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/140.0.0.0 YaBrowser/25.10.0.0 Safari/537.36'
    }

    cookies = {
        'PHPSESSID' : 'b38pvn1f7rdn0ooih5jq94ft56'
    }

    scraper = cloudscraper.create_scraper(
        browser={
            'browser': 'chrome',
            'platform': 'windows',
            'mobile': False
        },
        cookies = cookies,
        headers = headers,
    )

    try:
        response = scraper.get(url, headers=headers)
        response.raise_for_status()

        return response
    except requests.RequestException as e:
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