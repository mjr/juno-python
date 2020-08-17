# -*- coding: utf-8 -*-
# import os
# import re
# from setuptools import setup, find_packages

__description__ = "Juno Python"
__long_description__ = "Python library for Juno API"

__author__ = "Manaia Junior"
__author_email__ = "manaiajr.23@gmail.com"


# testing_extras = [
#     "pytest",
#     "pytest-cov",
# ]


# def _find_version():
#     # filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), "juno/sdk.py")
#     # with open(filename) as f:
#     # data = f.read()

#     # match = re.search(r"VERSION = '(.+)'", data)
#     # return match.groups()[0]
#     return "2"


# __version__ = _find_version()

# install_requires = (
#     open(
#         os.path.join(os.path.abspath(os.path.dirname(__file__)), "requirements.txt"),
#         "r",
#         encoding="utf-8",
#     )
#     .read()
#     .strip()
#     .split("\n")
# )


# setup(
#     name="juno-python",
#     version="2",
#     author=__author__,
#     author_email=__author_email__,
#     packages=find_packages(exclude=["tests", "tests.*"]),
#     license="MIT",
#     description=__description__,
#     long_description=__long_description__,
#     url="https://github.com/mjr/juno-python",
#     keywords="Payment, juno",
#     include_package_data=True,
#     zip_safe=False,
#     install_requires=[
#         'requests >= 2.20; python_version >= "3.0"',
#         'requests[security] >= 2.20; python_version < "3.0"',
#     ],
#     classifiers=[
#         "Intended Audience :: Developers",
#         "Intended Audience :: System Administrators",
#         "Operating System :: OS Independent",
#         "Topic :: Software Development",
#         "Environment :: Web Environment",
#         "Programming Language :: Python :: 2.7",
#         "Programming Language :: Python :: 3.5",
#         "Programming Language :: Python :: 3.6",
#         "Programming Language :: Python :: 3.7",
#         "License :: OSI Approved :: MIT License",
#     ],
#     tests_require=["pytest"],
#     extras_require={"testing": testing_extras,},
# )


from setuptools import setup, find_packages

setup(
    name="roman",
    version="0.1.0",
    url="https://github.com/mjr/juno-python",
    author=__author__,
    author_email=__author_email__,
    license="MIT",
    description=__description__,
    long_description=__long_description__,
    keywords="Payment, juno",
    packages=find_packages(),
    install_requires=["requests>=2.24.0"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)
