#!/usr/bin/python3
"""
The file storage module
"""
from datetime import datetime
import os
from models.base_model import BaseModel
from models.user import User
import json


class FileStorage():
    """
    That class will orginize all information of every object
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return the objects dictionary """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        element = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects.update({element:obj})

    def save(self):
        """  serializes __objects to the JSON file (path: __file_path)
        i created new_objects dictionary in different location becuase 
        when we iterate over __objects dictionary we will an error which
        is value has no to_dict method because that value will be dictionary no object
        that thing will happen when we create an object for first time but it happen
        when we create an object for the second time
        """
        new_objects = FileStorage.__objects.copy()
        for key, value in  FileStorage.__objects.items():
            new_objects[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(new_objects, f)

    def reload(self):
        """Deserialize the JSON file"""
        """ deserializes the JSON file to __objects """
        if os.path.isfile(FileStorage.__file_path) == False:
            return
        else:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                obj = json.load(file)
            for key, value in obj.items():
                name_class = obj[key]["__class__"]
                if name_class == "User":
                    model = User(**obj[key])
                else:
                    model = BaseModel(**obj[key])
                FileStorage.__objects[key] = model
