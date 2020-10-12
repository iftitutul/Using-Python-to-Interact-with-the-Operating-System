#!/usr/bin/env python3.6

#!/usr/bin/env python3.6

import unittest
# from <script_name> import <function_name>
from validations import validate_user

class TestValidateUser(unittest.TestCase):
   def test_valid(self):
      self.assertEqual(validate_user("validuser", 3), True)
   
   def test_too_short(self):
      self.assertEqual(validate_user("inv", 5), False)

   def test_invalid_characters(self):
      self.assertEqual(validate_user("invalid_user", 1), False)

   def test_invalid_min(self):
      self.assertRaises(ValueError, validate_user, "user", -1)

# Run the tests
unittest.main()
