from dataclasses import is_dataclass
import unittest
from unittest.mock import patch
import uuid
from __seedwork.domain.exceptions import InvalidUuidException

from __seedwork.domain.value_objects import UniqueEntityId


class TestUniqueEntityId(unittest.TestCase):
  
  def test_if_is_a_dataclass(self):
    self.assertTrue(is_dataclass(UniqueEntityId))

  def test_throw_exception_when_uuid_is_valid(self):
    with patch.object(
      UniqueEntityId,
      '_UniqueEntityId__validate', 
      autospec=True,
      side_effect=UniqueEntityId._UniqueEntityId__validate) as mock_validate:
      with self.assertRaises(InvalidUuidException) as assert_error:
        UniqueEntityId('fake id')
      mock_validate.assert_called_once()
      self.assertEqual(assert_error.exception.args[0], 'ID must be a valid UUID')

  def test_accept_uuid_passed_in_constructor(self):
    with patch.object(
      UniqueEntityId,
      '_UniqueEntityId__validate', 
      autospec=True,
      side_effect=UniqueEntityId._UniqueEntityId__validate) as mock_validate:
      value_object = UniqueEntityId('45b4cf8a-ff89-4892-b5ea-6b5d8e3a91ce')
      mock_validate.assert_called_once()
      self.assertEqual(value_object.id, '45b4cf8a-ff89-4892-b5ea-6b5d8e3a91ce')

      uuid_value = uuid.uuid4()
      value_object = UniqueEntityId(uuid_value)
      self.assertEqual(value_object.id, str(uuid_value))


  def test_generate_id_when_no_passed_id_in_constructor(self):
    with patch.object(
      UniqueEntityId,
      '_UniqueEntityId__validate', 
      autospec=True,
      side_effect=UniqueEntityId._UniqueEntityId__validate) as mock_validate:
      value_object = UniqueEntityId()
      uuid.UUID(value_object.id)
      mock_validate.assert_called_once()

