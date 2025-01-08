import re
import textwrap
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.pages import Page


pattern = r"\(https?:\/\/docs\.bazzite\.gg\/"


def on_page_markdown(markdown: str, page: Page, config: MkDocsConfig, files):
    for line_n, line in enumerate(markdown.splitlines()):
        if match := re.search(pattern, line):
            raise ValueError(
                "Hardcoded URL found in markdown: ",
                page.file,
                f"line {line_n}:{match.start()}",
                textwrap.TextWrapper().wrap(line),
            )
