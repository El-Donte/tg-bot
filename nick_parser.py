import requests
import cloudscraper
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright



async def get_response(url):
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
        }
    )



    try:
        # response = scraper.get(url, headers=headers, cookies=cookies)
        # response.raise_for_status()

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                viewport={'width': 1920, 'height': 1080},
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
                locale="ru-RU"
            )
            page = await context.new_page()

            await page.goto("https://ru.nickfinder.com/", wait_until="networkidle", timeout=45000)

            # ждём, пока Turnstile решится (обычно 3–15 сек)
            content = await page.content()

            # здесь можно уже парсить soup = BeautifulSoup(content, "lxml")

            await browser.close()

            return content
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