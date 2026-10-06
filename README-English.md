# Python Engineering Handbook

A course notes and examples repository for Python beginners. The main content is organized from the course materials, with an additional learning path and supplementary notes based on *Python Programming: An Introduction and Practice (Micro Video Edition)*.

This repository follows a simple progression: understand the fundamentals, practice with focused examples, and develop clear, maintainable, reusable coding habits.

## Learning Path

The recommended learning order is:

`Python environment -> Basic syntax -> Conditionals and loops -> Functions and modules -> Containers -> Classes and files -> Exceptions -> Built-in functions -> Multithreading -> pip -> NumPy`

The examples are stored under `src/`. Each course directory uses a three-digit number and an English name so that the repository is easy to browse and search on GitHub.

## Directory Structure

```text
python-engineering-handbook/
├── README.md
├── README-English.md
├── docs/
│   └── Python编程入门与实践-清华大学.pdf
└── src/
    ├── 001-python-introduction-and-installation/
    ├── 002-first-hello-world-program/
    ├── 003-python-basic-syntax/
    ├── 004-python-conditional-statements/
    ├── 005-python-loops/
    ├── 006-python-functions-and-modules/
    ├── 007-python-containers-and-operations/
    ├── 008-python-classes-and-file-operations/
    ├── 009-python-exception-handling/
    ├── 010-python-built-in-functions/
    ├── 011-python-multithreading/
    ├── 012-python-pip-usage/
    └── 013-python-numpy-basics/
```

## Main Curriculum

The main curriculum follows the 13 course topics in the course materials. Each topic has a runnable example under `src/`.

### 001 Python Introduction and Installation

Learn Python's language characteristics, cross-platform nature, runtime inspection, and the basic difference between procedural and object-oriented design.

Example: [`python_environment.py`](src/001-python-introduction-and-installation/python_environment.py)

### 002 First Program: Hello World

Learn string representation, `print()`, printing multiple objects, `sep`, `end`, and simple expressions.

Example: [`hello_world.py`](src/002-first-hello-world-program/hello_world.py)

### 003 Python Basic Syntax

Learn comments, indentation, PEP 8, identifiers, keywords, and the basic data types: numbers, strings, lists, tuples, dictionaries, and sets.

Example: [`basic_syntax.py`](src/003-python-basic-syntax/basic_syntax.py)

### 004 Python Conditional Statements

Learn arithmetic and comparison operators, logical operators, membership tests, and the `if`, `elif`, and `else` multi-branch structure.

Example: [`bmi_calculator.py`](src/004-python-conditional-statements/bmi_calculator.py)

### 005 Python Loops

Learn `while`, `for`, `break`, `continue`, `pass`, factorial calculation, and string traversal.

Example: [`loops_demo.py`](src/005-python-loops/loops_demo.py)

### 006 Python Functions and Modules

Learn function definitions and return values, positional arguments, default arguments, variable-length arguments, keyword arguments, mutability, and module imports.

Example: [`functions_and_modules.py`](src/006-python-functions-and-modules/functions_and_modules.py)

### 007 Python Containers and Operations

Learn the characteristics of lists, tuples, sets, and dictionaries, together with common add, delete, update, query, deduplication, and update operations.

Example: [`containers_and_operations.py`](src/007-python-containers-and-operations/containers_and_operations.py)

### 008 Python Classes and File Operations

This topic follows the two sections in the courseware.

#### Classes and Objects

Learn classes and objects, attributes, constructors, inheritance, polymorphism, and method overriding.

Example: [`classes_and_objects.py`](src/008-python-classes-and-file-operations/classes_and_objects.py)

#### File Operations

Learn file names, paths, text files, binary files, and reading, writing, and appending file content.

Example: [`file_operations.py`](src/008-python-classes-and-file-operations/file_operations.py)

### 009 Python Exception Handling

Learn common exceptions, `try`, `except`, `else`, and `finally`, as well as catching only exceptions that can be handled explicitly.

Example: [`exception_handling.py`](src/009-python-exception-handling/exception_handling.py)

### 010 Python Built-in Functions

Learn numeric operations, type conversion, base conversion, sequence processing, sorting, filtering, mapping, aggregation, and object inspection.

Example: [`built_in_functions.py`](src/010-python-built-in-functions/built_in_functions.py)

### 011 Python Multithreading

Learn processes and threads, `threading.Thread`, `join()`, shared data, and synchronization with `RLock`.

Example: [`threading_demo.py`](src/011-python-multithreading/threading_demo.py)

### 012 Python pip Usage

