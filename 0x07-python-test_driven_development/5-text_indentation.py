#!/usr/bin/python3
"""
    prints a text with 2 new lines after each of these characters: ., ? and :

    prototype: text_indentation(text):
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    new_text = ""
    i = 0
    if type(text) != str:
        raise TypeError("text must be a string")
    while i in range(len(text)):
        new_text += text[i]
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            new_text += "\n\n"
            i += 1
        i += 1
    print(new_text, end="")
