#!/usr/bin/python3
""" module of the base class of Abhnb """
import uuid
from datetime import datetime
import datetime

class BaseModel():
    """ the base class of Abhnb """
    def __init__(self):
        """ 
        generate an id for each object and also 
        generate the time which each item will be created at 
        """
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now()

    def __str__(self):
        """ return the object in a specified format """
        self.created_at = repr(self.created_at)
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ 
        updates the public instance attribute 
        updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        self.updated_at = repr(self.updated_at)

    def to_dict(self):
        """ 
        returns a dictionary containing all keys/values of 
        __dict__ of the instance
        """
        self.created_at = datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
        dict = self.__dict__
        dict["__class__"] = __class__.__name__
        return dict
