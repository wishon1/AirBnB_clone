#!/usr/bin/python3
""" test case for the base model class """
import io
import sys
import unittest
from models.base_model import BaseModel
class Test_Base_model_class(unittest.TestCase):
    """ Test Base model class """
    def test_str(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        my_model = BaseModel()
        print(my_model)

        my_model.save()
        print(my_model)

        #print( my_model.to_dict())

        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(
            ), f"{my_model.__class__.__name__}, {my_model.id}, {my_model.__dict__}\n",
               f"{my_model.__class__.__name__}, {my_model.id}, {my_model.__dict__}")
