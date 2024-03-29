### Text editor end-of-line-trimming

When editing text files, like source code, one often happens to add spurious spaces and tabs in the end of each line. Instead of pressing the "End" key at each line and removing those invisible characters manually, a simple algorithm to remove them automatically at the press of a button could be used.

Using Test-Driven Development, build a class or function that, given an input string, produces a right-trimmed output string.

Here are some tests that you could write:

* "abc " -> "abc"
* "abc\t" -> "abc"
* "  abc" -> "  abc" (does not remove beginning whitespace)
* "ab\n cd \n" -> "ab\ncd\n" (removes whitespace for each line)
* "ab\r\ncd\n" -> same string (handles both Windows and Unix line endings)
