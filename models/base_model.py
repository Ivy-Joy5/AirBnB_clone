#!/usr/bin/python3
"""
Custom base class for the entire project
"""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """Custom base for all the classes in the AirBnb console project

    Attributes:
        id (str): handles unique user identity
        created_at (datetime): assigns current datetime
        updated_at (datetime): updates current datetime

    Methods:
        __str__: prints the class name, id, and creates dictionary
                 representations of the input values
        save(self): updates instance attributes with current datetime
        to_dict(self): returns the dictionary values of the instance obj
    """

    def __init__(self, *args, **kwargs):
        """Public instance attributes initialization after creation

        Args:
            *args: positional arguments (not used here)
            **kwargs: dictionary of attribute values
        """
        DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)  # Register the object in the storage system
        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(value, DATE_TIME_FORMAT)
                elif key == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """Returns string representation of the class"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the 'updated_at' attribute with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.save()  # Save the changes to the storage system

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        # Use dictionary comprehension to simplify the code
        return {key: value.isoformat() if isinstance(value, datetime) else value
                for key, value in self.__dict__.items()
                } | {"__class__": self.__class__.__name__}

