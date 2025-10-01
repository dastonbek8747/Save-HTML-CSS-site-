# save_page.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os

def sanitize_filename(name: str) -> str:
    # oddiy filename safe qilish
    return "".join(c for c in name if c.isalnum() or c in "-._").rstrip("._-") or "file"

def save_page_with_css(url: str, out_dir: str = "output"):
    os.makedirs(out_dir, exist_ok=True)
    css_dir = os.path.join(out_dir, "css")
    os.makedirs(css_dir, exist_ok=True)

    resp = requests.get(url)
    resp.raise_for_status()
    html = resp.text

    soup = BeautifulSoup(html, "html.parser")

    # topilgan CSS linklarini yuklab, href'ni lokalga o'zgartirish
    for link in soup.find_all("link", rel=lambda v: v and "stylesheet" in v):
        href = link.get("href")
        if not href:
            continue
        # to'liq URL hosil qilish
        css_url = href if href.startswith("http") else urljoin(url, href)
        try:
            r = requests.get(css_url)
            r.raise_for_status()
            # nom olish (query paramlarni olib tashlab)
            parsed = urlparse(css_url)
            name = os.path.basename(parsed.path) or "style.css"
            safe_name = sanitize_filename(name)
            local_path = os.path.join("css", safe_name)
            # saqlash
            with open(os.path.join(out_dir, local_path), "w", encoding="utf-8") as f:
                f.write(r.text)
            # HTMLdagi linkni lokal yo'lga o'zgartirish
            link['href'] = local_path
            print(f"Saved CSS: {css_url} -> {local_path}")
        except Exception as e:
            print(f"Failed to download CSS {css_url}: {e}")

    # optionally: saqlashdan oldin inline <script> yoki <link rel="preload"> larni qo'ldan o'tkazish mumkin

    # HTMLni saqlash (prettify yoki original)
    out_file = os.path.join(out_dir, "page.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(str(soup))  # yoki soup.prettify()
    print(f"Saved HTML: {out_file}")

if __name__ == "__main__":
    url = input("Sahifa URL kiriting: ")
    save_page_with_css(url, out_dir="saved_page")
