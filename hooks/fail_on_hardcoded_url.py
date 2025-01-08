import re

from mkdocs import plugins
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.pages import Page

pattern = r"\(https?:\/\/docs\.bazzite\.gg\/"


@plugins.event_priority(100)
def on_page_markdown(markdown: str, page: Page, config: MkDocsConfig, files):
    for line_n, line in enumerate(markdown.splitlines()):
        if match := re.search(pattern, line):
            raise ValueError(
                "Hardcoded URL found in markdown: ",
                page.file,
                f"line {line_n}:{match.start()}",
                line,
            )
