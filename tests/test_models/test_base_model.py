#!/usr/bin/python3
"""Unit Test"""

from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ ### """

    def test_type_updated_at(self):
        """ ### """
        b = BaseModel()
        self.assertEqual(type(b.updated_at), datetime)
        
    def test_type_created_at(self):
        """ ### """
        b = BaseModel()
        self.assertEqual(type(b.created_at), datetime)

    def test_type_id(self):
        """ ### """
        b = BaseModel()
        self.assertEqual(type(b.id), str)

    def test_to_dict(self):
        """###"""
        b = BaseModel()
        dic = b.to_dict()
        self.assertEqual(dic['__class__'], b.__class__.__name__)
        self.assertNotEqual(type(dic['created_at']), datetime)
        self.assertNotEqual(type(dic['updated_at']), datetime)

    def test__str__(self):
        """###"""
        b = BaseModel()
        stg = f"[{b.__class__.__name__}] ({b.id}) {b.__dict__}"
        self.assertEqual(str(b), stg)

    def test_save(self):
        """###"""
        b = BaseModel()
        upd_at = b.updated_at
        b.save()
        self.assertNotEqual(b.updated_at, upd_at)
        self.assertEqual(type(b.updated_at), type(datetime.now()))


if __name__ == '__main__':
    unittest.main()
