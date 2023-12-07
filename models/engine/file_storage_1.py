#!/usr/bin/python3
"""
The file storage module
"""
from datetime import datetime
import os
from models.base_model import BaseModel
import json


class FileStorage():
    """
    That class will orginize all information of every object
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return the objects dictionary """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        element = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects.update({element:obj.__dict__})

    def save(self):
        """  serializes __objects to the JSON file (path: __file_path)"""
        for key, values in self.__objects.items():
            for value in values:
                if value == "updated_at" or value == "created_at":
                    values[value] = values[value].isoformat()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Deserialize the JSON file"""
        """ deserializes the JSON file to __objects """
        if os.path.isfile(self.__file_path) == False:
            return
        else:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                obj = json.load(file)
            for dico, de_valus in obj.items():
                name_class, id_1 = dico.split('.')
                model = name_class(**obj[dico])
                self.__objects[dico] = str(model)
