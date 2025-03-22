# Web Scraping with Python using requests and bs4 (BeautifulSoup)
# - Web scraping is the process of automatically extracting information
#   from websites using a programming language for later use.
# - The requests module retrieves web data into your Python script.
# - The bs4.BeautifulSoup module parses HTML content into Python objects,
#   making data extraction easier for developers.
# - Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# Installation:
# pip install requests types-requests bs4

import re

import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:3333/'
response = requests.get(url)
html_bytes = response.content
parsed_html = BeautifulSoup(html_bytes, 'html.parser', from_encoding='utf-8')

# if parsed_html.title is not None:
#     print(parsed_html.title.text)

top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')

if top_jobs_heading is not None:
    article = top_jobs_heading.parent

    if article is not None:
        for p in article.select('p'):
            cleaned_text = re.sub(r'\s{1,}', ' ', p.text).strip()
            print(cleaned_text)
