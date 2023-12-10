#!/usr/bin/python3
""" module to test the review class"""
from models.review import Review
import unittest


class test_review(unittest.TestCase):
    """ class to test for the review class """
    def test_review_class(self):
        """ test the review module """
        review_obj = Review()

        self.assertEqual(review_obj.place_id, "")
        self.assertEqual(review_obj.user_id, "")
        self.assertEqual(review_obj.text, "")

        string_form = str(review_obj)
        self.assertIn("[Review]", string_form)
        self.assertIn(review_obj.id, string_form)
        self.assertIn(str(review_obj.__dict__), string_form)
