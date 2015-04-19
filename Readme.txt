This is the readme for MATLAB-to-Python:

The goal of this program is to be able translate MATLAB code into Python code.

Below is some information about the translator in its current state:

MAJOR CHANGES - In the structure of the translator, testing needed.

MAJOR PROBLEMS - Indentation can no handle loops after loops, fix needed.

ADDED:
- Added try and catch
- Small changes
- Indentation handling changes

GRAMMAR TERMS REMOVED (NOT FULL LIST):
- Lambda_args
- Lambda_expr

PROBLEMS NOTICED:
- Left and Right divide
- Array left and right division
- Newlines in strings can't be read in probably
- Indentation

NOTES:
- Dotdivequals and Dotmulequals have been removed not sure what they do
- Lots more equals removed
- L/RBRACKET's are different tokens in grammar
- Removed persistence as python doesn't have need of it
- Large ammount of guess work has been done a large amount of testing needs to be done!!!

TO DO LIST:
- Check tokens for excess
- Fix string lexer
- Testing
- Clean up error messages, some are getting pass to command line
- Add comments
- Indentation

CURRENT STATUS:
- Lexer will recognise most tokens
- Parser will parse all grammar
- Code generation will work for some inputs (see support list)

FULL SUPPORT LIST:
- Simple expressions
- for loops (range function only no iterations yet!)
- if/else if/else loops
- switch
- brackets
- true, false, continue, break, return
- while
- try catch statements

DOES NOT SUPPORT: (support may be added at a later date)
- Cell arrays
- Matrices