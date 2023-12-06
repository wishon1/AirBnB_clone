#!/usr/bin/python3
""" test case for the base model class """
import io
import sys
import unittest
from datetime import datetime
from models.base_model import BaseModel


class Test_Base_model_class(unittest.TestCase):
    """ Test Base model class """
    def test_func(self):
        """ test the method str, save, to_dict"""
        my_model = BaseModel()

        my_model.name = "first_model"
        my_model.my_number = 89

        s = str(my_model)
        self.assertIn("[BaseModel]", s)
        self.assertIn(my_model.id, s)
        self.assertIn(str(my_model.__dict__), s)

        my_model.save()

        s = str(my_model)
        self.assertIn("[BaseModel]", s)
        self.assertIn(my_model.id, s)
        self.assertIn(str(my_model.__dict__), s)

        d = my_model.to_dict()

        self.assertIsInstance(d, dict)

        self.assertIn("id", d)
        self.assertIn("created_at", d)
        self.assertIn("updated_at", d)
        self.assertIn("name", d)
        self.assertIn("my_number", d)
        self.assertIn("__class__", d)

    def test_04_baseModel(self):
        """ test attributes of basemodel after creation """
        my_model = BaseModel()
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)

        self.assertIsNotNone(my_new_model.id)
        self.assertIsInstance(my_new_model.created_at, datetime)
        self.assertIsInstance(my_new_model.updated_at, datetime)
