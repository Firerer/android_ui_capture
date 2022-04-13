"""
   Modified from https://gist.github.com/dawand/7b4308d568c6b955b645dd7e707e5cf1
"""
import os
from urllib.parse import quote_plus

import cloudscraper
from bs4 import BeautifulSoup

from definitions import APK_DIR

scraper = cloudscraper.create_scraper(delay=1000)


def search(query):
    res = scraper.get(
        f"https://apkpure.com/search?q={quote_plus(query)}",
    ).text

    if "Cloudflare Ray ID" in res:
        print("Cloudflare protection could not be bypassed, trying again..")
        return

    soup = BeautifulSoup(res, "html.parser")
    search_result = soup.find("div", {"id": "search-res"}).find(
        "dl", {"class": "search-dl"}
    )
    app_tag = search_result.find("p", {"class": "search-title"}).find("a")
    download_link = "https://apkpure.com" + app_tag["href"]
    return download_link


def download(link, apk_dir=APK_DIR):
    res = scraper.get(f"{link}/download?from=details").text
    soup = BeautifulSoup(res, "html.parser").find("a", {"id": "download_link"})
    if soup["href"]:
        r = scraper.get(soup["href"], stream=True)

        filename = f"{link.split('/')[-1]}.apk"
        filepath = os.path.join(apk_dir, filename)
        with open(filepath, "wb") as file:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        return filepath

async def download_apk(app_id):
    download_link = await search(app_id)

    if download_link is not None:
        print(f"Downloading from {download_link}...")
        path = await download(download_link)
        print("Download from {download_link} completed!")
        return path
    else:
        print("No results")
