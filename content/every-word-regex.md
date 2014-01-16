Title: Return a List of Every Entry in Websters 1913 Dictionary with One Python Regex 
Date: 2014-01-15
Tags: Python, Regex
Slug: one-regex
Summary: Regular expressions are amazing. In a text file that contains the entire Webster's Unabridged Dictionary (over 4.5 million words) you can use one regular expression (36 characters) to match only the 103,039 dictionary entries. Here's how:

First, you'll need to visit [http://www.gutenberg.org/ebooks/29765][4] and download the 'Plain Text UTF-8' file. This is the 1913 edition of Webster's Unabridged Dictionary, as a 27.6 MB text file. Save this as 'dictionary.txt'.

Next, create your python script in the same directory you saved your text file. I called mine 'search.py'.

Start your script by importing Python's regular expression module.

```python
import re
```

Next, open your 'dictionary.txt' file and initialize it as a file object.

```python
import re
with open('dictionary.txt') as dictionary:
```

After that, convert the text file into a string and store it in a variable.
 
```python
import re
with open('dictionary.txt') as dictionary:
    dicstring = dictionary.read()
```

Our next variable will store the regex itself, which I'll explain in detail.

```python
import re
with open('dictionary.txt') as dictionary:
    dicstring = dictionary.read()
    pat = re.compile(r'(?<=\r\n\r\n)[A-Z]+(?![a-z])(?=\r\n)')
```

The `re.compile` part allows us to store a regex in a variable, so we can use it later if need be. The function takes a string as an arguement for the regular expression. The `r` before the regex string tells python to interpret the quoted text as a [raw string][1] and avoids the [backslash plague][2] in Python's re module. The `(?<=...)` section is a [positive lookbehind assertion][3] and tells the regex engine to only match a string if it is preceded by `...`. Our lookbehind assertion is `\r\n\r\n` because every entry in our dictionary file is preceded by this string. The next chunk is our actual matching pattern, `[A-Z]+`. This bit says, match one or more continuous uppercase letters (preceded by `\r\n` because of the lookbehind assertion). The next part `(?!...)` is a negative lookahead assertion, and tells python to only return a match if the pattern is NOT followed by `...`, which for us is `[a-z]` or any lowercase letter. The negative lookahead assertion is required because there are certain title case words (i.e 'Help') at the end of the text file that were matching. The regular expression ends with a positive lookahead assertion, `(?=...)` that tells Python to match only if the pattern IS followed by `...`, in our case `\r\n` (all dictionary entries in the text file are followed by this string).

To actually run our compiled regular expression against the dictionary stored as a string, we'll use the re.findall function and store the result in the variable `entries`. As you can see below, re.finall(expression, string) takes two arguments, the first being the compiled regular expression and the second being the string to match against.  

```python
import re
with open('dictionary.txt') as dictionary:
    dicstring = dictionary.read()
    pat = re.compile(r'(?<=\r\n\r\n)[A-Z]+(?![a-z])(?=\r\n)')
    entries = re.findall(pat, dicstring)  
```

Below is the entire script, along with some commented out code that can be uncommented to print various other interesting things to the console.

```python
import re, random

with open('dictionary.txt') as dictionary:
    dicstring = dictionary.read()
    pat = re.compile(r'(?<=\r\n\r\n)[A-Z]+(?![a-z])(?=\r\n)')
    pat1 = re.compile(r'[A-Za-z]+'] # This regex will match (approximately) all
words in the text file
    entries = re.findall(pat, dicstring)
    ##Uncomment the below line to see the actual string (with '\r\n' etc.)
    #print repr(dicstring)
    ##Uncomment the below line to print the number of words matched
    #print len(entries)
    ##Uncomment the below line to print your list of dictionary entries
    #print entries
```

[1]: http://docs.python.org/2/reference/lexical_analysis.html#string-literals "Python string literals"
[2]: http://docs.python.org/2/howto/regex.html#the-backslash-plague "Python regex backslash plague"
[3]: http://docs.python.org/2/library/re.html#regular-expression-syntax "Python regex syntax"
[4]: http://www.gutenberg.org/ebooks/29765 "Webster's 1913 dictionary on Project Gutenberg"