Learn what pip does, how to inspect its version, list packages, inspect package information, and understand installation and removal command formats.

Example: [`pip_usage.py`](src/012-python-pip-usage/pip_usage.py)

### 013 Python NumPy Basics

Learn array creation, indexing, slicing, Boolean filtering, reshaping, combining, and splitting arrays.

Example: [`numpy_basics.py`](src/013-python-numpy-basics/numpy_basics.py)

## Running the Examples

Python 3.9 or later is recommended. Check the installed Python version:

```bash
python --version
```

Run a regular example:

```bash
python src/002-first-hello-world-program/hello_world.py
python src/003-python-basic-syntax/basic_syntax.py
```

Run an interactive example:

```bash
python src/004-python-conditional-statements/bmi_calculator.py
python src/005-python-loops/loops_demo.py
```

Install the NumPy dependency before running the NumPy example:

```bash
python -m pip install numpy
python src/013-python-numpy-basics/numpy_basics.py
```

Except for the NumPy example, the main course examples primarily use the Python standard library. `pip_usage.py` only checks the pip version and displays command patterns; it does not install or uninstall packages automatically.

## Engineering Conventions

 - Each example can run as an independent script.
 - `if __name__ == "__main__":` is used as the script entry point.
 - Functions and classes use Chinese docstrings to describe responsibilities, parameters, return values, and expected exceptions.
 - Prefer clear naming, explicit boundary validation, and standard-library capabilities.
 - Use context managers for file resources and locks to protect shared data in threads.
 - Keep each example focused on one topic and avoid unrelated complexity.
 - When validating code, pay attention to syntax, input boundaries, resource cleanup, and reproducibility.

## Supplementary Notes: Reference Book

The following notes are based on the chapter structure of *Python Programming: An Introduction and Practice (Micro Video Edition)* and a comparison with the current courseware. This section records topics that are not systematically covered by the courseware; no new code implementation is included.

### Supplement 1: Development Tools and Help Systems

The courseware introduces the Python environment and PyCharm. The reference book also introduces how to start, edit, run, and debug programs with IDLE. The three tools have different roles:

 - The command-line interpreter is useful for quickly testing syntax and expressions.
 - IDLE helps beginners observe interactive execution, editing, and debugging.
 - PyCharm is useful for organizing projects, managing interpreters, running scripts, and maintaining larger codebases.

The reference book also emphasizes the built-in help system, including help for built-in functions, types, module members, and complete modules. When an unfamiliar standard-library interface appears, inspect the object's own help information before consulting external documentation.

### Supplement 2: Variables, Constants, and Expressions

The reference book further distinguishes variables, constants, null values, type conversion, operators, and expressions. Key points include:

 - `None` represents no value or a result that is not available yet. It is different from `0`, an empty string, and `False`.
 - A variable stores a reference to an object; assignment is not the same as copying the object.
 - Constants are conventionally named with uppercase letters and underscores. Python mainly communicates constant intent through naming conventions.
 - Type conversion should account for the source of the data and possible failure. External input should usually be validated before conversion.
 - Keep expressions simple. Break complex calculations into meaningful intermediate values.

### Supplement 3: Common Algorithmic Thinking

The courseware covers basic conditions and loops. The reference book also organizes common approaches such as accumulation and multiplication, finding maximum and minimum values, enumeration, recurrence, and iteration.

 - Accumulation and multiplication are suitable for aggregating values one by one.
 - Maximum and minimum problems require an explicit initial value and a clear empty-sequence policy.
 - Enumeration searches candidate solutions by traversal. The candidate space and stopping condition must be defined first.
 - Recurrence derives the next state from one or more previous states, while iteration emphasizes repeatedly updating state.
 - Before writing a loop, define the initialization, loop condition, state change, and final result.

### Supplement 4: Advanced Functions

The courseware introduces function parameters and module imports. The reference book additionally covers lambda expressions, variable scope, closures, and recursive calls.

 - Lambda expressions are suitable for short, one-off function logic. Use a named function for complex logic.
 - Understand local, enclosing, and global scope, and minimize implicit dependencies.
 - Closures can preserve state from an enclosing function, but state changes should remain easy to trace.
 - Recursion requires a clear base case to avoid infinite calls. When a simple loop expresses the same logic, readability and resource usage should guide the choice.

### Supplement 5: Advanced File and Directory Operations

