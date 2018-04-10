##lexer.py

# try:
#     import regex

# except:
#     import re as regex

import regex


class Token:

    def __init__(self, name, value, isRegex = False):

        self.Name  = name.upper()
        self.Value = value
        self.isRegex = isRegex


    def __repr__(self):
        return "ObjToken({:s}, \"{:}\")".format(
            self.Name,
            self.Value)


    def __len__(self):
    
        return len(self.Value)


class Lexer:

    def __init__(self, filename):

        with open(filename, "r") as file:
            self.file = [x.split(" ") for x in file]

        self.tokens = []

        self.iteration_level = 0


    def __iter__(self):
        return self


    def __next__(self):

        if self.iteration_level == len(self.file):
            raise StopIteration

        current_line = self.file[self.iteration_level]

        self.iteration_level += 1

        return self.get_tokens(current_line)
        

    def add(self, token_name, value, isRegex = False):

        if isinstance(value, dict):
            for key, value in value.items():
                self.add(token_name.replace("@", key), value, isRegex)

        elif isinstance(value, list):
            for token_rule in value:
                self.add(token_name, token_rule, isRegex)

        if isRegex:
            self.tokens.append(Token(token_name, value, isRegex = True))

        else:
            self.tokens.append(Token(token_name, value))


    def get_tokens(self, line):

        if ''.join(line).replace(" " , "") \
                        .replace("\n", "") == "":

            return None

        line = ' '.join(line)

        current_token = 0

        isLexing = True

        token_list = []

        while isLexing:

            token = self.tokens[current_token]

            if token.isRegex:

                regex_check = regex.match(token.Value, line)
                
                if regex_check:

                    token_list.append(Token(token.Name, regex_check.group(0)))

                    line = line[len(regex_check.group(0)):].lstrip()

                    current_token = 0

                else:
                    current_token += 1

            elif line[:len(token.Value)] == token.Value:

                token_list.append(token)
                line = line[len(token.Value):].lstrip()
                current_token = 0

            else:
                current_token += 1


            if current_token == len(self.tokens):
                isLexing = False


        return token_list
