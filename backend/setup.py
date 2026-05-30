import setuptools
from pathlib import Path
from setuptools import setup, find_packages

this_directory = Path(__file__).parent
readme_path = this_directory.parent / "README.md"

long_description = readme_path.read_text(encoding="utf-8")

__version__ = "0.0.0"

REPO_NAME = "Phishing url detection app"
AUHTOR_USER_NAME = "condonettercode"
SRC_REPO = "src" # Name of local package
AUHTOR_EMAIL = "siddhesh1199@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUHTOR_USER_NAME,
    author_email=AUHTOR_EMAIL,
    description="Phishing url detection app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)