This is the readme for MATLAB-to-Python:

The goal of this program is to be able translate MATLAB code into Python code.

Below is some importation about the translator in its current state:

ADDED:
- Comments as tokens
- Keywords as tokens
- Formal grammar added (Some errors at the moment!) less now
- Parser methods

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
- Removed persistence as python doesn't have need of it
- Large ammount of guess work has been done a large amount of testing needs to be done!!!

TO DO LIST:
- Check tokens for excess
- Check grammar
- Fix string lexer
- Make all functions defined similarly in order to use switch in code generation
- Add indentation counter in parser

CURRENT STATUS:
- Will recognise tokens
- Parser has been filled in,(no testing done)
- Will parse most expressions correctly

DOES NOT SUPPORT: (support may be added at a later date)
- Cell arrays
- Matrices