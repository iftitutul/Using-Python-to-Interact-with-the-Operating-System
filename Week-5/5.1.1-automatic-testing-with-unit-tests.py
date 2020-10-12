#!/usr/bin/env python3.6

from testing import rearrange_name  # from <script_name> import <function_name>
import unittest

class TestRearrange(unittest.TestCase):
   def test_basic(self):
      testcase = "Lovelace, Ada"
      expected = "Ada Lovelace"
      self.assertEqual(rearrange_name(testcase),expected)

unittest.main()