The courseware covers basic text-file access. The reference book additionally discusses file seeking, binary files, the current working directory, directory operations, and file operations.

 - The file pointer determines where the next read or write occurs. Understand the meaning of `seek` and `tell` when using random access.
 - Binary files should be handled as bytes; their content should not be assumed to be text.
 - Prefer `pathlib` for path handling to reduce cross-platform path-separator problems.
 - Distinguish checking, creating, traversing, copying, moving, and deleting files and directories.
 - Confirm the target path and operation scope before deleting or overwriting anything.

### Supplement 6: Advanced Object-Oriented Design

The courseware introduces classes, objects, inheritance, and polymorphism. The reference book additionally covers destructors, private and public members, multiple inheritance, and operator overloading.

 - A constructor establishes a valid initial state for an object.
 - A destructor should not carry critical business logic because object-destruction timing is not a reliable resource-management mechanism.
 - Private members are part of encapsulation and access-control design. The key goal is to protect object invariants.
 - Multiple inheritance increases the complexity of method resolution and responsibility composition, so it should have a clear design reason.
 - Operator overloading should have intuitive semantics and match users' expectations for the operator.

### Supplement 7: GUI Programming Basics

Chapter 7 of the reference book introduces Tkinter, while the current courseware does not cover GUI programming. First understand the difference between GUI and command-line programs:

 - A GUI program consists of windows, widgets, layouts, and events.
 - Widgets display information or receive input, while event handlers respond to user actions.
 - The main event loop continuously receives and dispatches events. Long blocking tasks can make the interface unresponsive.
 - Layout design should consider component hierarchy, size, spacing, and usability.

This supplement does not provide Tkinter code.

### Supplement 8: Multiprocessing

The courseware introduces multithreading, while Chapter 8 of the reference book also introduces multiprocessing. Key points include:

 - Processes have relatively independent address spaces, while threads usually share memory within one process.
 - Multiprocessing is suitable when resource isolation or multi-core computation is needed, but process creation and communication cost more.
 - Processes cannot rely on ordinary variables for direct shared state. They need process-safe communication or shared-state mechanisms.
 - Choose between threads and processes based on task type, shared state, isolation requirements, and the deployment environment.

This supplement does not provide `multiprocessing` code.

### Supplement 9: Database Access and SQL

Chapter 9 of the reference book introduces database fundamentals, relational databases, SQL, and SQLite3, none of which are covered systematically by the current courseware. Important concepts include:

 - Databases persist and manage structured data.
 - Tables consist of fields and records, and a primary key uniquely identifies a record.
 - `SELECT` queries data, `INSERT` adds records, `UPDATE` changes records, and `DELETE` removes records.
 - Parameterized queries separate SQL structure from external input and avoid directly concatenating user input into SQL strings.
 - Database work must account for connections, transactions, commits, rollbacks, and resource cleanup.

This supplement does not provide SQLite or SQL code.

### Supplement 10: Image Processing

Chapter 10 of the reference book introduces Pillow, including image I/O, text and shape drawing, filters, watermarks, verification codes, and QR codes. The current courseware does not cover image processing.

 - Image objects manage pixel data and basic properties.
 - Drawing modules add text, lines, and shapes to images.
 - Font modules control text rendering, and font files affect cross-platform display.
 - Filters change the appearance of an image. Watermarks and verification codes are typical image-composition tasks.
 - QR-code generation usually requires an additional third-party dependency and an explicit output format.

This supplement does not provide Pillow code.

### Supplement 11: Network Programming

Chapter 11 of the reference book introduces networking fundamentals, TCP/UDP, network sniffers, port scanners, and web crawlers. The current courseware does not cover network programming. Establish clear boundaries first:

 - TCP is connection-oriented and emphasizes reliable, ordered byte-stream delivery.
 - UDP is connectionless and has lower overhead, but does not guarantee delivery or ordering.
 - Network programs must handle timeouts, disconnections, partial messages, encoding, resource cleanup, and exceptions.
 - Web crawlers should follow service terms, rate limits, `robots.txt`, and data-privacy requirements.
 - Sniffing and port scanning involve security boundaries and must only be performed in explicitly authorized environments.

This supplement does not provide networking, sniffer, or port-scanner code.

## References

 - Course examples: [`src/`](src/)
 - Reference book: [`Python编程入门与实践-清华大学.pdf`](docs/Python编程入门与实践-清华大学.pdf)
 - Python documentation: https://docs.python.org/zh-cn/
 - NumPy documentation: https://numpy.org/doc/

## Notes

The examples in this repository are intended for learning and practice. They are simplified and should not be treated as complete production solutions. For files, threads, databases, networks, and third-party libraries, add the appropriate permissions, logging, tests, timeouts, and resource-management strategies for the actual environment.
