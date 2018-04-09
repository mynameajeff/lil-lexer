# lil-lexer
I made this lexer in ~(7-8) hours, but it works alright :v

It has a few neat features:
  - Regex Support for token rules (rule definitions must have the optional parameter isRegex set to True)
  - for multiple matches for a single token name, a list can be passed instead and tokens of the same name will be created for all the items in the list, but the state of the isRegex parameter will be applied to all of those resulting tokens.

Alongside those, it also has caveats:
  - Whitespace is obliterated due to the lexing process, which may make this lexer unsuitable in some cases.
  - When it encounters an undeclared token, it will cease to gather tokens from the line.
  - The later the token is declared, the lower the priority of lexing, so if a regex token checks for integers, and another for floats, if the integer token is declared before the float token, it will prefer the integer token.
  - Redeclaration of tokens has no effect. (Different Name, same Value)
  - Has no implemented error checking

For any other questions, please see the example in the related folder.
