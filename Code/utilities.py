"""Some useful functions used by several things"""

import re

def optionalFieldIsGood(mine, theirs):
    """check if optional field theirs matches with mine"""
    if (theirs is None or
            theirs == "" or
            theirs == mine):
        return True
    else:
        return False

def requiredFieldIsGood(mine, theirs):
    """check if required field theirs matches with mine"""
    if (theirs is not None and
            mine == theirs):
        return True
    else:
        return False

def sanitize(string):
    """Returns string with unsanitary characters (";) removed"""
    return string.translate(None, '";')

def validateName(name):
    """Returns False if name looks potentially incorrect"""
    if name.count(' ') > 1:
        return False
    # if has > 2 caps or 0 caps
    if sum(1 for c in name if c.isupper()) > 2 or sum(1 for c in name if c.isupper()) == 0:
        return False
    # if has more than 1 of ' or -
    if name.count('\'') > 1:
        return False
    if name.count('-') > 1:
        return False
    # if has any chars other than A-Z ' -
    if re.match('[A-Za-z\'-]*', name) == None:
        return False

    return True

def stripPhoneNumber(number):
    """Returns number stripped of any characters other than 0-9, +, and x"""
    newNumber = ''
    for c in number:
        if c.isdigit() or c == '+' or c == 'x':
            newNumber += c

    return newNumber
