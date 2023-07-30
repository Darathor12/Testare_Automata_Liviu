# Unit Test Library

## Introduction

The `unittest` library in Python is a built-in module that provides a framework for writing and running tests. It is part of the Python standard library, so there is no need to install any additional packages.

Using `unittest`, you can create test cases, organize them into test suites, and execute them to verify the correctness of your code. The library follows the xUnit style of testing and provides a rich set of methods and decorators to facilitate test creation and execution.

The main components and concepts of unittest are: create tests, important methods, decorators.

**1. Test Case:**

- A test case is the smallest unit of testing in `unittest`. It represents an individual test scenario or condition that you want to verify.
- To create a test case, you need to define a class that inherits from the `unittest.TestCase` class.
- In the test case class, you write test methods that begin with the word `test` to indicate that they should be executed as tests.

Example:

```python
import unittest

class MyTestCase(unittest.TestCase):
    def test_addition(self):
        result = 2 + 2
        self.assertEqual(result, 4)

    def test_subtraction(self):
        result = 5 - 3
        self.assertEqual(result, 2)
```

**2. Test Suite:**

- A test suite is a collection of test cases that can be executed together.
- `unittest` provides a `TestSuite` class to create and manage test suites.
- Test suites allow you to organize your tests and run them selectively.


Example:

```python
import unittest

class MyTestCase(unittest.TestCase):
    
    # Test case definitions...
    pass

# Create a test suite
suite = unittest.TestSuite()
suite.addTest(MyTestCase('test_addition'))
suite.addTest(MyTestCase('test_subtraction'))

# Run the test suite
unittest.TextTestRunner().run(suite)
```

**3. Test Runner:**

- The test runner is responsible for discovering and executing the tests.
- `unittest` provides various test runners, including the `TextTestRunner`, which displays test results in the console, and the `HTMLTestRunner`, which generates HTML reports.

Example:

```python
import unittest

class MyTestCase(unittest.TestCase):
    # Test case definitions...
    pass
# Create a test suite
suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

# Run the test suite using the TextTestRunner
unittest.TextTestRunner().run(suite)
```

**4. Assertion Methods:**

- Assertion methods are used to validate the expected results of your tests.
- `unittest` provides a wide range of assertion methods to check conditions such as equality, inequality, truthiness, exceptions, and more.

Important Assertion Methods:

- `assertEqual(a, b)`: Checks if a and b are equal.
- `assertNotEqual(a, b)`: Checks if a and b are not equal.
- `assertTrue(x)`: Checks if x is true.
- `assertFalse(x)`: Checks if x is false.
- `assertRaises(exception, callable, *args, **kwargs)`: Checks if callable raises exception when called with the specified arguments.

Example:

```python
import unittest

class MyTestCase(unittest.TestCase):
    def test_addition(self):
        result = 2 + 2
        self.assertEqual(result, 4)

    def test_division(self):
        self.assertRaises(ZeroDivisionError, lambda: 1 / 0)
```

**5. Test Fixtures:**

- Test fixtures are methods that set up or clean up the test environment before and after each test method.
- `unittest` provides decorators to define test fixtures: `setUp()`, `tearDown()`, `setUpClass()`, and `tearDownClass()`.
- `setUp()` and `tearDown()` are executed before and after each test method, while `setUpClass()` and `tearDownClass()` are executed once per test case class.

Example:

```python
import unittest

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up class-level fixtures
        pass

    def setUp(self):
        # Set up test-level fixtures
        pass

    def tearDown(self):
        # Clean up test-level fixtures
        pass

    @classmethod
    def tearDownClass(cls):
        # Clean up class-level fixtures
        pass

    # Test methods...
```

These are the basic concepts and methods of the `unittest` library. You can build upon them to create more complex tests and test suites. Remember to import unittest at the beginning of your test script.

Template for unittest usage:

```python
import unittest

# Create a test case class that inherits from unittest.TestCase
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up class-level fixtures
        # This method is executed once before any tests in the test case class are run
        # You can use it to set up resources or configurations that are shared among all the tests
        # For example, initializing a database connection or loading test data
        pass

    def setUp(self):
        # Set up test-level fixtures
        # This method is executed before each test method in the test case class
        # You can use it to prepare any necessary resources or state for the individual test
        # For example, creating objects or initializing variables
        pass

    def tearDown(self):
        # Clean up test-level fixtures
        # This method is executed after each test method in the test case class
        # You can use it to clean up any resources or reset the state modified during the test
        # For example, closing connections or deleting temporary files
        pass

    @classmethod
    def tearDownClass(cls):
        # Clean up class-level fixtures
        # This method is executed once after all the tests in the test case class have been run
        # You can use it to perform any necessary cleanup actions for the entire test case
        # For example, releasing resources or closing connections
        pass

    # Test methods...
    # Here, you can define your individual test methods, each starting with the word "test"
    # These methods will be executed as separate tests

    def test_example(self):
        # Implement your test logic here
        # In this method, you can perform assertions to verify the behavior of your code
        # For example, calling functions and checking the expected output or behavior
        pass
```

First automation simulation example:

```python
import unittest

# Create a test case class that inherits from unittest.TestCase
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up class-level fixtures
        cls.shared_resource = "Initialized shared resource"

    def setUp(self):
        # Set up test-level fixtures
        self.test_data = [1, 2, 3]

    def tearDown(self):
        # Clean up test-level fixtures
        self.test_data = None

    @classmethod
    def tearDownClass(cls):
        # Clean up class-level fixtures
        cls.shared_resource = None

    def test_example(self):
        # Implement your test logic here
        result = sum(self.test_data)
        self.assertEqual(result, 6)

# Run the tests
if __name__ == "__main__":
    unittest.main()
```

### UnitTest Skip decorator:

**Decorator** `unittest.skip` :

- The `unittest.skip` decorator can be used to skip a test method declaratively.
- You can provide an optional reason parameter as a string to specify the reason for skipping the test.


```python
import unittest

class MyTestCase(unittest.TestCase):
    @unittest.skip("Skipping test_example for demonstration purposes")
    def test_example(self):
        # Test logic...
        pass
```

In this example, the `test_example` test method will be skipped with the reason "Skipping test_example for demonstration purposes". The `@unittest.skip` decorator is applied to the test method, indicating that the test should be skipped.





































































































