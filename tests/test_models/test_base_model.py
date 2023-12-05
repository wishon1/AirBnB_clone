#!/usr/bin/python3
""" test case for the base model class """
import unittest

class Test_Base_model_class(unittest.TestCase):
    """ Test Base model class """
    my_model = BaseModel()
    self.assertEqual(my_model.id, uuid.uuid4())
    self.assertEqual(my_model.created_at, 
