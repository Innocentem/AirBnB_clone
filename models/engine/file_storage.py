#!/usr/bin/python3
"""
File storage module engine
"""
import os
import json


class FileStorage:
    """Serialization of instance to JSON and Deserialize JSON to instance"""
    __objects: dict = dict()
    __file_path: str = "file.json"

    def all(self):
        """Returns the dictionary __objects"""
        return type(self).__objects

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_obj = type(self).__objects
        path = type(self).__file_path
        with open(path, 'w', encoding='UTF-8') as file:
            json.dump(
                {key: value.to_dict() for key, value in new_obj.items()},
                file,
                indent=4
            )

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        type(self).__objects[f"{obj.__class__.__name__}"] = obj

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        path = type(self).__file_path
        if os.path.exists(path):
            with open(path, "r") as file:
                FileStorage.__objects = json.load(file)
