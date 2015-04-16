This is the readme for MATLAB-to-Python:

The goal of this program is to be able translate MATLAB code into Python code.

Below is some information about the translator in its current state:

MAJOR CHANGES - In the structure of the translator, testing needed.

ADDED:
- Node file
- Codegen file
- Now translates for loops (range function only)
- Indentation can now be done for all looping functions

GRAMMAR TERMS REMOVED (NOT FULL LIST):
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
- Fix string lexer
- Add other looping functions
- Testing

CURRENT STATUS:
- Lexer will recognise most tokens
- Parser will parse all grammar
- Code generation will work for some inputs (see support list)

FULL SUPPORT LIST:
- Simple expressions
- For loops

DOES NOT SUPPORT: (support may be added at a later date)
- Cell arrays
- Matrices