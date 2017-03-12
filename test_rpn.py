import unittest
import rpn


class TestBasics(unittest.TestCase):
  def test_add(self):
    result = rpn.calculate("1 1 +")
    self.assertEqual(2, result)
    result = rpn.calculate("2 5 + 2 2 + +")
    self.assertEqual(11, result)
    result = rpn.calculate("1 2 3 +")
    self.assertEqual(None, result)

  def test_sub(self):
    result = rpn.calculate("19 5 -")
    self.assertEqual(14, result)

  def test_fail(self):
    result = rpn.calculate("19 -")
    self.assertEqual(None, result)

  def test_mult(self):
    result = rpn.calculate("5 2 * 10 *")
    self.assertEqual(100, result)

  def test_div(self):
    result = rpn.calculate("5 2 / 2 /")
    self.assertEqual(1.25, result)

  def test_combine(self):
    result = rpn.calculate("1 1 + 2 *")
    self.assertEqual(4, result)
  def test_exp(self):
    result = rpn.calculate("4 3 ^")
    self.assertEqual(64, result)

