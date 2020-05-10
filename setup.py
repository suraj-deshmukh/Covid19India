import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Covid19India",
    version="0.0.1",
    description="A Python Library to get India's Total Covid patients stats as well State wise stats",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/suraj-deshmukh/Covid19India",
    author="Suraj Deshmukh",
    author_email="surajdeshmukh96@gmail.com",
    license="MIT LICENSE",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["Covid19India"],
    include_package_data=True,
    install_requires=["requests", "beautifulsoup4"],
)
