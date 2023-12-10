#!/usr/bin/python3
""" module to test the city class"""
from models.city import City
import unittest


class test_city(unittest.TestCase):
    """ class to test for the city """
    def test_city_class(self):
        """ test the city """
        city_obj = City()

        self.assertEqual(city_obj.state_id, "")
        self.assertEqual(city_obj.name, "")

        string_form = str(city_obj)
        self.assertIn("[City]", string_form)
        self.assertIn(city_obj.id, string_form)
        self.assertIn(str(city_obj.__dict__), string_form)
