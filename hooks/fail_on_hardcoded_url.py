import re
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.pages import Page


pattern = r"[^[]\(https?:\/\/docs\.bazzite\.gg"


def on_page_markdown(markdown: str, page: Page, config: MkDocsConfig, files):
    if (_match := re.search(pattern, markdown)) is not None:
        raise ValueError("Hardcoded URL found in markdown: ", page.file, _match.group())
