### Word-wrapping

In text editors you can usually find a configuration setting named "Word wrap". When checked, lines that do not fit horisontally in the editor window are "wrapped" to several lines, thus removing the need for a horisontal scroll bar in the window.

Develop a word-wrapping algorithm, which is given a string and a row-length, and returns a list of word-wrapped-rows.

Examples of behaviour:

* If the row-length is 60, and the input string is 30, the result is just the input string
* If the row-length is 3, and the input string is "abc def" the result is "abc", "def"
* If the row-length is 3, and the input string is "abcdef" the result is "abc", "def"
* If the row-length is 3, and the input string is "abcdef abc" the result is "abc", "def", "abc"
* With row length 3 and "a b c d e f" the result is "a b", "c d", "e f"
