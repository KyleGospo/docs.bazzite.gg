import re

from bs4 import BeautifulSoup, Tag
from mkdocs.structure.pages import Page

IMG_SIZED_RE = r"\|(\d+)x(\d+)(?:.*?(\d+)%)?"
"""Used to get width, height from `text|WIDTHxHEIGHT`"""


def on_page_content(html: str, page: Page, config, files):
    soup = BeautifulSoup(html, "html.parser")

    for img in soup.find_all(name="img", alt=True):
        if not isinstance(img, Tag):
            continue
        alt = str(img["alt"])
        m = re.search(IMG_SIZED_RE, alt, flags=re.M)
        if m:
            width, height, multi = m.group(1, 2, 3)
            multi = int(multi) / 100 if multi else 1
            width = int(width) * multi
            height = int(height) * multi
            img["style"] = f"width: {width}px; max-height: {height}px;"

    return str(soup)
