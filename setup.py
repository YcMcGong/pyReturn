import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyReturn",
    version="0.0.1",
    author="Yicong Gong",
    author_email="gongyc3@gmail.com",
    description="A python package to provide auto-formatted json response for web services.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YcMcGong/pyReturn",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
