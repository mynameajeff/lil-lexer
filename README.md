# lil-lexer

This lexer has a few neat features:
  - Regex Support for token rules (rule definitions must have the optional parameter `isRegex` set to True)
  - For multiple matches for a single token name, a list can be passed instead and tokens of the same name will be created for all the items in the list, but the state of the `isRegex` parameter will be applied to all of those resulting tokens.
  - For tokens of a similar name (e.g. `ADD-OPERAND`, `MUL-OPERAND`), you could simply pass a string `@-OPERAND`(the @ is what is replaced, and more than one is allowed), and a dictionary to the .add method of the lexer.Lexer object, which contains the difference(key), and the value of the token. (PLEASE NOTE: Normal dictionaries do not keep the order of which items were entered, which can cause some problems due to the priority caveat discussed below. To fix this in such cases where priority is important, use `collections.OrderedDict`)
  - The dict/list rule features can be nested.

Alongside those, it also has caveats:
  - Whitespace is obliterated due to the lexing process, which may make this lexer unsuitable in some cases.
  - When it encounters an undeclared token, it will cease to gather tokens from the line.
  - The later the token is declared, the lower the priority of lexing, so if a regex token checks for integers, and another for floats, if the integer token is declared before the float token, it will prefer the integer token.
  - Redeclaration of tokens has no effect. (Different Name, same Value)
  - Has no implemented error checking

For any other questions, please see the example in the related folder.
