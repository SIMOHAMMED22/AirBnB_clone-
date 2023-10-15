#!/usr/bin/python3
"""Unit Test"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest

class TestFileStorage(unittest.TestCase):
    """ ### """

    def test_file_path(self):
        """ ### """
        f = FileStorage()
        self.assertEqual(f.__file_path, 'file.json')

    def test_type_objects(self):
        """ ### """
        f = FileStorage()
        self.assertEqual(f.__objects, {})

    def test_all_func(self):
        """ ### """
        f = FileStorage()
        self.assertEqual(f.all(), {})

    def test_new_func(self):
        """ ### """
        b = BaseModel()
        f = FileStorage()
        f.new(b)
        key = "BaseModel." + b.id
        self.assertEqual(f.all()[key], b)

if __name__ == '__main__':
    unittest.main()
