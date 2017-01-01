"""
Assist is a library of functions that are usable in multiple other
modules, most commonly for things such as headers, footers, and
other common interfaces.
"""

import re
from django.conf import settings
from django.utils.timezone import utc
import evennia
from evennia import utils
from evennia.utils.ansi import ANSIString, ANSI_PARSER
from evennia.utils import evtable, create
from evennia.server.sessionhandler import SESSIONS

MAX_WIDTH = 78

# Titlecase accepts a string, and capitalizes the first letter of each word in it.
def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
        lambda mo: mo.group(0)[0].upper() +
            mo.group(0)[1:].lower(), s)


# header accepts a string and outputs a header of width 'width', defaults to nothing
def header(header_text=None, width=MAX_WIDTH):
    header_string = ""
    fill = "-"
    if header_text:
        header_string = "|R.-< |G" + header_text + " |R>-" + ( fill * (width - 8 - len(header_text))) + ".|n"
    else:
        header_string = "|R." + ( fill * (width - 2)) + ".|n"

    return header_string


# footer accepts a string and outputs a foot of width 'width', defaults to game name
def footer(footer_text=None, width=MAX_WIDTH):
    footer_string = ""
    fill = "-"
    if footer_text:
        footer_string = "|R'" + ( fill * (width - 8 - len(footer_text))) + "-< |G" + footer_text + "|R >-'|n"

    else:
        footer_string = "|R'" + ( fill * (width - 8 - len(settings.SERVERNAME))) + "-< |G" + settings.SERVERNAME + "|R >-'|n"

    return footer_string


# csex accepts input, if it matches any of the registered 'sex' varients
# it will return it colorized for consistency. Set short to True to get
# a single letter output. Returns unmodified input if not recognized.
def csex(input, short=False):

    if input == "Male":
        if short:
            return "|RM|n"
        else:
            return "|RMale|n"
    elif input == "Female":
        if short:
            return "|MF|n"
        else:
            return "|MFemale|n"
    elif input == "Hermaphrodite":
        if short:
            return "|CH|n"
        else:
            return "|CHermaphrodite|n"
    elif input == "Intersex":
        if short:
            return "|BI|n"
        else:
            return "|BIntersex|n"
    elif input == "Neuter":
        if short:
            return "|wN|n"
        else:
            return "|wNeuter|n"
    else:
        return input