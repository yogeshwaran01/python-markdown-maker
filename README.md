<h1 align='center'>Python Markdown Maker</h1>

<p align="center">Python Objects for Markdown 
</p>Python Markdown maker use to write markdown documents in the Pythonic way

## Installation

```bash
$ git clone https://github.com/yogeshwaran01/python-markdown-maker/
$ cd python-markdown-maker/
$ python3 setup.py install
```

## Usage

| Elements     | Normal Markdown    | Pythonic Markdown                      |
| ------------ | ------------------ | -------------------------------------- |
| Headings     | `## Python`        | `headers('Python', level=3)`           |
| Images       | `![alt](source)`   | `image(src, alt)`                      |
| Links        | `[text](link)`     | `links(link, text)`                    |
| Bold         | `**Bold**`         | `styled_text(text, bold=True)`         |
| Italic       | `*Italic*`         | `styled_text(text, italic=True)`       |
| Striketrough | `~~text~~`         | `styled_text(text, strikethrough=True` |
| Inline code  | `some code`        | `inline_code("some code")`             |
| Blackquotes  | `> text are super` | `blockquotes('text are super')`        |

#### Code Blocks

```python

code_block("print('Hello World!')", lang='python')

```

#### UnOrdered List

```python

lists(['Python', 'Javascript', 'Go', 'PhP'])

```

```markdown
- Python
- Javascript
- Go
- PhP
```

#### Ordered List

```python

lists(['order', 'Python', 'Javascript', 'Go', 'PhP'])

```

```markdown
1. Python
2. Javascript
3. Go
4. PhP
```

#### Both Ordered & Unorder list

```python

lists([
    'Frontend',[
        'order', 'Html', 'Css', 'Javascript'
    ],
    'Backend',[
        'order', 'Python', 'Postgress'
    ]
])

```

```markdown
- Frontend 1. Html 2. Css 3. Javascript
- Backend 1. Python 2. Postgress
```

#### Tables

```python

t = Table(["Languages", "Uses"])
t.add_item("Python", "ML/AI")
t.add_item("Javascript", "Web Dev")
table = t.render()

```

```markdown
    Languages | Uses

--------- | ----
Python | ML/AI
Javascript | Web Dev
```

### Rendering

```python

from python_markdown_maker import *

ou = lists([
    'Frontend',[
        'order', 'Html', 'Css', 'Javascript'
    ],
    'Backend',[
        'order', 'Python', 'Postgress'
    ]
])

t = Table(["Languages", "Uses"])
t.add_item(["Python", "ML/AI"])
t.add_item(["Javascript", "Web Dev"])
table = t.render()

items = lists(['order', 'Python', 'Javascript', 'Go', 'PhP'])

md = Document()
md.write([ou, table, items])

with open('code.md', 'w') as file:
    md.render.save_as_md(file)
    # md.render.save_as_html(file)
    # md.render.to_html()
    # md.render.text


```
