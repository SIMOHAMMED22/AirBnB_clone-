#!/usr/bin/python3
"""Unit Test"""
from models.state import State
import unittest
from datetime import datetime

class TestState(unittest.TestCase):
    """ ### """

    def test_type_updated_at(self):
        """ ### """
        b = State()
        self.assertEqual(type(b.updated_at), datetime)
        
    def test_type_created_at(self):
        """ ### """
        b = State()
        self.assertEqual(type(b.created_at), datetime)

    def test_type_id(self):
        """ ### """
        b = State()
        self.assertEqual(type(b.id), str)

if __name__ == '__main__':
    unittest.main()
