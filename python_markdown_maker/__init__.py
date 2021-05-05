import requests


def markdown_to_html(text: str) -> str:
    """ Function convert markdown to HTML """
    return requests.post("https://api.github.com/markdown", json={"text": text}).text


def headers(text: str, level: int) -> str:
    return level * "#" + f" {text}" + "\n"


def lists(list_item: list, k=0) -> str:
    code = list_item[0]
    struture = ""
    if code == "order":
        list_item = list_item[1:]
        count = 0
        for i in list_item:
            if isinstance(i, list):
                struture = struture + lists(i, k=k + 1)
            else:
                count = count + 1
                struture = struture + k * "\t" + str(count) + ". " + i + "\n"
        return struture
    else:
        for i in list_item:
            if isinstance(i, list):
                struture = struture + lists(i, k=k + 1)
            else:
                struture = struture + k * "\t" + "* " + i + "\n"
        return struture


def image(src: str, alt: str) -> str:

    return f"![{alt}]({src})" + "\n"


def links(link: str, text: str) -> str:

    return f"[{text}]({link})"


def styled_text(text: str, bold=False, italic=False, strikethrough=False):
    if bold:
        return f"**{text}**"
    if italic:
        return f"*{text}*"
    if strikethrough:
        return f"~~{text}~~"
    else:
        return text


def inline_code(text: str) -> str:
    return f"`{text}`"


def code_block(code: str, lang: str):
    return f"""```{lang}
    {code}
```\n"""


def blockquotes(text: str):
    return f"> {text} \n"


def task(text: str, checked: bool):
    if checked:
        return f"[x] {text}"
    return f"[ ] {text}"


class Table:
    def __init__(self, filednames):
        self.filednames = filednames
        self.all_items = []

    def add_item(self, item: list):
        self.all_items.append(item)

    def render(self):
        code = " | ".join(self.filednames) + "\n"
        line = " | ".join([j * "-" for j in [len(i) for i in self.filednames]]) + "\n"
        items = []
        for i in self.all_items:
            items.append(" | ".join(i))
        self.strcture = code + line + "\n".join(items)

        return self.strcture + "\n"


def collapsible(text: str, summary: str):
    return (
        f"""
<details>
  <summary>{summary}</summary>
  
{text}

</details>
"""
        + "\n"
    )


def aligned_header(text: str, level: int, align: str) -> str:
    return f"<h{level} align='{align}'>{text}</h{level}>" + "\n" + "\n"


def aligned_text(text: str, align: str) -> str:
    return f'<p align="{align}">{text}</p>'


def aligned_image(src: str, alt: str, align: str) -> str:
    return f'<p align="{align}"> <img alt="{align}" src="{src}"/> </p>' + "\n" + "\n"


class _render:
    def __init__(self, text):
        self.text = text

    def to_html(self):
        return markdown_to_html(self.text)

    def save_as_md(self, fp):
        fp.write(self.text)

    def save_as_html(self, fp):
        fp.write(self.to_html())


class Document:
    def __init__(self):
        self.document = ""

    @property
    def render(self):
        render_obj = _render(self.document)
        return render_obj

    def write(self, elements: list):
        self.document = "".join(elements)
