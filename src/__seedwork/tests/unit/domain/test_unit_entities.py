
from abc import ABC
from __seedwork.domain.entities import Entity
from dataclasses import dataclass, is_dataclass
import unittest

from __seedwork.domain.value_objects import UniqueEntityId


@dataclass(frozen=True, kw_only=True)
class StubEntity(Entity):
    props1: str
    props2: str


class TestEntityUnit(unittest.TestCase):

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Entity))

    def test_if_is_a_abstract_class(self):
        self.assertIsInstance(Entity(), ABC)

    def test_set_unique_entity_id_and_props(self):
        entity = StubEntity(props1='value1', props2='value2')
        self.assertEqual(entity.props1, 'value1')
        self.assertEqual(entity.props2, 'value2')
        self.assertIsInstance(entity.unique_entity_id, UniqueEntityId)
        self.assertEqual(entity.unique_entity_id.id, entity.id)

    def test_accept_a_uuid(self):
        entity = StubEntity(
            unique_entity_id=UniqueEntityId(
                '45b4cf8a-ff89-4892-b5ea-6b5d8e3a91ce'),
            props1='value1',
            props2='value2',
        )
        self.assertEqual(entity.id, '45b4cf8a-ff89-4892-b5ea-6b5d8e3a91ce')

    def test_to_dict_method(self):
        entity = StubEntity(
            unique_entity_id=UniqueEntityId(
                '45b4cf8a-ff89-4892-b5ea-6b5d8e3a91ce'),
            props1='value1',
            props2='value2',
        )
        self.assertDictEqual(entity.to_dict(), {
            'id': '45b4cf8a-ff89-4892-b5ea-6b5d8e3a91ce',
            'props1': 'value1',
            'props2': 'value2'
        })
