#!/usr/bin/python3
"""
Base Model of the AirBnB project
"""
from datetime import datetime
import uuid


class BaseModel:
    """A class representation of the Base Model"""

    def __init__(self):
        """New Instance of the Base Model"""
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())

    def __str__(self):
        """A string representation of the class"""
        return "[{}] ({}) {}".format(
            type(self).__name__,
            self.id,
            self.__dict__
        )

    def to_dict(self):
        """Returns a dictionary representation of the class"""
        cur_dict = self.__dict__
        cur_dict["__class__"] = type(self).__name__
        return cur_dict

    def save(self):
        """Save the changes that have been made"""
        self.updated_at = datetime.now()
