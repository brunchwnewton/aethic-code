"""
Scrape all "versus" matchup links from the Carnivora.net Interspecific Conflict Directory.
Handles pagination — the thread spans many pages.

Requirements:
    pip install beautifulsoup4 requests

Usage (two modes):

  MODE 1 — Parse locally saved HTML files (most reliable):
    1. Open the page in your browser:
       https://carnivora.net/interspecific-conflict-directory-t37.html
    2. Right-click → "Save As..." → save as "page.html"
       IMPORTANT: If you see pagination at the bottom (Page 1, 2, 3...),
       save EACH page and pass them all:
         python scrape_versus_links.py page1.html page2.html page3.html ...
       Or put all saved .html files in a folder:
         python scrape_versus_links.py pages_folder/

  MODE 2 — Auto-crawl all pages from the web:
    python scrape_versus_links.py
"""

import sys
import os
import re
import time
from bs4 import BeautifulSoup

OUTPUT_FILE = "versus_links.txt"
BASE_URL = "https://carnivora.net"
START_URL = f"{BASE_URL}/interspecific-conflict-directory-t37.html"

# Forum navigation / utility pages to exclude
EXCLUDE_PATTERNS = [
    "ucp.php",
    "search.php",
    "viewforum.php",
    "memberlist.php",
    "posting.php",
    "report.php",
    "mcp.php",
    "faq.php",
    "feed.php",
    "?sid=",
    "&sid=",
    "interspecific-conflict-f8",
    "zoology-f3",
    "interspecific-conflict-directory-t37",  # the directory page itself
    "#",
    "javascript:",
]


def is_matchup_link(href: str) -> bool:
    """Return True only for actual versus matchup thread links."""
    href_lower = href.lower()

    # Must be a carnivora.net or tapatalk carnivoraforum link
    if "carnivora.net" not in href_lower and "tapatalk.com/groups/carnivoraforum" not in href_lower:
        return False

    # Exclude forum navigation / utility pages
    for pattern in EXCLUDE_PATTERNS:
        if pattern in href_lower:
            return False

    return True


def extract_links(html: str) -> list[str]:
    """Extract all versus matchup links from a single page's HTML."""
    soup = BeautifulSoup(html, "html.parser")

    links = []

    # Method 1: <li> > <a> tags (primary structure for matchup links)
    for li in soup.find_all("li"):
        for a_tag in li.find_all("a", href=True):
            href = a_tag["href"].replace("&amp;", "&")
            if is_matchup_link(href):
                links.append(href)

    # Method 2: any <a class="postlink"> not already found
    for a_tag in soup.find_all("a", class_="postlink", href=True):
        href = a_tag["href"].replace("&amp;", "&")
        if is_matchup_link(href) and href not in links:
            links.append(href)

    # Method 3: regex fallback
    if not links:
        pattern = r'href="(https?://(?:carnivora\.net|www\.tapatalk\.com/groups/carnivoraforum)/[^"]+)"'
        for href in re.findall(pattern, html):
            if is_matchup_link(href):
                links.append(href)

    return links


def find_pagination_urls(html: str) -> list[str]:
    """Find all pagination page URLs from the thread."""
    soup = BeautifulSoup(html, "html.parser")
    page_urls = set()

    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"].replace("&amp;", "&")

        if re.search(r't37-s\d+\.html', href):
            if href.startswith("/"):
                href = BASE_URL + href
            elif not href.startswith("http"):
                href = BASE_URL + "/" + href
            page_urls.add(href)

        if "t=37" in href and "start=" in href:
            if href.startswith("/"):
                href = BASE_URL + href
            elif not href.startswith("http"):
                href = BASE_URL + "/" + href
            page_urls.add(href)

    return sorted(page_urls)


def fetch_html(url: str, session) -> str:
    """Fetch a single page."""
    resp = session.get(url, timeout=30)
    resp.raise_for_status()
    return resp.text


def crawl_all_pages():
    """Fetch page 1, discover all pagination URLs, then crawl them all."""
    import requests

    session = requests.Session()
    session.headers.update({
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    })

    print(f"Fetching page 1: {START_URL}")
    html = fetch_html(START_URL, session)
    all_links = extract_links(html)
    print(f"  → {len(all_links)} matchup links found on page 1")

    page_urls = find_pagination_urls(html)
    print(f"Found {len(page_urls)} additional pages to crawl")

    for i, page_url in enumerate(page_urls, start=2):
        print(f"Fetching page {i}/{len(page_urls)+1}: {page_url}")
        time.sleep(1)
        try:
            html = fetch_html(page_url, session)
            new_links = extract_links(html)
            all_links.extend(new_links)
            print(f"  → {len(new_links)} matchup links found")
        except Exception as e:
            print(f"  → Error: {e}")

    return all_links


def parse_local_files(paths: list[str]) -> list[str]:
    """Parse one or more local HTML files or all .html files in a folder."""
    all_links = []
    files = []

    for path in paths:
        if os.path.isdir(path):
            for fname in sorted(os.listdir(path)):
                if fname.lower().endswith((".html", ".htm")):
                    files.append(os.path.join(path, fname))
        else:
            files.append(path)

    for filepath in files:
        print(f"Reading: {filepath}")
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            html = f.read()
        new_links = extract_links(html)
        all_links.extend(new_links)
        print(f"  → {len(new_links)} matchup links found")

    return all_links


def main():
    if len(sys.argv) > 1:
        all_links = parse_local_files(sys.argv[1:])
    else:
        all_links = crawl_all_pages()

    # Deduplicate preserving order
    seen = set()
    unique = []
    for link in all_links:
        if link not in seen:
            seen.add(link)
            unique.append(link)

    if not unique:
        print("\nNo links found! Try saving all pages locally and using:")
        print(f"  python {sys.argv[0]} page1.html page2.html ...")
        return

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for link in unique:
            f.write(link + "\n")

    print(f"\nDone! Found {len(unique)} unique versus matchup links across all pages.")
    print(f"Saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
