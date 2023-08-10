import requests
import contextlib
from urllib.parse import urlencode
from urllib.request import urlopen
from bs4 import BeautifulSoup


def search_results(query):
    search_url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    links = []

    prefix = "/url?esrc=s&q=&rct=j&sa=U&url="
    for link in soup.find_all("a"):
        href = link.get("href")
        if href and href.startswith(prefix):
            # Extract the actual URL from the href parameter
            url = href[len(prefix):].split("&")[0]
            links.append(url)

    return links[:3]


def shorten_url(urls):
    small_urls = []
    for url in urls:
        request_url = ("http://tinyurl.com/api-create.php?" + urlencode({"url":url}))
        with contextlib.closing(urlopen(request_url)) as response:
            small_urls.append(response.read().decode("utf-8"))
	
    return small_urls


def main(prompt):
    links = search_results(prompt)
    return shorten_url(links)


if __name__ == "__main__":
    main()