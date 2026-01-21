import requests
from bs4 import BeautifulSoup


def get_response(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        print(f"Ошибка запроса: {e}")
        exit()


def get_visible_text(soup):
    for tag in soup(["script", "style", "head", "title", "meta", "[document]"]):
        tag.decompose()

    text = soup.get_text(separator="\n", strip=True)

    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)


def get_nicks_for_name(name):
    url = f"https://ru.nickfinder.com/{name}"
    response = get_response(url)

    soup = BeautifulSoup(response.text, "html.parser")

    clean_text = get_visible_text(soup)
    start_index = clean_text.find("Генератор ников для")
    end_index = clean_text.find("Уже скопировано")

    return clean_text[start_index:end_index - 1].split('\n')[1:]