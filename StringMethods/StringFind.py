# finds a occurance of passed string and provides its positive index 

tempStr = """Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming. Wikipedia
Designed by: Guido van Rossum
Developer: Python Software Foundation
Filename extensions: .py,.pyw,.pyz,.pyi,.pyc,.pyd
First appeared: 20 February 1991; 33 years ago
Paradigm: Multi-paradigm: object-oriented, procedural (imperative), functional, structured, reflective
Stable release: 3.12.6 / 7 September 2024; 6 days ago
Typing discipline: duck, dynamic, strong; optional type annotations (since 3.5, but those hints are ignored,
 except with unofficial tools)"""

print(tempStr.find('Python'))
search = 'python'

if tempStr.lower().find(search)<0:
    print("search string {0} doesnt exist".format(search))
else:
    print(tempStr.lower().count('python'))

