#!/usr/bin/env python3.6
import unittest

from qwiklabemails import find_email


class EmailsTest(unittest.TestCase):

    def test_basic(self):
        testcase = [None, "Bree", "Campbell"]
        expected = "breee@abc.edu"
        self.assertEqual(find_email(testcase), expected)

    def test_one_name(self):  # Test Case 1: Missing parameters
        testcase = [None, "John"]
        expected = "Missing parameters"
        self.assertEqual(find_email(testcase), expected)

    def test_two_name(self): # Test Case 2: Random email address
        testcase = [None, "Roy", "Cooper"]
        expected = "No email address found"
        self.assertEqual(find_email(testcase), expected)


if __name__ == '__main__':
    unittest.main()
