#!/usr/bin/env python3

import lexer

test = lexer.Lexer("test.code")

# Adds a token for the Lexer to look for

test.add("ATSYMBOL", "@")
test.add("LIBSTR", "library")

test.add("LIB", "stdio")
test.add("LIB", "stdlib")
# test.add("LIB", r"std(io|lib)", isRegex = True) #alternative, regex-y way of
#     doing the last two lines.
# test.add("LIB", ["stdio", "stdlib"]) #alternative, less regex-y way of doing
#     the last two (uncommented) lines.

test.add("LPAREN", "(")
test.add("RPAREN", ")")

test.add("SEMICOLON", ";")

test.add("ADD-OPERAND", "+")
test.add("MUL-OPERAND", "*")

test.add("FLOAT",   r"(\d+\.(\d+)?|\.\d+)", isRegex = True)
test.add("INTEGER", r"\d+",                 isRegex = True)

tokenfinal = []

for token_list in test:

    if token_list:
        tokenfinal += token_list
        print(token_list)
