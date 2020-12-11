from pdf_redactor import pdf_redactor

import re

options = pdf_redactor.RedactorOptions()

"""
options.content_filters = [
    (
        re.compile(u"Damik Dhar"),
        lambda m: "(Farhan Hai Khan)"
    ),
]
"""

options.content_filters = [
    (
        re.compile(u"ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
        lambda m: "FARHAN HAI KHAN"
    ),
]

# Perform the redaction using PDF on standard input and writing to standard output.
pdf_redactor.redactor(options)

# python Gen4.py < templates/1.pdf > document-redacted.pdf
# python Gen4.py < templates/medicai.pdf > document-redacted.pdf
