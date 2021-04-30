#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "click",
    "moviepy",
    "pillow",
    "numpy",
]

setup(
    author="Marco Caggioni",
    author_email="marco.caggioni@gmail.com",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="CLI tool to create timelapse video from sequence of images stored in a single folder",
    entry_points={"console_scripts": ["seq2video=seq2video.cli:main"]},
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="seq2video",
    name="seq2video",
    packages=find_packages(include=["seq2video", "seq2video.*"]),
    url="",
    version="0.1.0",
    zip_safe=False,
)
