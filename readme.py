from python_markdown_maker import *

readme = Document()

head_1 = aligned_header("Python Markdown Maker", level=1, align='center')
quotes = aligned_text("Python Objects for Markdown \n", align='center')

explantion = "Python Markdown maker use to write markdown documents in the Pythonic way" + 2 * "\n"

t = Table(["Elements","Normal Markdown", "Pythonic Markdown"])
t.add_item([
    "Headings",
    inline_code('## Python'), inline_code("headers('Python', level=3)")
])
t.add_item([
    "Images",
    inline_code("![alt](source)"),
    inline_code("image(src, alt)")
])
t.add_item([
    "Links",
    inline_code("[text](link)"),
    inline_code("links(link, text)")
])
t.add_item([
    "Bold",
    inline_code("**Bold**"),
    inline_code("styled_text(text, bold=True)")
])
t.add_item([
    "Italic",
    inline_code("*Italic*"),
    inline_code("styled_text(text, italic=True)")
])
t.add_item([
    "Striketrough",
    inline_code("~~text~~"),
    inline_code("styled_text(text, strikethrough=True")
])
t.add_item([
    "Inline code",
    inline_code("`some code`"),
    inline_code('inline_code("some code")')
])
t.add_item([
    "Blackquotes",
    inline_code("> text are super"),
    inline_code("blockquotes('text are super')")
])

head_2 = headers("Code Blocks", level=4) 
text_c = """
code_block("print('Hello World!')", lang='python')
"""

head_3 = headers("Tables", level=4)
text_d = """
t = Table(["Languages", "Uses"])
t.add_item("Python", "ML/AI")
t.add_item("Javascript", "Web Dev")
table = t.render()
"""

head_4 = headers("UnOrdered List", level=4)
text_e = """
lists(['Python', 'Javascript', 'Go', 'PhP'])
"""

head_5 = headers("Ordered List", level=4)
text_f = """
lists(['order', 'Python', 'Javascript', 'Go', 'PhP'])
"""

head_6 = headers("Both Ordered & Unorder list", level=4)
text_g = """
lists([
    'Frontend',[
        'order', 'Html', 'Css', 'Javascript'
    ],
    'Backend',[
        'order', 'Python', 'Postgress'
    ]
])
"""

ou1 = """
* Frontend
        1. Html
        2. Css
        3. Javascript
* Backend
        1. Python
        2. Postgress"""

ou2 = """Languages | Uses
--------- | ----
Python | ML/AI
Javascript | Web Dev"""

ou3 = """
* Python
* Javascript
* Go
* PhP
"""

ou4 = """
1. Python
2. Javascript
3. Go
4. PhP
"""

fines = """
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

"""

readme.write(
    [head_1, quotes, explantion, t.render(), head_2, code_block(text_c, lang='python'), 
    head_4, code_block(text_e, lang='python'),
    code_block(ou3, lang='markdown'),
    head_5, code_block(text_f, lang='python'),
    code_block(ou4, lang='markdown'),
    head_6, code_block(text_g, lang='python'),code_block(ou1, lang='markdown'),
    head_3, code_block(text_d, lang='python'),code_block(ou2, lang='markdown'),
    headers("Rendering", level=3),
    code_block(fines, lang='python')],
)

a = open('README.md', 'w')
print(readme.render.text)
readme.render.save_as_md(a)
