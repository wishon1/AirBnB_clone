#!/usr/bin/python3
""" test module for class amenity"""
from models.place import Place
import unittest

class test_place(unittest.TestCase):
    """ test class for the amenity """
    def test_place_module(self):
        """ test module for the class amenity """
        place_obj = Place()

        self.assertEqual(place_obj.name, "")
        self.assertEqual(place_obj.city_id, "")
        self.assertEqual(place_obj.user_id, "")
        self.assertEqual(place_obj.description, "")
        self.assertEqual(place_obj.number_rooms, 0)
        self.assertEqual(place_obj.number_bathrooms, 0)
        self.assertEqual(place_obj.max_guest, 0)
        self.assertEqual(place_obj.price_by_night, 0)
        self.assertEqual(place_obj.latitude, 0)
        self.assertEqual(place_obj.longitude, 0)
        self.assertEqual(place_obj.amenity_ids, [])

        string_form = str(place_obj)
        self.assertIn("[Place]", string_form)
        self.assertIn(place_obj.id, string_form)
        self.assertIn(str(place_obj.__dict__), string_form)
