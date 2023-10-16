#!/usr/bin/python3
"""Unit Test"""
from models.review import Review
import unittest
from datetime import datetime

class TestReview(unittest.TestCase):
    """ ### """

    def test_type_updated_at(self):
        """ ### """
        r = Review()
        self.assertEqual(type(r.updated_at), datetime)
        
    def test_type_created_at(self):
        """ ### """
        r = Review()
        self.assertEqual(type(r.created_at), datetime)

    def test_type_id(self):
        """ ### """
        r = Review()
        self.assertEqual(type(r.id), str)

    def test_place_id(self):
        """ ### """
        r = Review()
        self.assertEqual(type(r.place_id), str)

    def test_user_id(self):
        """ ### """
        r = Review()
        self.assertEqual(type(r.user_id), str)

    def test_text(self):
        """ ### """
        r = Review()
        self.assertEqual(type(r.text), str)

if __name__ == '__main__':
    unittest.main()
