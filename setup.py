import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-markdown-maker",
    version="1.0",
    license='MIT',
    author="Yogeshwaran R",
    author_email="yogeshin247@gmail.com",
    description="Write Markdown in Pythonic way",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yogeshwaran01/python-markdown-maker",
    packages=setuptools.find_packages(),
    download_url="https://github.com/yogeshwaran01/python-markdown-maker/archive/refs/heads/master.zip",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)