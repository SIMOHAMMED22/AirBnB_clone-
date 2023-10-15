#!/usr/bin/python3
"""Unit Test"""
from models.user import User
import unittest
from datetime import datetime

class TestUser(unittest.TestCase):
    """ ### """

    def test_type_updated_at(self):
        """ ### """
        b = User()
        self.assertEqual(type(b.updated_at), datetime)
        
    def test_type_created_at(self):
        """ ### """
        b = User()
        self.assertEqual(type(b.created_at), datetime)

    def test_type_id(self):
        """ ### """
        b = User()
        self.assertEqual(type(b.id), str)

if __name__ == '__main__':
    unittest.main()
