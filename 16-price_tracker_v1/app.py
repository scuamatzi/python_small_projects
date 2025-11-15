import requests
from bs4 import BeautifulSoup
import unicodedata
# from send_mail import send_mail

# PENDING
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5",
}


def get_product_info(url):
    page = requests.get(url, headers=HEADERS)
    print(page)
    soup = BeautifulSoup(page.content, features="lxml")
    print(soup)

    try:
        title = soup.find(id="productTitle").get_text().strip()
        print(f"Title: {title}")
        price_str = soup.find(id="priceblock_ourprice").get_text()
        print(f"price_str: {price_str}")
    except:
        return None, None, None

    try:
        soup.select("#availability .a-color-success")[0].get_text().strip()
        available = True
    except:
        available = False

    try:
        price = unicodedata.normilize("NFKD", price_str)
        price = price.replace(",", ".").replace("$", "")
        price = float(price)
    except:
        return None, None, None

    return title, price, available


if __name__ == "__main__":
    # url = "https://www.amazon.com.mx/dp/B094YT8F6X/"
    url = "https://www.amazon.com.mx/dp/B094YT8F6X/?coliid=I1KX5RGIK4DY20&colid=3RVUXHYQRQ45&psc=1&ref_=list_c_wl_lv_ov_lig_dp_it"
    products = [(url, 800)]

    products_below_limit = []
    for product_url, limit in products:
        title, price, available = get_product_info(product_url)
        if title is not None and price < limit and available:
            products_below_limit.append(url, title, price)

    if products_below_limit:
        message = "Subject: Price below limit!\n\n"
        message += "Your tracked products are below the given limit!\n\n"

        for url, title, price in products_below_limit:
            message += f"{title}\n"
            message += f"Price: {price}\n"
            message += f"{url}\n\n"

        print(message)
