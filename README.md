# python-tests

This repository contains one module called `is_primary.py` with one function called `is_primary` that is meant to check whether a number is primary or not.

Next to it, there is a test file: `test_is_primary.py` that checks for some cases. Currently, one test out of five is "red".

To run the test, type in the shell:

```sh
python -m unittest
```

This will discover all test files and run all the tests and you'll get the following message:
```
..F..
======================================================================
FAIL: test_nine (test_is_primary.TestIsPrimary)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/walter/code/python-tests/test_is_primary.py", line 20, in test_nine
    self.assertFalse(is_primary(9))
AssertionError: True is not false

----------------------------------------------------------------------
Ran 5 tests in 0.000s

```

This means that the test that checks whether 9 is primary (it's not) failed: "True is not false".

There is a nicer way to run the test, but it requires installing one more package. Run in the shell:
```sh
sudo pip install pytest
```

And then:

```sh
pytest
```

And you'll get a nicer and more colorful report.

Now, all that's left is to fix the code in `is_primary.py`...
