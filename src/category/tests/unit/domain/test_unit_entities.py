from dataclasses import is_dataclass
from datetime import datetime
import unittest
from category.domain.entities import Category

class TestCategory(unittest.TestCase):

  def test_if_is_a_dataclass(self):
    self.assertTrue(is_dataclass(Category))

  def test_constructor(self):

    category = Category(name='Movie')
    self.assertEqual(category.name, 'Movie')
    self.assertEqual(category.description, None)
    self.assertEqual(category.is_active, True)
    self.assertIsInstance(category.created_at, datetime)

    created_at = datetime.now()
    category = Category(name='Movie', description='Some descrition', is_active=True, created_at=created_at)
    self.assertEqual(category.name, 'Movie')
    self.assertEqual(category.description, 'Some descrition')
    self.assertEqual(category.is_active, True)
    self.assertIsInstance(category.created_at, datetime)
  
  def test_if_created_at_is_generated_in_contructor(self):
    category1 = Category('Movie1')
    category2 = Category('Movie2')
    self.assertNotEqual(category1.created_at.timestamp(), category2.created_at.timestamp())
    