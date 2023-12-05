#!/usr/bin/python3
""" module of the base class of Abhnb """
import uuid
from datetime import datetime

class BaseModel():
    """ the base class of Abhnb """
    def __init__(self):
        """ 
        generate an id for each object and also 
        generate the time which each item will be created at 
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ return the object in a specified format """
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ 
        updates the public instance attribute 
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ 
        returns a dictionary containing all keys/values of 
        __dict__ of the instance
        """
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        dict = self.__dict__
        dict["__class__"] = __class__.__name__
        return dict
