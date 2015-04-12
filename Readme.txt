This is the readme for MATLAB-to-Python:

THe goal of this program is to be able translate MATLAB code into Python code.

Currently the only working feature is the lexical analysis which will work for simple input.

ADDED:
- Comments as tokens
- Keywords as tokens
- Formal grammar added (Some errors at the moment!)


TOKENS NOT NEEDED:
- PLUSPLUS + similar
- PLUSEQUALS + similar removed

PARSE TERMS REMOVED (NOT FULL LIST):
- Lambda_args
- Lambda_expr

PROBLEMS NOTICED:
- Left and Right divide
- Array left and right division

NOTES:
- Dotdivequals and Dotmulequals have been removed not sure what they do
- Lots more equals removed
- L/RBRACKET's are different tokens in grammar

TO DO LIST:
- Check tokens for excess
- Check grammar
- Fix string lexer

CURRENT STATUS:
- Will recognise tokens
- Will parse simple expressions such as 9+5*(4-1)