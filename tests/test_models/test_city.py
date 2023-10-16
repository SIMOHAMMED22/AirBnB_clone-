#!/usr/bin/python3
"""Unit Test"""
from models.city import City
import unittest
from datetime import datetime

class TestCity(unittest.TestCase):
    """ ### """

    def test_type_updated_at(self):
        """ ### """
        c = City()
        self.assertEqual(type(c.updated_at), datetime)
        
    def test_type_created_at(self):
        """ ### """
        c = City()
        self.assertEqual(type(c.created_at), datetime)

    def test_type_id(self):
        """ ### """
        c = City()
        self.assertEqual(type(c.id), str)

    def test_name(self):
        """ ### """
        c = City()
        self.assertEqual(type(c.name), str)

    def test_state_id(self):
        """ ### """
        c = City()
        self.assertEqual(type(c.state_id), str)

if __name__ == '__main__':
    unittest.main()
