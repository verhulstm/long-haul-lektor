import sys
from setuptools import setup

from longhaullektor.settings import *

assert sys.version_info >= MINIMUM_PYTHON_VERSION

setup(
    name="long-haul-jekyll",
    version=VERSION,
    description="long haul jekyll",
    url="https://github.com/verhulstm/long-haul-jekyll",
    author="Terminal Labs",
    author_email="michael@terminallabs.com",
    license="see LICENSE file",
    packages=["longhaullektor"],
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "setuptools",
        "Lektor",
        "click",
        "black",
        "flake8",
    ],
    entry_points="""
        [console_scripts]
        longhaullektor=longhaullektor.__main__:main
    """,
)
