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

### White-box Testing 
White box testing also sometimes called clear-box or transparent testing relies on the test creators knowledge of the software being tested to construct the test cases. With a white-box test, the test creator knows how the code works and can write test cases that use the understanding to make sure that everything is performing the way it's expected to. 

### Black Box Testing
In black-box testing, the software being tested is treated like an opaque box. In other words, the tester doesn't know the internals of how the software works. Black-box tests are written with an awareness of what the program is supposed to do, its requirements or specifications, but not how it does it.

### Integration Test
Integration tests verify that the interactions between the different pieces of code in integrated environments are working the way we expect them to. Integration test, usually take the individual modules of code that unit test verify then combine them into a group to test.

### Regression Test
A variant of unit tests our regression tests. They're usually written as part of a debugging and troubleshooting process to verify that an issue or error has been fixed once it's been identified. Regression tests are useful part of a test suite because they ensure that the same mistake doesn't happen twice.

### Smoke Test
Smoke test sometimes called build verification test, get their name from a concept that comes from testing hardware equipment. Plug in the given piece of hardware and see if smoke starts coming out of it. When writing software smoke test serve as a kind of sanity check to find major bugs in a program. Smoke test answer basic questions like, does the program run? These tests are usually run before more refined testing takes place. Since if the software fails the smoke test you can be pretty sure none of the other tests will pass either.

### Load Test
Load tests verify that the system behaves well when it's under significant load. To actually perform these tests will need to generate traffic to our application simulating typical usage of the service. These tests can be super-helpful when deploying new versions of our applications to verify that performance does not degrade.

### Test Driven Development
A process called test-driven development or TDD calls for creating the test before writing the code. This might seem a bit counter-intuitive, but it can make for more thoughtful well-written programs. When presented with a new problem that can be solved by automation, your gut instinct might be to fire up your code editor and start writing.

The test-driven development cycle typically involves first writing a test then running it to make sure it fails. After all, you haven't written the code to make it passed yet. Once you've verified it fails, you write the code that will satisfy the test then run the tests again. If it passes you can continue on to the next part of your program. If it fails you Debug and run the test again. The cycle is repeated for each new feature of your script until it's up and running.

### More About Tests

Check out the following links for more information:

- https://landing.google.com/sre/sre-book/chapters/monitoring-distributed-systems/
- https://landing.google.com/sre/sre-book/chapters/testing-reliability- 
- https://testing.googleblog.com/2007/10/performance-testing.html
- https://www.guru99.com/smoke-testing.html
- https://www.guru99.com/exploratory-testing.html
- https://testing.googleblog.com/2008/09/test-first-is-fun_08.html

### Handling Errors Cheat-Sheet

Raise allows you to throw an exception at any time.

- https://docs.python.org/3/tutorial/errors.html#raising-exceptions

Assert enables you to verify if a certain condition is met and throw an exception if it isn’t.

- https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement
- https://stackoverflow.com/questions/5142418/what-is-the-use-of-assert-in-python

The standard library documentation is kind of unclear. Basically `assert <something false>` will raise AssertionError, which the caller may need to handle.

In the try clause, all statements are executed until an exception is encountered.

- https://docs.python.org/3/tutorial/errors.html#handling-exceptions

Except is used to catch and handle the exception(s) that are encountered in the try clause.

- https://docs.python.org/3/library/exceptions.html#bltin-exceptions

Other interesting Exception handling readings:

- https://doughellmann.com/blog/2009/06/19/python-exception-handling-techniques/

### Help with Jupyter Notebooks

We've aimed to make our Jupyter notebooks easy to use. But, if you get stuck, you can find more information [here](https://learner.coursera.help/hc/en-us/articles/360004995312-Solve-problems-with-Jupyter-Notebooks).

If you still need help, the discussion forums are a great place to find it! Use the forums to ask questions and source answers from your fellow learners.

If you want to learn more about Jupyter Notebooks as a technology, check out these resources:

- [Jupyter Notebook Tutorial](https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook), by datacamp.com
- [How to use Jupyter Notebooks](https://www.codecademy.com/articles/how-to-use-jupyter-notebooks), by codeacademy.com
- [Teaching and Learning with Jupyter](https://jupyter4edu.github.io/jupyter-edu-book/), by university professors using Jupyter