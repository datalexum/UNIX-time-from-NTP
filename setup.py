from setuptools import setup, find_packages
from io import open
from os import path
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')
install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and (
    not x.startswith('#')) and (not x.startswith('-'))]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs \
                    if 'git+' not in x]

setup (
    name = 'UtfN',
    description = 'UNIX time from NTP or short UtfN is a simple CLI tool to set the time from an NTP-Server.',
    version = '1.0.1',
    packages = find_packages(),
    install_requires = install_requires,
    python_requires='>=3',
    entry_points='''
        [console_scripts]
        utfn=utfn.__main__:main
    ''',
    author="Alexander Schröder",
    keyword="time, date, unix, setup, linux, rtc, battery",
    long_description=README,
    long_description_content_type="text/markdown",
    license='MIT',
    url='https://github.com/datalexum/UNIX-time-from-NTP/',
    download_url='https://codeload.github.com/datalexum/UNIX-time-from-NTP/tar.gz/refs/tags/1.0.1',
    dependency_links = dependency_links,
                        author_email='alexander.schroeder-t59@rub.de',
                        classifiers=[
                                "License :: OSI Approved :: MIT License",
                                "Programming Language :: Python :: 3",
                                "Programming Language :: Python :: 3.8",
                            ]
)