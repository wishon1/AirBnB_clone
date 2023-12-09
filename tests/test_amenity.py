#!/usr/bin/python3
""" test module for class amenity"""
from models.amenity import Amenity
import unittest

class test_amenity(unittest.TestCase):
    """ test class for the amenity """
    def test_amenity_module(self):
        """ test module for the class amenity """
        amenity_obj = Amenity()

        self.assertEqual(amenity_obj.name, "")

        string_form = str(amenity_obj)
        self.assertIn("[Amenity]", string_form)
        self.assertIn(amenity_obj.id, string_form)
        self.assertIn(str(amenity_obj.__dict__), string_form)
