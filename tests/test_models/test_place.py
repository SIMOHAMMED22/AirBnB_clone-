#!/usr/bin/python3
"""Unit Test"""
from models.place import Place
import unittest
from datetime import datetime

class TestPlace(unittest.TestCase):
    """ ### """

    def test_type_updated_at(self):
        """ ### """
        p = Place()
        self.assertEqual(type(p.updated_at), datetime)
        
    def test_type_created_at(self):
        """ ### """
        p = Place()
        self.assertEqual(type(p.created_at), datetime)

    def test_type_id(self):
        """ ### """
        p = Place()
        self.assertEqual(type(p.id), str)

    def test_city_id(self):
        """ ### """
        p = Place()
        self.assertEqual(type(p.city_id), str)

    def test_user_id(self):
        """ ### """
        p = Place()
        self.assertEqual(type(p.user_id), str)

    def test_name(self):
        """ ### """
        p = Place()
        self.assertEqual(type(p.name), str)

    def test_description(self):
        """ ### """
        p = Place()
        self.assertEqual(type(p.description), str)

    def test_number_rooms(self):
        """ ### """
        p = Place()
        self.assertEqual(type(p.number_rooms), int)

    def test_number_bathrooms(self):
        """ ### """
        p = Place()
        self.assertEqual(type(p.number_bathrooms), int)

    def test_max_guest(self):
        """ ### """
        p = Place()
        self.assertEqual(type(p.max_guest), int)

    def test_price_by_night(self):
        """ ### """
        p = Place()
        self.assertEqual(type(p.price_by_night), int)

    def test_latitude(self):
        """ ### """
        p = Place()
        self.assertEqual(type(p.latitude), float)

    def test_longitude(self):
        """ ### """
        p = Place()
        self.assertEqual(type(p.longitude), float)

    def test_amenity_ids(self):
        """ ### """
        p = Place()
        self.assertEqual(type(p.amenity_ids), list)



if __name__ == '__main__':
    unittest.main()
