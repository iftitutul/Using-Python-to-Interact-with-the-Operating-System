#!/usr/bin/env python3.6

import unittest
from testing import rearrange_name  # from <script_name> import <function_name>

class TestRearrange(unittest.TestCase):
   def test_basic(self):
      testcase = "Lovelace, Ada"
      expected = "Ada Lovelace"
      self.assertEqual(rearrange_name(testcase), expected)
   
   # for edge cases run sucessfully, use below code
   # if result is None:
   #   return ""
   def test_empty(self):
      testcase = ""
      expected = ""
      self.assertEqual(rearrange_name(testcase), expected)

   def test_double_name(self):
      testcase = "Hopper, Grace M."
      expected = "Grace M. Hopper"
      self.assertEqual(rearrange_name(testcase), expected)

   def test_single_name(self):
      testcase = "Voltaire"
      expected = "Voltaire"
      self.assertEqual(rearrange_name(testcase), expected)

unittest.main()

