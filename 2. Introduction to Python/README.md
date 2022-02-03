# 2. Introduction to Python

### What is Python?

**Python** is a programming language, introduced in 1991. The last version is Python 3.10. To work with Python, you will pick an interface to the Python interpreter among the many available choices. You can have several "instances" of the interpreter, called **kernels**, running independently in your computer.

Warning: Python is **case sensitive**. So, `type` is a Python function which returns the type of an object, but `Type` is not recognized (unless you create a new function with this name), and will return an error message.

### The Anaconda distribution

There are many distributions of Python. In the data science community, **Anaconda** (`anaconda.com`) is the favorite one. The current Anaconda distribution comes with Python 3.9. Downloading and installing Anaconda will leave you with the **Anaconda Navigator**, which opens in the browser and allows you to choose among different interfaces to the Python interpreter. Alternatively, you can bypass the navigator calling those interfaces in a **shell** application (such as *Command Prompt* in Windows, or *Terminal* in Mac).

Among the many interfaces offered by Anaconda, I recommend you the **Jupyter Qt console**, which is an input/output text interface. Jupyter (Julia/Python/R) is a new name for an older project called **IPython** (Interactive Python). IPython's contribution was the IPython shell, which added some features to the mere Python language. The Qt console is the result of adding a graphical interface (GUI), with drop-down menus, mouse-clicking, etc, to the IPython shell, with a toolkit called Qt.

Jupyter provides an alternative approach, based on the **notebook** concept. In a notebook, you can combine input, output and ordinary text. In the notebook arena, **Jupyter Notebook** is the leading choice, followed by **Apache Zeppelin**. Most data scientists prefer the console for developing their code, but use notebooks for difusion, specially for posting their work on platforms like GitHub.

Besides the Jupyter tools, Anaconda also provides a Python IDE (Integrated Development Environment) called **Spyder**, where you can manage a console and an text editor for your code. If you have previous experience with this type of interface, for instance from working with R in RStudio, you may prefer Spyder to the QtConsole. Calling any of these apps will start a Python kernel. You can then send commands to the interpreter.

### Python packages

Python is modular. When a kernel is started, only a few basic resources are available. Many additional resources can been added in the form of **modules**. A module is just a text file containing Python code. The **Python Standard Library** is a basic collection of modules included in any Python distribution.

Modules are grouped in libraries, also called **packages**, because their elements are packed according to some specific rules which allow you to install and call them together. Plain Python can be extended by more than 300,000 packages. Some big packages, like scikit-learn, are composed of many **subpackages**.

Since plain Python (without any extra module) is quite limited, you will need additional resources for practically everything. For instance, suppose that you want to do some math, and calculate the square root of 2. You will then **import** the module `math`, whose resources include the square root and many other mathematical functions. Once the package has been imported, all its functions are available. You can then apply the function `math.sqrt`. This notation indicates that `sqrt` is a function of the module `math`.

Packages are imported just for the current kernel. You finish the session by either closing the console or by restarting the kernel. You can do this with `Kernel >> Restart current Kernel` or by typing `Ctrl+.`.

With Anaconda, most packages used in this course are already available and can be directly imported. If it is not the case, you have to **install** the package (only once). There is a basic installation procedure in Python, which uses a **package installer** called `pip` (see `pypi.org/project/pip`). We will do it in some examples of this course.

**Pandas** (2008) is a library for data management, very popular among data scientists. Pandas is built on top of two older libraries, NumPy and Matplotlib. **NumPy** (1995) is a library for dealing with vectors and matrices, called there **arrays**. **Matplotlib** is a graphics library, based on NumPy. This course uses Pandas in most examples, but the coverage of NumPy and Matplotlib is very superficial.

### Data types

The **data types** in Python are similar to those of other languages. The type can be learned with the function `type`. Let me review the main data types:

* First, we have **integer numbers** (type `int`). There are subdivisions of this basic type, such as `int64`, but you don't need to know about that to start using Python.

* We can also have **floating-point** numbers (type `float`), that is, numbers with decimals. We also have subdivisions here, such as `float64`.

* Under type `bool`, Python admits **Boolean** values, which are either `True` or `False`.

* Besides numbers, we can also manage **strings**, with type `str`.

### Data containers

Python has various **data container** types. The most versatile is the **list**, which is represented as a sequence of comma-separated values inside square brackets:

`mylist = ['Messi', 'Cristiano', 'Neymar', 'Coutinho']`

An element of a list is extracted indicating its place between square brackets. For instance, `mylist[1]` would extract `'Cristiano'` (in Python we start at zero). To extract a sublist with several consecutive terms, we indicate the corresponding range. For instance, `mylist[1:3]` extracts the sublist `['Cristiano', 'Neymar']` (in Python, the left limit is included but the right limit is not).

A **tuple** is like a list, represented with parentheses instead of square brackets:

`mytuple = ('Messi', 'Cristiano', 'Neymar', 'Coutinho')`

A **dictionary** is a set of **pairs key/value**. For instance, the following dictionary contains three features of an individual:

`mydict = {'name': 'Joan', 'gender': 'F', 'age': 32}`

The packages used in data science come with new data container types: NumPy arrays, Pandas series and Pandas data frames. Dealing with so many types of objects is a bit challenging for the beginner. The elements of the Python data containers (eg lists) can have different data types, but NumPy and Pandas data containers have consistency constraints. So, an array has a unique data type, while a data frame has a unique data type for every column.

### Functions

A **function** takes a collection of **arguments** and performs an action. The functions that appear in this course will **return** a value. For instance, `len(mylist)` returns `4`. In addition to the built-in functions (such as `len` or `int`) and those coming in the packages that you may import (such as `math.sqrt`), you can define your own functions. The definition will work only for the current kernel. If you are happy with your function, you will save it in a source file for future use.

A simple example of a user-defined function would be:

`def f(x): return 1/(1 - x**2)`

Longer definitions can involve several lines of code. In that case, all the lines after the colon must be *indented*. Jupyter interfaces create the indentation automatically when we press the *Return* key after the colon.

### Loops and conditional logic

**Loops** are used in practically all programming languages, so, if you will be familiar with them if you programming experience. In particular, `for` loops are used to avoid repetition. Suppose that you wish to extract the first letter of the names of the list `mylist`, storing them in a new list. You can use the `for` loop to iterate the extraction:

`inilist = [name[0] for name in mylist]`

This would return `['M', 'C', 'N', 'C']`. Loops are much less frequent in the data science practice, because NumPy and Pandas provide **vectorized functions**, that, when applied to a data container such as a Pandas series, return a data container with same shape, whose terms are the values of the function on the corresponding terms of the original data container. 

Also ubiquitous in programming is **conditional logic**, operationalized through **if-then-else** commands. You also have this in Python. For instance, if you wish to create a dummy flag for names with more than 5 letters in the list `mylist`, you can do it with:

`flaglist = [1 if len(name) > 5 else 0 for name in mylist]`

This would return `[0, 1, 0, 1]`. It is also less frequent to find explicit if-the-else arguments in data science, since "vectorial" syntax is preferred (and typically leads to a faster execution).
