# 7. HTML data

### What is HTML?

**HTML** (Hypertext Markup Language) is the language in which are written the documents designed to be displayed in a web browser. The web browser receives HTML documents from a web server or from local storage and renders the documents as multimedia web pages.

HTML is assisted by two technologies:

* **CSS** (Cascading Style Sheets) is a language used to describe the style of HTML documents.

* **JavaScript** is a scripting language, that is, one for integrating and communicating with other languages. Scripting languages are used for "small jobs". JavaScript code can be used when processing dynamic HTML documents in Python, for instance in web scraping jobs, but this must be left for an advanced course.

An extremely simple example of a HTML document follows. It is easy to see, in this example, why HTML is called a **markup language**. The markup, which consists here of the tags `<head>`, `<body>`, `<title>`, `<div>` and `<a>`, is used for creating a structure in the document and for including **links** to web pages, pictures, etc.

	<html>

	<head>

		<title>Data Viz</title>

	</head>

	<body>

		<div class="course">Data Visualization</div>

		<div class="program">MBA full-time</div>

		<a class="professor" href="https://www.iese.edu/faculty-research/faculty/miguel-angel-canela">Miguel Ángel Canela</a>

	</body>

	</html>

Unfortunately, in a HTML document captured from Internet, you will not find such a friendly presentation, with one line for each tag, and indentation to help you see the structure of the document. But there are many tools for rendering the XML and HTML documents in this form.

### Tags and attributes

The structure of a HTML document is made by the tags. Every part of the document is opened by a **start tag** (`<tag>`) and closed by an **end tag** (`</tag>`). The tags create a tree-like structure in the document. In HTML, only the tags and the text between the tags matter. Some web designers insert white space to make the document readable, but that white space between tags is ignored by the HTML interpreter.

The tag `<html>` tells the browser that this is a HTML document. The part of the document enclosed by a start tag and an end tag is called a **HTML element**. The `html` element is the whole document. It has two **child elements**, `head` and `body`. A HTML document is always split in this way. In the example, the `head` element has one **child**, while the `body` element has three children, which are **siblings**.

Then, the `title` element contains the string `'Data Viz'`, enclosed between the start tag and the end tag (this can also be said of the `head` element). This string is referred to as **text**. Also, most of the tags have **attributes**. The attributes are contained in the start tag. In our example, the `div` tags have one `class` attribute, while the `a` tag has two attributes, a `class` attribute and a `href` attribute. `class` attributes, which specify one or more `class` names for a tag, are very frequent, and can be used in any tag. The value of a `class` attribute can be used by CSS and JavaScript to perform certain tasks for tags with that `class` value.

The `a` tag has a special role. It marks a **hyperlink**, which is used to link a page to another page, or to download a file. The most important attribute of the this tag is the `href` attribute, which indicates the link's destination.

### Beautiful Soup

Suppose that a HTML document has been imported to your computer as the Python string `html_str`. How can we extract the pieces of information we are interested in? There are various approaches (not equally powerful) and no consensus about which is best, bout most practitioners agree that the simplest way to start is that of the package **Beautiful Soup**.

You can install Beautiful Soup by entering in the shell (or in the Jupyter console):

`pip install bs4`

It is already installed, you import the function `Beautiful Soup` with:

`from bs4 import BeautifulSoup`

This function can **parse** an HTML document, learning the tree structure encoded there, which is stored in a "soup"  object:

`soup = BeautifulSoup(html_str, 'html.parser')`

The simplest way to extract the tags that contain a certain type of information is by means of the methods `find` and `find_all`. The method `find_all` returns a list containing all the tags that satisfy a specification, while `find` returns only the first one. The specification of the tags can be just a tag name, such as `div`, or a tag name plus an attribute value. For instance, we get a list containing the two `div` tags with:

`tag_list = soup.find_all('div')`

Or the second `div` tag with:

`tag = soup.find('div', 'program')`

Once the interesting tags have been captured, the text enclosed in a tag can be extracted as:

`tag.text`

In certain cases, we are interested in an attribute value. Example: `a` tag whose attribute `href` contains a relevant link. This is extracted as:

`tag['href']`
