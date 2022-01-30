# 8. Web scraping in Python

### What is web scraping?

**Web scraping** is concerned with extracting data from websites, in particular data that would be difficult to get on a large scale using traditional data collection methods. There is a whole industry built around web scraping, as it is used to track product price changes or discounts, to gather data from social profiles, to capture real estate listings, in search engine optimization (SEO), etc.

Scraping a web page involves downloading the page and extracting data from it. Both things can be done with many languages, in particular with Python. There are also specialized web scraping software applications, such as **Octoparse**. This course covers only those pages that are rendered to the browser in a single step (explained below). Although we use in this course the package `lxml`, you can use other Python packages, such as Beautiful Soup (`bs4`) and Scrapy (`scrapy`).

### HTML and the browser

Suppose that your browser (let me assume that you use either Chrome or Firefox) is displaying a web page on the screen. You can get the source code of the page through the contextual menu that opens when right-clicking anywhere on the page. A new tab will open, displaying a HTML document. In most pages, this HTML document corresponds to the page that the browser displayed for you. These pages are the ones covered here. But not all pages are that simple. Some use a technology called **AJAX** (Asynchronous JavaScript And XML), which, in a few words, works as follows:

1. The page corresponding to the URL that you have entered is loaded.

2. A JavaScript program creates a XMLHttpRequest object.

3. The XMLHttpRequest object sends a request to a web server.

4. The server sends a new HTML document back to the browser, which is displayed on the screen. This second document corresponds to the page that you see.

The problem is that neither the Python methods discussed in this course capture this second document, which is, probably, from where you wish to scrape, but the first one. To get the second one, web scrapers use a tool called **Selenium**, which in Python can be accessed through the package `selenium`.

### The package Requests

With Python, files can be downloaded from Internet sources in multiple ways. Many tutorials suggest using the package `urllib`, which is part of the Python Standard Library. More popular, nowadays, is the package Requests (`requests`), briefly introduced here. Requests comes with the Anaconda distribution, so you do not have to install it.

Let us refresh the context. You have probably noticed the string `'https'` (sometimes `'http'`) at the beginning of a URL. The **Hypertext Transfer Protocol** (HTTP) was designed to enable communications between clients and servers. For instance, a client (such as your browser) sends a **HTTP request** to the server. Then the server returns the response to the client. The response contains status information about the request and, if the request is accepted, the requested content.

**GET** is one of the most common HTTP methods. It is used to request data from a specified resource. The function `requests.get` is a Python implementation of the GET request. You can manage this as follows.

`import requests`

`page = requests.get(urlname).text`

`requests.get` returns a `requests` object (type `requests.models.Response`). The attribute `text` of this object is a string which, for an ordinary web page, is the HTML source code. Now you can parse this string with the function `BeautifulSoup`, which has already appeared in this course, and then extract the information you are interested in.
