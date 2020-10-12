#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages


def load_requirements(f):
    retval = [str(k.strip()) for k in open(f, "rt")]
    return [k for k in retval if k and k[0] not in ("#", "-")]


setup(
    name="rr_sdas",
    version="0.2.0",
    description="Basic example of a Reproducible Research Project in Python",
    url="https://github.com/sdevenes/M05_MiniProject",
    license="MIT",
    license_file="LICENSE",
    author="Steve Devènes, Amara Spano",
    author_email="steve.devenes@etu.unidistance.ch, amara.spano@etu.unidistance.ch",
    long_description=open("README.rst").read(),
    long_description_content_type="text/x-rst",
    packages=find_packages(),
    include_package_data=True,
    install_requires=load_requirements("requirements.txt"),
    entry_points={"console_scripts": ["rr-paper = rr.experiment.__main__:main",
                                      "rr-data = rr.download_data.__main__:main"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
