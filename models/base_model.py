#!/usr/bin/python3
"""
BaseModel module
"""

from datetime import datetime
import uuid


class BaseModel:
    """A class representation of the Base Model"""

    def __init__(self):
        """New Instance of the Base Model"""
        self.created_at = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
        self.updated_at = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
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
        new_dict = self.__dict__
        new_dict["__class__"] = type(self).__name__
        return new_dict

    def save(self):
        """Save the changes that have been made"""
        self.updated_at = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
