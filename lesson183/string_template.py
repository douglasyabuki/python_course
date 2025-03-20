# Using string.Template to substitute variables into text
# Docs: https://docs.python.org/3/library/string.html#template-strings
# Methods:
# substitute: replaces placeholders and raises an error if any keys are missing
# safe_substitute: replaces placeholders without raising errors for missing keys
# You can also change the delimiter and other properties by creating a subclass of Template.

import locale
import string
from datetime import datetime
from pathlib import Path

FILE_PATH = Path(__file__).parent / 'lesson183.txt'

locale.setlocale(locale.LC_ALL, '')


def convert_to_brl(amount: float) -> str:
    brl = 'R$ ' + locale.currency(amount, symbol=False, grouping=True)
    return brl


date = datetime(2022, 12, 28)
data = dict(
    name='John',
    amount=convert_to_brl(1_234_456),
    date=date.strftime('%d/%m/%Y'),
    company='O. M.',
    phone='+55 (11) 7890-5432'
)


class MyTemplate(string.Template):
    delimiter = '%'


with open(FILE_PATH, 'r', encoding='utf-8') as file:
    text = file.read()
    template = MyTemplate(text)
    print(template.substitute(data))
