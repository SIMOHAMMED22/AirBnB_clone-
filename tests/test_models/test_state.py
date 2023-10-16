#!/usr/bin/python3
"""Unit Test"""
from models.state import State
import unittest
from datetime import datetime

class TestState(unittest.TestCase):
    """ ### """

    def test_type_updated_at(self):
        """ ### """
        s = State()
        self.assertEqual(type(s.updated_at), datetime)
        
    def test_type_created_at(self):
        """ ### """
        s = State()
        self.assertEqual(type(s.created_at), datetime)

    def test_type_id(self):
        """ ### """
        s = State()
        self.assertEqual(type(s.id), str)

    def test_name(self):
        """ ### """
        s = State()
        self.assertEqual(type(s.name), str)

if __name__ == '__main__':
    unittest.main()
