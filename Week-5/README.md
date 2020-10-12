## Testing

Software testing is a process of evaluating computer code to determine whether or not it does what you expect it to do. When you test a piece of software, you want to find the errors and defects and see where things go wrong.

### Manual Testing
Executing a script with different command-line arguments to see how its behavior changed is an example of manual testing. Using the interpreter to try our code before putting it in a script is another form of manual testing.

### Automatic Testing
Formal software testing takes us process a step further, codifying tests into its own software and code that can be run to verify that our programs do what we expect them to do. This is called automatic testing. The goal of automatic testing is to automate the process of checking if the returned value matches the expectations.

### Unit Tests
Unit tests are used to verify that small isolated parts of a program are correct. Unit tests are generally written alongside the code to test the behavior of individual pieces or units like functions or methods. Unit tests help assure the developer that each piece of code does what it's meant to do.

### Edge Cases 
Edge cases are inputs to our code that produce unexpected results, and are found at the extreme ends of the ranges of input we imagine our programs will typically work with. Edge cases usually need special handling in scripts in order for the code to continue to behave correctly.

### Unit Test Cheat-Sheet

Frankly, the unit testing library for Python is fairly well documented, but it can be a bit of a dry read. Instead, we suggest covering the core module concepts, and then reading in more detail later.
Best of Unit Testing Standard Library Module

Understand a Basic Example:

- https://docs.python.org/3/library/unittest.html#basic-example

Understand how to run the tests using the Command Line:

- https://docs.python.org/3/library/unittest.html#command-line-interface

Understand various Unit Test Design Patterns:

- https://docs.python.org/3/library/unittest.html#organizing-test-code

- Understand the uses of setUp, tearDown; setUpModule and tearDownModule

Understand basic assertions:

|  |  |  |
|--|--|--|
|Method|Checks that|New in |
|assertEqual(a, b)|	a == b|	|
|assertNotEqual(a, b)|	a != b|	|
|assertTrue(x)|	bool(x) is True|	|
|assertFalse(x)|	bool(x) is False|	|
|assertIs(a, b)|	a is b|	3.1|
|assertIsNot(a, b)|	a is not b|	3.1|
|assertIsNone(x)|	x is None|	3.1|
|assertIsNotNone(x)|	x is not None|	3.1|
|assertIn(a, b)|	a in b|	3.1|
|assertNotIn(a, b)|	a not in b|	3.1|
|assertIsInstance(a, b)|	isinstance(a, b)|	3.2|
|assertNotIsInstance(a, b)|	not isinstance(a, b)|	3.2|

Understand more specific assertions such as assertRaises

- https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises

### Help with Jupyter Notebooks

We've aimed to make our Jupyter notebooks easy to use. But, if you get stuck, you can find more information [here](https://learner.coursera.help/hc/en-us/articles/360004995312-Solve-problems-with-Jupyter-Notebooks).

If you still need help, the discussion forums are a great place to find it! Use the forums to ask questions and source answers from your fellow learners.

If you want to learn more about Jupyter Notebooks as a technology, check out these resources:

- [Jupyter Notebook Tutorial](https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook), by datacamp.com
- [How to use Jupyter Notebooks](https://www.codecademy.com/articles/how-to-use-jupyter-notebooks), by codeacademy.com
- [Teaching and Learning with Jupyter](https://jupyter4edu.github.io/jupyter-edu-book/), by university professors using Jupyter