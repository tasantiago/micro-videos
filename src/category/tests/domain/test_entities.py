from datetime import datetime
import unittest
from category.domain.entities import Category

class TestCategory(unittest.TestCase):

  def test_constructor(self):
    category = Category('Movie', 'Some descrition', True, datetime.now())
    self.assertEqual(category.name, 'Movie')
    self.assertEqual(category.description, 'Some descrition')
    self.assertEqual(category.is_active, True)
    self.assertIsInstance(category.created_at, datetime)
