#!/usr/bin/python3
"""Unit Test"""
from models.engine.file_storage import FileStorage
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

if __name__ == '__main__':
    unittest.main()
