This is the readme for MATLAB-to-Python:

The goal of this program is to be able translate MATLAB code into Python code.

Below is some information about the translator in its current state:

MAJOR CHANGES - Indentation handling has been changed, testing needed.

ADDED:
- New indentation handling
- New methods in codegen to deal with indents
- Functions file will direct translations for some functions
- Added some function translations (simple ones, no argument changes)
- Main method, asks for filename to be translated

NOTES:
- L/RBRACKET's are different tokens in grammar
- Removed persistence as python doesn't have need of it

TO DO LIST:
- Add comments
- Testing!!
- Clean up error messages, some are getting pass to command line
- Error catching
- Remove print lines from parser
- Make for loops work for more complex ideas

CURRENT STATUS:
- Lexer will recognise most tokens
- Parser will parse all grammar
- Code generation will work for some inputs (see support list)
- Unable to deal with comments

FULL SUPPORT LIST:
- Simple expressions
- for loops (range function only no iterations yet!)
- if/else if/else loops
- switch
- brackets
- true, false, continue, break, return
- while
- try catch statements
- Function declaration
- Simple functions

DOES NOT SUPPORT: (support may be added at a later date)
- Cell arrays
- Matrices