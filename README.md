# Save Webpage (HTML + CSS)

> A script that saves a web page together with its HTML and CSS using BeautifulSoup.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)


## What It Does

Downloads a page, extracts the HTML, finds linked stylesheets and saves everything into `saved_page/` with a rewritten CSS path so the page opens correctly offline.

## Quick Start

```bash
git clone https://github.com/dastonbek8747/save-webpage-html-css.git
cd save-webpage-html-css
python -m venv .venv && source .venv/bin/activate
pip install beautifulsoup4 requests
python main.py
```

## Project Structure

```
main.py
saved_page/
├── page.html
└── css/app.css
```

## License

MIT © 2026 Doston Sultonov.
