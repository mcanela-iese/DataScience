# 6. String data

### Strings

A **string** is a sequence of **characters**. This includes the (English) alphanumeric characters and also special characters like white space, punctuation, etc. Other symbols, like emoticons, can also appear in your data, specially in social networks data. Besides that, you can also find the letters from other languages (Cyrillic, Han, Kanji, etc).

There is a basic set of 127 characters, called the **ASCII characters**, which are encoded in the same way by all the computers, so you will never have trouble with them. They include the English letters (without accents), the numbers, basic punctuation (not curly quote marks or long dashes), white space, **control characters** such as the new line, shown in Python as `\n`, and other symbols familiar to you, such the dollar (`$`) and the hash (`#`) symbols. The complete list can be easily found in Internet.

Non-ASCII characters can be encoded by different computers or different text editors in different ways. Mind that, if you capture string data on your own, you will probably find some of these characters in your data. Even when the documents are expected to be in English, they can be contaminated by other languages: Han characters, German umlaut, Spanish eñe, etc.

The preferred **encoding** is **UTF-8** (`utf-8`), which is the default encoding in Macintosh computers. Reading and writing text files in Pandas, the argument `encoding` allows you to manage both UTF-8 and the alternative encoding **Latin-1** (`latin1`). Windows computers use their own system, which is region specific. In US and Western Europe, this is **Windows-1252**, which is very close to Latin-1, though not exactly the same.

### Strings as lists

Being a sequence, a string is managed in Python as a list, inheriting some basic methods from lists. Examples: (a) the function `len` gives you the number of characters of a string, (b) the plus sign (`+`) allows you to concatenate strings, and (c) you can extract a **substring** from a string in the same way you extract a sublist from a list using a range of indexes.

A difference between strings and lists is found in the use of `in`. For lists, it indicates that an object is among the elements of a list. For strings, that a string is contained in another string.

### Python string methods

Besides the methods inherited from lists, Python has a collection of methods for manipulating strings. The most widely used, among those methods, is `replace`. The syntax is `str.replace(old, new)`. Other common methods are `lower`, `upper`, `split`, `find` and `count`.

### Regular expressions

A **regular expression** is a pattern which describes multiple strings. Regular expressions can be used in many computer languages. In Python, the package `re`, which is part of the Python Standard Library, provides some functions which read a matching pattern as a regular expression.

For instance, we can combine the `re` function `sub` with the regular expression `[a-z]`, which stands for any lower case (ASCII) letter. Then, `re.sub([a-z], repl, str)` will return a string resulting from the string `str` after replacing *each of those letters* by the string `repl`. `[a-z]` is an example of a **character class**. Character classes are built by enclosing a collection of characters within square brackets. The square brackets indicate *any* of the characters enclosed.

Character classes get more powerful when complemented with **quantifiers**. For instance, followed by a plus sign (`+`), a character class indicates a sequence of any length. So, `[a-z]+` indicates any word made of lower case ASCII letters and `re.sub([a-z]+, repl, str)` will replace *each word* by the string `repl`.

### Pandas string functions

Pandas **string functions** are vectorized versions of those old methods. The syntax takes, in most cases, the form `s.str.fname(args)`. For a Pandas series `s`, this returns another Pandas series, resulting from applying the function `fname` term-by-term.

Pandas functions accept a regular expression as a matching pattern, with the argument `regex=True`, but read the pattern as a fixed string with `regex=False`. For instance, `s.str.replace('. ', repl, regex=False)` replaces every instance of the string made by a dot plus a white space by the string `repl`. But `s.str.replace('. ', repl, regex=True)` reads the pattern `'. '` as a regular expression. Since the dot is used in regular expressions as a **wildcard**, which can match any single character (letter, digit, whitespace, etc), followed by a white space will be replaced by `repl`.

### Some useful Pandas functions

* The Pandas function `str.len` returns the **length** of every element of a string series. This is just a vectorized version of the Python function `len`.

* **Substrings** can be extracted term-by-term from a string series just as we extract elements from a list. The syntax is either `s.str[start, end]`, `s.str[:end]` or `s.str[start:]`.  

* Strings are **joined** in Python just as lists, with the plus sign (`+`). The same works for string series. For instance, `s1 + ' ' + s2` returns a series in which every term results from pasting the corresponding terms from `s1` and `s2`, with a white space as the glue.

* `str.lower`  **converts to lowercase**. The syntax is `s.str.lower()`.

* `str.contains` **detects the presence of a pattern** in the terms of a string series. The syntax is `s.str.contains(pat)`. This returns a Boolean series indicating, term by term, whether `pat` occurs in `s`.

* `str.findall` **extracts matching patterns** from the terms of a string series. The syntax is `s.str.findall(pat)`. This returns a series in which every term is a list containing all the occurrences of `pat` in the corresponding term of `s`. Using lists as the values of this function allows for the pattern to occur with different frequency along `s`.

* `str.replace` **replaces matched patterns** in the terms of a string series. The syntax is `s.str.replace(pat, repl)`.

* `str.split` **splits up** into pieces the terms of a string series. The syntax is `s.str.split(pat)`. The default pattern is `pat=''`. This returns a series in which every term is a list containing the words contained in the the corresponding term of `s` (such list is called a bag of words).

The patterns used by the functions `str.contains`, `str.findall`, `str.replace` and `str.split` can be fixed strings or **regular expressions**.
