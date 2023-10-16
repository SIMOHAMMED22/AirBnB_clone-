#!/usr/bin/python3
"""Unit Test"""
from models.user import User
import unittest
from datetime import datetime

class TestUser(unittest.TestCase):
    """ ### """

    def test_type_updated_at(self):
        """ ### """
        u = User()
        self.assertEqual(type(u.updated_at), datetime)
        
    def test_type_created_at(self):
        """ ### """
        u = User()
        self.assertEqual(type(u.created_at), datetime)

    def test_type_id(self):
        """ ### """
        u = User()
        self.assertEqual(type(u.id), str)

    def test_email(self):
        """ ### """
        u = User()
        self.assertEqual(type(u.email), str)

    def test_first_name(self):
        """ ### """
        u = User()
        self.assertEqual(type(u.first_name), str)
        
    def test_last_name(self):
        """ ### """
        u = User()
        self.assertEqual(type(u.last_name), str)

    def test_password(self):
        """ ### """
        u = User()
        self.assertEqual(type(u.password), str)

if __name__ == '__main__':
    unittest.main()
