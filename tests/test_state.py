#!/usr/bin/python3
""" Test model for the state class """
from models.state import State
import unittest


class test_state(unittest.TestCase):
    """ test case for class state """

    def test_case_state(self):
        """ module to test the state class """
        state_instance = State()

        self.assertEqual(state_instance.name, "")
        
        s = str(state_instance)
        self.assertIn("[State]", s)
        self.assertIn(state_instance.id, s)
        self.assertIn(str(state_instance.__dict__), s)
